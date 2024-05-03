import requests
from urllib.parse import urlparse

def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException as e:
        return False

def is_internal_url(url, base_url):
    parsed_url = urlparse(url)
    parsed_base_url = urlparse(base_url)
    return parsed_url.netloc == parsed_base_url.netloc or not parsed_url.netloc

def scan_for_ssrf_vulnerability(base_url):
    vulnerable_urls = []
    urls_to_check = [
        "http://localhost",
        "http://127.0.0.1",
        "http://[::1]",
        "http://localhost:5000",
        "http://127.0.0.1:5000",
        "http://[::1]:5000",
        "http://test",
        "http://example.com",
        "http://example.com:80",
        "http://169.254.169.254",
        "http://metadata.google.internal",
        "http://localhost/path/file.txt",
        "http://localhost:22",
        "http://www.google.com",  # Google home page URL
        # Add more URLs as needed
    ]
    for url_to_check in urls_to_check:
        full_url = f"{base_url}/{url_to_check}"
        if is_internal_url(full_url, base_url):
            if send_request(full_url):
                vulnerable_urls.append(full_url)
    return vulnerable_urls

if __name__ == "__main__":
    base_url = input("Enter the base URL of the web application: ")
    vulnerable_urls = scan_for_ssrf_vulnerability(base_url)
    if vulnerable_urls:
        print("Vulnerable URLs found:")
        for url in vulnerable_urls:
            print(url)
    else:
        print("No vulnerable URLs found.")

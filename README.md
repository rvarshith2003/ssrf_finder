# ssrf_finder
This tool is used to find if there are any Server-Side Request Forgery (SSRF) vulnerabilities on a particular website.

## Features

It is helpful in finding SSRF attacks on a website.
It also has separate word list file named "urls.txt" included which makes it to add any new URL's at ease.

## Technologies used

This tool is built using Python programming language.

## Installation and Usage

    Clone the repository:
    Navigate to the project directory.
    Install packages needed like Python, flask etc...
    Run the SSRF_finder.py file.
    Enter the URL for that specific website you want to find for when asked. URL should be in a specific format. Ex - "http://127.0.0.1:5000/?url="
    This tool will search for any SSRF vulnerabilities using the list of URL's from urls.txt file.
    If there are any vulnerabilities then the tool will show vulnerable URL's
    If not then it will show "No vulnerabilities found".
### Screenshots
![2024-05-03 18_41_22-Kali  Running  - Oracle VM VirtualBox](https://github.com/rvarshith2003/ssrf_finder/assets/107018042/1b633121-8a58-4418-8f34-484d55192fad) 
 ![2024-05-03 18_39_27-Kali  Running  - Oracle VM VirtualBox](https://github.com/rvarshith2003/ssrf_finder/assets/107018042/856b0660-3ee6-4653-8d1d-0aaf6a657667)
 ![2024-05-03 18_43_22-Kali  Running  - Oracle VM VirtualBox](https://github.com/rvarshith2003/ssrf_finder/assets/107018042/a4d0312f-46a1-45f1-9f3e-8b23bdd44248)

## Testing

To test the above tool you can use Python vulnerable website from the repository. The file is named as ssrf_vuln.py.

    Navigate to the project directory.
    Type "python3 ssrf_vuln.py" to start the vulnerable site.
    Then the code will give an IP address, that is used in launching the site. Ex - "127.0.0.1:5000"
    Copy and paste this IP address in your browser to start the vulnerable site.
    2024-05-03 18_50_46-Kali Running - Oracle VM VirtualBox
### Screenshot
![2024-05-03 18_50_46-Kali  Running  - Oracle VM VirtualBox](https://github.com/rvarshith2003/ssrf_finder/assets/107018042/fd1a3f1c-c6d2-49f9-afa6-b56e00c0f33a)

# ssrf_finder
This tool is used to find if there are any Server-Side Request Forgery (SSRF) vulnerabilities on a particular website.

Features

It is helpful in finding SSRF attacks on a website.
It also has separate word list file named "urls.txt" included which makes it to add any new URL's at ease.

Technologies used

This tool is built using Python programming language.

Installation and Usage

    Clone the repository:
    Navigate to the project directory.
    Install packages needed like Python, flask etc...
    Run the SSRF_finder.py file.
    Enter the URL for that specific website you want to find for when asked. URL should be in a specific format. Ex - "http://127.0.0.1:5000/?url="
    2024-05-03 18_41_22-Kali Running - Oracle VM VirtualBox
    This tool will search for any SSRF vulnerabilities using the list of URL's from urls.txt file.
    If there are any vulnerabilities then the tool will show vulnerable URL's
    2024-05-03 18_39_27-Kali Running - Oracle VM VirtualBox
    If not then it will show "No vulnerabilities found".
    2024-05-03 18_43_22-Kali Running - Oracle VM VirtualBox

Testing

To test the above tool you can use Python vulnerable website from the repository. The file is named as ssrf_vuln.py.

    Navigate to the project directory.
    Type "python3 ssrf_vuln.py" to start the vulnerable site.
    Then the code will give an IP address, that is used in launching the site. Ex - "127.0.0.1:5000"
    Copy and paste this IP address in your browser to start the vulnerable site.
    2024-05-03 18_50_46-Kali Running - Oracle VM VirtualBox


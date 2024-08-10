# Testing Insecure Cookie Flags

This project contains a Python script designed to analyze cookies returned by web servers and check for insecure cookie flags. The script assesses whether cookies are missing the `Secure`, `HttpOnly`, or domain initial dot flags, which could lead to potential security vulnerabilities.

## Features

- **Cookie Analysis:** Extracts cookies from HTTP responses and evaluates their security attributes.
- **Secure Flag Check:** Identifies cookies that are not marked as `Secure`, indicating that they might be transmitted over non-HTTPS connections.
- **HttpOnly Flag Check:** Detects cookies that are not marked as `HttpOnly`, making them potentially accessible to client-side scripts.
- **Domain Initial Dot Check:** Examines whether cookies have a loosely defined domain with an initial dot, making them accessible to subdomains.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arifbinekram/testing-insecure-cookie-flag.git
   cd testing-insecure-cookie-flag
   ```

2. **Install the required Python packages:**

   The script requires Python 3 and the `requests` library. Install the required package using pip:

   ```bash
   pip install requests
   ```

## Usage

1. **Run the script:**

   Execute the script using Python 3:

   ```bash
   python3 cookie_check.py
   ```

2. **Enter the URL when prompted:**

   The script will ask for a URL input. Provide the URL you want to analyze for cookie security.

## Output

- **Cookie Name and Value:** Displays the name and value of each cookie.
- **Secure Flag:** Indicates whether the cookie is marked as secure. Insecure flags are highlighted.
- **HttpOnly Flag:** Reports whether the cookie is marked as `HttpOnly`. Insecure flags are highlighted.
- **Domain Initial Dot:** Shows if the cookie domain is loosely defined. Loosely defined domains are highlighted.

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss potential improvements or features.

## Disclaimer

This tool is intended for educational and authorized testing purposes only. Ensure you have permission to test any system with this script, as unauthorized testing can be illegal and unethical.

## Acknowledgments

- Inspired by the need to evaluate cookie security for web applications.
- Thanks to the open-source community for providing tools and libraries that make projects like this possible.

---

For more information, visit the [project repository](https://github.com/arifbinekram/testing-insecure-cookie-flag).
```

This `README.md` file provides a detailed overview of the project, including its purpose, features, installation instructions, usage guidelines, and important notes about responsible use and contributions. Adjust any sections as needed to fit additional project specifics or updates.

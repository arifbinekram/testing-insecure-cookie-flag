import requests

# Prompt user for URL input
url = input("Enter the URL to check cookies: ").strip()

# Send an HTTP GET request to the specified URL
req = requests.get(url)

# Iterate over each cookie in the response
for cookie in req.cookies:
    print('Name:', cookie.name)
    print('Value:', cookie.value)

    # Check if the cookie is marked as secure
    if not cookie.secure:
        cookie.secure = '\x1b[31mFalse\x1b[39;49m'  # Mark as insecure in red
    print('Secure:', cookie.secure)

    # Check if the cookie is marked as HttpOnly
    if 'httponly' in cookie._rest.keys():
        cookie.httponly = 'True'
    else:
        cookie.httponly = '\x1b[31mFalse\x1b[39;49m'  # Mark as insecure in red
    print('HTTPOnly:', cookie.httponly)

    # Check if the cookie's domain is loosely defined
    if cookie.domain.startswith('.'):
        cookie.domain_initial_dot = '\x1b[31mTrue\x1b[39;49m'  # Mark as loosely defined in red
    else:
        cookie.domain_initial_dot = 'False'
    print('Loosely defined domain:', cookie.domain_initial_dot, '\n')

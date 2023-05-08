#!/usr/bin/env python3

import cgi

# Define the username and password
username = "admin"
password = "futuristic"

# Get the form data
form = cgi.FieldStorage()
user = form.getvalue("user")
pwd = form.getvalue("pass")

# Check if the username and password are correct
if user == username and pwd == password:
    # Successful login
    print("Content-Type: text/html")
    print("Set-Cookie: session_id=picoCTF{h6E4555DFYxdf5TIssDUx6}")
    print("Location: index.html\n")
else:
    # Incorrect username or password
    print("Content-Type: text/html\n")
    print("<html><head><title>Login Failed</title></head><body><h1>Login Failed</h1><p>Incorrect username or password.</p></body></html>")

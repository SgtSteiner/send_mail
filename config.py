# SMTP server
mail_host = "smtp.gmail.com"
mail_port = "587"

# Account info
mail_account = "name_acount@gmail.com"
mail_pwd = "xxxXXXxxx"
mail_from = "John Doe <john_doe@gmail.com>"

# Email address file list (with path)
mail_to_files = [
    "data/mail_examples.txt",
]
# Message data
mail_subject = "Subject Lorem Ipsum"
mail_body = """
    Lorem ipsum dolor sit amet.

    consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
"""

# List of attachments (indicating the path and the name with which it will be attached).
mail_attach_files = [
    ("data/lorem_ipsum.pdf", "lorem_ipsum.pdf"),
]

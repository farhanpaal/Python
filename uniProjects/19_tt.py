import re

email_pattern=r'^[A-Za-z0-9_+.-]+@[a-zA-Z0-9]+\.[A-Za-z]{2,}$'

emails=["farhan.12345.pala@gmail.com", "paal@gmail","test12@gmail.c"]

for i in emails:
    if re.match(email_pattern,i):
        print(i,"True")
    else:
        print(i,"false")
import re

date_pattern = r'\s(\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})'
email_pattern = r'\s[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
website_pattern = r'\s(https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?)'

with open('task_add.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    dates = re.findall(date_pattern, content)
    emails = re.findall(email_pattern, content)
    websites = re.findall(website_pattern, content)

print(dates, emails, websites)

import re
import csv

with open('task3.txt', 'r', encoding='utf-8') as file:
    table_content = file.read()

id = re.findall(r'(?<!\d-)\b[1-9]\d*\b(?!-\d)', table_content)
surnames = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]+\b', table_content)
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.[a-z]{2,}\b', table_content)
registration_dates = re.findall(r'\b\d{4}-\d{2}-\d{2}', table_content)
websites = re.findall(r'\bhttps?://[\w.-]+\.[a-z]{2,}\b', table_content)

with open('task3_output.csv', "w", newline='', encoding='UTF-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=";")
    csv_writer.writerow(["ID", "Фамилия", "Email", "Дата регистрации", "Сайт"])
    for row in zip(id, surnames, emails, registration_dates, websites):
        csv_writer.writerow(row)
print("Данные в task3.csv")
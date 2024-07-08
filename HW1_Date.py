from datetime import datetime

date_string = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
given_date = datetime.strptime(date_string, '%Y-%m-%d')
current_date = datetime.today()
difference = current_date - given_date
days_difference = difference.days
print(f"{days_difference}")

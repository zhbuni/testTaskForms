from string import digits


# Функция для валидации номера телефона
def validate_phone_number(number):
    if not number:
        return {}

    if len(number) != 12:
        return False

    if number[:2] != '+7':
        return False

    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    if len(set(number[1:]).intersection(digits)) != len(set(number[1:])):
        return False

    return True


# Функция для валидации почты
def validate_email(email):
    if not isinstance(email, str):
        return False

    if len(tuple(filter(lambda x: x, email.split('@')))) != 2:
        return False

    username, host = email.split('@')

    if len(tuple(filter(lambda x: x, host.split('.')))) != 2:
        return False
    return True


# Функция для валидации даты
def validate_date(date):
    if not isinstance(date, str):
        return False

    year, month, day = None, None, None

    if len(date.split('-')) == 3:
        year, month, day = date.split('-')

    if len(date.split('.')) == 3:
        day, month, year = date.split('.')

    if year is None:
        return False

    try:
        year = int(year)
    except ValueError:
        return False
    if len(str(year)) != 4:
        return False

    try:
        month = int(month)
    except ValueError:
        return False
    if not (1 <= month <= 12):
        return False

    try:
        day = int(day)
    except ValueError:
        return False

    if not (1 <= day <= 31):
        return False
    return True


def determine_type(value):
    if validate_date(value):
        return 'DATE'
    if validate_email(value):
        return 'EMAIL'
    if validate_phone_number(value):
        return 'PHONE_NUMBER'
    return 'TEXT'


phone = '+79191457369'
print(determine_type(phone))
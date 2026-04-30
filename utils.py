import random

def generate_email():
    random_number = random.randint(100, 999)
    return f'irina_dolmatova_43_{random_number}@gmail.com'

def generate_password():
    password = ''
    for _ in range(8):
        password += str(random.randint(0, 9))
    return password

class Email_and_Password():
    email='irina_dolmatova_43@gmail.com'
    password='123123123'
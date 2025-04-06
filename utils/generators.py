import random
import string

def generate_email():
    prefix = ''.join(random.choices(string.ascii_lowercase, k=6))
    domain = 'yandex.ru'
    return f"{prefix}_test_999@{domain}"

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_invalid_email():
    return "invalid-email"
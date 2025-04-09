import random
import string

def generate_email():

    # Списки для генерации
    names = ["анна", "иван", "мария", "алексей", "ольга"]
    surnames = ["иванова", "петров", "сидоров", "смирнов", "кузнецова"]
    domains = ["yandex.ru", "mail.ru", "gmail.com"]

    # Выбираем случайные компоненты
    name = random.choice(names)
    surname = random.choice(surnames)
    cohort = "9"  # Номер когорты
    digits = f"{random.randint(100, 999)}"
    domain = random.choice(domains)

    email = f"{name}_{surname}_{cohort}_{digits}@{domain}"
    return email
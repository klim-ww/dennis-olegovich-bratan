import math

a = 0.1 + 0.2
b = 0.3

print(a == b)              
print(math.isclose(a, b))





import re

def has_email(text):
    return re.search(r"\S+@\S+", text) is not None

print(has_email("Пишите на test@example.com"))  # True
print(has_email("Здесь нет адреса"))            # False




import os

filename = "empty.txt"

with open(filename, "w"):
    pass 

print(os.path.exists(filename))  
print(os.path.getsize(filename)) 









from datetime import datetime

LOG_FILE = "app.log"


def log_event(message):
    """Дописывает сообщение с текущей меткой времени в конец файла."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def show_today_events():
    """Выводит только записи за сегодняшний день."""
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(f"[{today}"):
                    print(line.rstrip())
    except FileNotFoundError:
        print("Лог-файл пока не создан.")


log_event("Приложение запущено")
log_event("Пользователь вошёл в систему")
show_today_events()
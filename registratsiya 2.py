# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 19:14:19 2026

@author: INFINITE CO
"""

name = input("Ismingizni kiriting: ")

if "s" in name.lower():
    print("Ismingiz qabul qilindi")
else:
    print("Ismingiz qabul qilinmadi")

age = int(input("Yoshingizni kiriting: "))

if age >= 11:
    print("Registratsiyadan o‘tdingiz")
else:
    print("Yoshingiz yetarli emas")

login = input("Login kiriting: ")
password = input("Parol kiriting: ")

if login == "admin" and password == "1234":
    print("Kirish muvaffaqiyatli")
else:
    print("Login yoki parol xato")

password = input("Yangi parol kiriting: ")

if len(password) >= 6:
    print("Parol qabul qilindi")
else:
    print("Parol juda qisqa")

phone = input("Telefon raqam kiriting: ")

if len(phone) == 9:
    print("Telefon raqam to‘g‘ri")
else:
    print("Telefon raqam noto‘g‘ri")

email = input("Email kiriting: ")

if "@" in email:
    print("Email qabul qilindi")
else:
    print("Email noto‘g‘ri")

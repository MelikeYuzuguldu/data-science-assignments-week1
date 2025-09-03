year_of_birth=int(input("Dogum Yilinizi Giriniz:"))

age=2025-year_of_birth

if 0<=age & age<=12:
    print("Cocuksunuz...")

if 13<=age & age<=17:
    print("Ergensiniz...")

if 18<=age:
    print("Yetiskinsiniz...")

else:
    print("Gecersiz Tarih Girdiniz!")
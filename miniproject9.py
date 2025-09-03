product1=int(input("Birinci Urunun Fiyatini Giriniz:"))

product2=int(input("Ikinci Urunun Fiyatini Giriniz:"))

product3=int(input("Ucuncu Urunun Fiyatini Giriniz:"))

sum_price=product1+product2+product3
print("Urunlerin Toplam Fiyati:",sum_price)

if sum_price>200:
    print("Tebrikler , %10 indirim kazandiniz...")
    discount=(sum_price*10)/100
    discount_price=sum_price-discount
    print("Odenecek Tutar:",discount_price)

else:
    print("Odenecek Tutar:",sum_price)
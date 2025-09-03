price=int(input("Urunun Fiyatini Giriniz:"))

print("Urun Fiyati:",price)

discount_rate=float(input("İndirim oranini giriniz (%):"))

print("İndirim oraniniz :%",discount_rate)

discount=(price*discount_rate)/100

discounted_price=price-discount

print("Indirimli Fiyati:",discounted_price)
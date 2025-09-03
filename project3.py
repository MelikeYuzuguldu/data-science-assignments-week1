kelime = "merhaba"

ilk = kelime[0]   # indeksler 0'dan başlar

son = kelime[-1]  # -1 her zaman son karakteri verir

uzunluk = len(kelime)  # len() fonksiyonu uzunluğu bulur

ters = kelime[::-1]    # [başlangıç:bitiş:adım] → adım -1 olursa ters çevirir

print("İlk karakter:", ilk)
print("Son karakter:", son)
print("Uzunluk:", uzunluk)
print("Ters hali:", ters)
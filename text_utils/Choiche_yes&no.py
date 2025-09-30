import secrets

satu = "Iya"
dua = "Tidak"

hasil = secrets.choice([satu, dua])
print("Hasil acak (secure):", hasil)

import secrets

satu = "lakukan"
dua = "jangan lakukan"

hasil = secrets.choice([satu, dua])
print("Hasil acak (secure):", hasil)

import secrets

satu = "lakukan"
dua = "jangfan lakukan"

hasil = secrets.choice([satu, dua])
print("Hasil acak (secure):", hasil)

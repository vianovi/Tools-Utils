import os, numpy as np

opsi = ["iya", "Tidak"]

rand_byte = int.from_bytes(os.urandom(1), "big")

hasil = np.random.choice(opsi) if rand_byte % 2 == 0 else np.random.choice(opsi[::-1])

print("Jawaban super random:", hasil)

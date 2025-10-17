from pdf2docx import Converter
import os
import re

input_folder = "/home/silinux/Documents/IBU"
output_folder = "/home/silinux/Documents/IBU_result"

os.makedirs(output_folder, exist_ok=True)

def sanitize_filename(name):
    # Hilangkan karakter aneh
    name = re.sub(r'[^A-Za-z0-9_.-]', '_', name)
    # Potong kalau kepanjangan
    if len(name) > 100:
        name = name[:100]
    return name

for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        safe_name = sanitize_filename(file)
        if safe_name != file:
            os.rename(
                os.path.join(input_folder, file),
                os.path.join(input_folder, safe_name)
            )
            file = safe_name  # update nama file setelah rename

        pdf_path = os.path.join(input_folder, file)
        docx_path = os.path.join(output_folder, file.replace(".pdf", ".docx"))

        print(f"Converting {file} -> {os.path.basename(docx_path)}")
        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
        except Exception as e:
            print(f"[ERR] Gagal convert {file}: {e}")

print("✅ Semua PDF dicoba convert pakai pdf2docx")

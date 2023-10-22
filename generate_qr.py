import qrcode

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    file_name += ".png"  # Tambahkan ekstensi .png

    image.save(file_name)
    print(f"Kode QR telah disimpan dalam file: {file_name}")

# Meminta pengguna untuk memasukkan link YouTube dan nama file
link_youtube = input("Masukkan link YouTube: ")
nama_file = input("Masukkan nama file: ")
generate_qr_code(link_youtube, nama_file)

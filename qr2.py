import qrcode
kod = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
kod.add_data("Warsztaty matematyczne")
kod.make(fit=True)
obraz = kod.make_image(fill_color="black", back_color="white")
obraz.save("warsztaty.png")
print("Wersja kodu:", kod.version)

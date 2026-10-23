import qrcode
tresc = "Kochamy uczyć się Analizę Matematyczą"
obraz = qrcode.make(tresc)

obraz.save("QR23102026.png")

print("Gotowe")





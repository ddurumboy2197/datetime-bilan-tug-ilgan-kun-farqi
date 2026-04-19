from datetime import datetime, date

def kunlar_soni(tugilgan_sana, hozirgi_sana):
    tugilgan_sana = datetime.strptime(tugilgan_sana, "%Y-%m-%d")
    hozirgi_sana = datetime.strptime(hozirgi_sana, "%Y-%m-%d")
    farq = hozirgi_sana - tugilgan_sana
    return farq.days

tugilgan_sana = input("Tug'ilgan sana: ")
hozirgi_sana = date.today().strftime("%Y-%m-%d")
print(kunlar_soni(tugilgan_sana, hozirgi_sana))

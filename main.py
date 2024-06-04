import pandas as pd
from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta 

def main():
    try:  
        personel1 = Personel(1, "Ali", "Soyak", "Acil", 7500)
        personel2 = Personel(2, "Ayşe", "Akarsu", "Cerrahi", 9900)
        print(personel1)
        print(personel2)

        doktor1 = Doktor(3, "Ateş", "Yavaş", "Kardiyoloji", 44600, "Kardiyolog", 6, "Hastane 1")
        doktor2 = Doktor(4, "Mehmet", "Uçar", "Plastik Cerrahi", 83000, "Plastik Cerrah", 15, "Hastane 2")
        doktor3 = Doktor(5, "Elif", "Sönmez", "Jinekoloji", 65000, "Jinekolog", 12, "Hastane 3")
        print(doktor1)
        print(doktor2)
        print(doktor3)


        hemsire1 = Hemsire(6, "Asiye", "Kara", "Yoğun Bakım", 22600, 40, "Yoğun Bakım Sertifikası", "Hastane 1")
        hemsire2 = Hemsire(7, "Ayten", "Petek", "Anestezi", 19000, 38, "Anestezi Sertifikası", "Hastane 2")
        hemsire3 = Hemsire(8, "Songül", "Güneş", "Onkoloji", 18600, 36, "Onkoloji Sertifikası", "Hastane 3")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)


        hasta1 = Hasta(1, "Filiz", "Tokgöz", "13.05.1966", "grip", "normal tedavi")
        hasta2 = Hasta(2, "Ayşe", "Toprak", "16.01.1973", "ishal", "normal tedavi")
        hasta3 = Hasta(3, "Mehmet", "Çelik", "30.12.1998", "farenjit", "özel tedavi")
        print(hasta1)
        print(hasta2)
        print(hasta3)

        data = [
            [personel1.get_ad(), personel1.get_soyad(), personel1.get_departman(), personel1.get_maas(), None, None,
             None, None, None],
            [personel2.get_ad(), personel2.get_soyad(), personel2.get_departman(), personel2.get_maas(), None, None,
             None, None, None],
            [doktor1.get_ad(), doktor1.get_soyad(), doktor1.get_departman(), doktor1.get_maas(), doktor1.get_uzmanlik(),
             doktor1.get_deneyim_yili(), None, None, None],
            [doktor2.get_ad(), doktor2.get_soyad(), doktor2.get_departman(), doktor2.get_maas(), doktor2.get_uzmanlik(),
             doktor2.get_deneyim_yili(), None, None, None],
            [doktor3.get_ad(), doktor3.get_soyad(), doktor3.get_departman(), doktor3.get_maas(), doktor3.get_uzmanlik(),
             doktor3.get_deneyim_yili(), None, None, None],
            [hemsire1.get_ad(), hemsire1.get_soyad(), hemsire1.get_departman(), hemsire1.get_maas(), None, None, None,
             None, None],
            [hemsire2.get_ad(), hemsire2.get_soyad(), hemsire2.get_departman(), hemsire2.get_maas(), None, None, None,
             None, None],
            [hemsire3.get_ad(), hemsire3.get_soyad(), hemsire3.get_departman(), hemsire3.get_maas(), None, None, None,
             None, None],
            [hasta1.get_ad(), hasta1.get_soyad(), None, None, None, None, hasta1.get_hastalik(), hasta1.get_tedavi(), hasta1.get_dogum_tarihi()],
            [hasta2.get_ad(), hasta2.get_soyad(), None, None, None, None, hasta2.get_hastalik(), hasta2.get_tedavi(), hasta2.get_dogum_tarihi()],
            [hasta3.get_ad(), hasta3.get_soyad(), None, None, None, None, hasta3.get_hastalik(), hasta3.get_tedavi(), hasta3.get_dogum_tarihi()],
        ]

        df = pd.DataFrame(data, columns=["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık","Tedavi", "Doğum Tarihi"])

        df.fillna(0, inplace=True) # Boş değişkenleri 0 ile doldurma

        doktor_uzmanlık = df[df["Uzmanlık"] != 0].groupby("Uzmanlık").size()
        print("Doktorları uzmanlık alanlarına göre gruplandırma:\n", doktor_uzmanlık)

        deneyimli_doktorlar = df[(df["Deneyim Yılı"] > 5)]
        print("5 yıldan fazla deneyime sahip olan doktorlar:\n", deneyimli_doktorlar)

        hasta_df = df[df["Hastalık"] != 0]
        hasta_df_sıralama = hasta_df.sort_values("Ad")
        print("Hasta adına göre alfabetik sıralama:\n", hasta_df_sıralama)

        maasi_yuksek_personel = df[(df["Maaş"] > 7000)]
        print("Maaşı 7000 TL üzerinde olan personeller:\n", maasi_yuksek_personel)
     
    except Exception:
        print("Bir hata oluştu")



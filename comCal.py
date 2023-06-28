import time
from colorama import Fore, Back, Style

asgariUcret = 11402.32

print("Quartzz Complicated Calculator")
time.sleep(2)


def hesaplamaZamani():
  print(
    """
  [1] - Verilen Sayının """ + Fore.CYAN,
    "Karekökünü Alma",
    Fore.RESET,
    """\n[2] - Verilen Sayının""" + Fore.GREEN,
    "Küpünü Alma",
    Fore.RESET,
    """\n[3] - Verilen Oranda""" + Fore.LIGHTMAGENTA_EX,
    "Zam Hesaplama",
    Fore.RESET,
    """\n[4] - Verilen Oranda""" + Fore.RED,
    "İndirim Hesaplama",
    Fore.RESET,
    """\n[5] - İstenilen Şekilde""" + Fore.YELLOW,
    "İşçi Maaş Hesaplama",
    Fore.RESET,
    """\n[6] - Verilen Bilgilere Göre""" + Fore.LIGHTCYAN_EX,
    "Çember Alan/Çevre Hesaplama",
    Fore.RESET,
  )
  secim = input("")
  secim = int(secim)

  if (secim == 1):
    karekokSayi = input(
      "Karekökünü Almak İstediğiniz Sayıyı Giriniz : (Tam Sayı) ")
    karekokSayi = int(karekokSayi)

    karekokSayi2 = (karekokSayi**2)
    time.sleep(1)
    print(karekokSayi, "in/ın Karekökü", karekokSayi2, "dir")

  elif (secim == 2):
    karekokSayi = input(
      "Küpünü Almak İstediğiniz Sayıyı Giriniz : (Tam Sayı) ")
    karekokSayi = int(karekokSayi)

    karekokSayi2 = (karekokSayi**3)
    time.sleep(1)
    print(karekokSayi, "in/ın Küpü", karekokSayi2, "dir")

  elif (secim == 3):
    zamsizFiyat = input("Zamsız Miktarı Girin : " +
                        "(Tam Sayı Olmak Zorunda Değildir) ")
    time.sleep(1)
    zamOran = input("Zam Oranını Giriniz : " +
                    "(Tam Sayı Olmak Zorunda Değildir) ")

    zamsizFiyat = float(zamsizFiyat)
    zamOran = float(zamOran)

    eklenecekFiyat = (zamsizFiyat * zamOran) / 100.0

    print("Hesaplanıyor . . . ")
    time.sleep(2)
    print("Zamsız Fiyat", Fore.BLUE + str(zamsizFiyat) + Style.RESET_ALL,
          "--->", "Zamlı Fiyat",
          Fore.RED + str(zamsizFiyat + eklenecekFiyat) + Style.RESET_ALL)

  elif (secim == 4):
    indirimsizFiyat = input("İndirimsiz Miktarı Girin : " +
                            "(Tam Sayı Olmak Zorunda Değildir) ")
    time.sleep(1)
    indirimOran = input("İndirim Oranını Giriniz : " +
                        "(Tam Sayı Olmak Zorunda Değildir) ")

    indirimsizFiyat = float(indirimsizFiyat)
    indirimOran = float(indirimOran)

    cikarilacakMiktar = (indirimsizFiyat * indirimOran) / 100.0

    print(
      "İndirimsiz Fiyat", Fore.BLUE + str(indirimsizFiyat) + Style.RESET_ALL,
      "--->", "İndirimli Fiyat",
      Fore.RED + str(indirimsizFiyat - cikarilacakMiktar) + Style.RESET_ALL)

  elif (secim == 5):
    isciSayi = input("İşçi Sayınızı Giriniz : ")
    isciSayi = int(isciSayi)

    odenecekMiktar = float(isciSayi * asgariUcret)

    print(
      "İşçi Başı Asgari Olarak 2023 Yılında Vermeniz Gereken Miktar " +
      Fore.RED + str(asgariUcret), Style.RESET_ALL)
    time.sleep(2)
    print(Fore.RED + str(isciSayi) + Style.RESET_ALL,
          "Kadar İşçiniz Var. Toplam Aylık Ödemeniz Gereken Min. Miktar:",
          str(odenecekMiktar), "TL")
    time.sleep(3)

  elif (secim == 6):
    pi = 3
    r = input("Çember Yarıçapını Gir :")
    r = int(r)

    alan = pi * (r**2)
    cevre = 2 * pi * r

    print("Çember Alanı : ", Fore.BLUE + str(alan), Fore.RESET,
          "Çember Çevresi : ", Fore.GREEN + str(cevre))
  else:
    print("Yanlış Giriş Yaptınız Tekrardan Deneyiniz . . .")


hesaplamaZamani()

if "__name__" == "__name__":
  hesaplamaZamani()

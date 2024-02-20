sifre = input("Lütfen şifreyi girin: ")

if not(4 <= len(sifre) <= 8):
    if len(sifre) < 4:
        print("Şifre çok kısa. (Geçersiz Şifre)")
    else:
        print("Şifre en fazla 8 karakter olabilir. (Geçersiz Şifre)")
else:
    if not any(karakter.islower() for karakter in sifre):
        print("Şifre en az bir küçük harf içermeli. (Geçersiz Şifre)")
    elif not any(karakter.isupper() for karakter in sifre):
        print("Şifre en az bir büyük harf içermeli. (Geçersiz Şifre)")
    elif not any(karakter.isdigit() for karakter in sifre):
        print("Şifre en az bir rakam içermeli. (Geçersiz Şifre)")
    elif not any(karakter in '()*+,-.çÇğĞIıİiÖöşŞüÜ' for karakter in sifre):
        print("Şifre izin verilen özel karakterlerden en az birini içermeli. (Geçersiz Şifre)")
    else:
        print("Geçerli Şifre")

        kucuk_harf_sayisi = sum(1 for karakter in sifre if karakter.islower())
        buyuk_harf_sayisi = sum(1 for karakter in sifre if karakter.isupper())
        rakam_sayisi = sum(1 for karakter in sifre if karakter.isdigit())
        ozel_karakter_sayisi = sum(1 for karakter in sifre if not karakter.isalnum())
        
        gucluluk_skoru = 3 * (kucuk_harf_sayisi + 1) * 5 * (buyuk_harf_sayisi + 1) * 2 * (rakam_sayisi + 1) * 4 * (ozel_karakter_sayisi + 1) - 120

        if gucluluk_skoru < 2000:
            print("Şifre Güçlülük Skoru:" , gucluluk_skoru , "(Çok Zayıf Şifre)")
        elif 2000 <= gucluluk_skoru < 4000:
            print("Şifre Güçlülük Skoru:" , gucluluk_skoru , "(Zayıf Şifre)")
        elif 4000 <= gucluluk_skoru < 6000:
            print("Şifre Güçlülük Skoru:" , gucluluk_skoru , "(Ortalama Şifre)")
        elif 6000 <= gucluluk_skoru < 9000:
            print("Şifre Güçlülük Skoru:" , gucluluk_skoru , "(Güçlü Şifre)")
        else:
            print("Şifre Güçlülük Skoru:" , gucluluk_skoru , "(Çok Güçlü Şifre)")
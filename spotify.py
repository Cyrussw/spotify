# Ben Sairus, Burak tarafından spotify üzerinde hızlı işlemler yapmanız için geliştirildim.
# Burak - Cyrus - 23.07.2023

from config import *
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

# Temiz bir sayfa açalım

os.system("cls")

# OAuth 2.0 yetkilendirme işlemi
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

print("Sairus: Yapılıcak işlemi giriniz. (İşlemleri bilmiyorsanız yardım yazmanız yeterli olucaktır.)")

try:
    while True:
        islem = input("İşlem: ").lower()

        if not islem:
            print("Sairus: Lütfen bir işlem giriniz.")
        elif islem == "yardım":
            print("Sairus: Yardım menüsüne hoş geldiniz.")
            print("1. Müziği Başlat/Durdur")
            print("2. Hangi Müzik Çalıyor.")
            print("3. Müzik Çalıyormu?")
            print("0. Kapat")

        # Müzik Başlat Durdur
        elif islem == "müzik":
            # Kullanıcının mevcut çalma durumunu al
            current_playback = sp.current_playback()

            if current_playback:
                is_playing = current_playback["is_playing"]
                if is_playing:
                    print(
                        "Sairus: Müziği Durdurmak İçin (evet-e) yada (hayır-h) giriniz.")
                    altIslem = input("İşlem: ").lower()

                    if altIslem == "evet" or altIslem == "e":
                        sp.pause_playback()
                    elif altIslem == "hayır" or altIslem == "h":
                        print("Sairus: İşlem İptal Edildi!")
                else:
                    print(
                        "Sairus: Müziği Başlatmak İçin (evet-e) yada (hayır-h) giriniz.")
                    altIslem = input("İşlem: ").lower()

                    if altIslem == "evet" or altIslem == "e":
                        sp.start_playback()
                    elif altIslem == "hayır" or altIslem == "h":
                        print("Sairus: İşlem İptal Edildi!")
            else:
                print("Sairus: Şuanda müzik dinlemiyorsunuz.")

        # Müziği Durdur.
        elif any(word in islem for word in pauseMusicList):
            current_playback = sp.current_playback()

            if current_playback:
                is_playing = current_playback["is_playing"]
                if is_playing:
                    sp.pause_playback()
                    print("Sairus: Müzik durduruldu!")
                else:
                    print("Sairus: Şuanda müzik çalmıyor.")
            else:
                print("Sairus: Şuanda müzik çalmıyor.")

        # Müziği Başlat.
        elif any(word in islem for word in playMusicList):
            current_playback = sp.current_playback()

            if current_playback:
                is_playing = current_playback["is_playing"]
                if is_playing:
                    print("Sairus: Müzik zaten çalıyor.")
                else:
                    sp.start_playback()
                    print("Sairus: Müzik başlatıldı!")
            else:
                print("Sairus: Şuanda müzik çalmıyor.")

        # Müzik Çalıyor Mu?
        elif any(word in islem for word in musicStatusList):
            current_playback = sp.current_playback()

            if current_playback:
                is_playing = current_playback["is_playing"]
                if is_playing:
                    print("Sairus: Müzik çalıyor.")
                else:
                    print("Sairus: Müzik çalmıyor!")
            else:
                print("Sairus: Şuanda müzik çalmıyor.")

        # Hangi Müzik Çalıyor
        elif any(word in islem for word in whatsPlayingList):
            current_playback = sp.current_playback()
            if current_playback:
                is_playing = current_playback["is_playing"]
                if is_playing:
                    track_name = current_playback["item"]["name"]
                    artist_name = current_playback["item"]["artists"][0]["name"]
                    print(f"Sairus: Şu anda çalınan şarkı: {track_name} - {artist_name}")
                else:
                    print("Sairus: Şuanda müzik çalmıyor.")
            else:
                print("Sairus: Şuanda müzik çalmıyor.")

        # Programı Sonlandır.
        elif any(word in islem for word in closeProgramList):
            print("Sairus: Program kapatılıyor görüşmek üzere!")
            break
except Exception as e:
    print(f"Sairus: Bir Hata Meydana Geldi!\nHata: {e}")

# Sairus - Spotify İşlem Yöneticisi

Sairus, Spotify üzerinde hızlı işlemler yapmak için Burak tarafından geliştirilmiş bir Python betiğidir.

## Nasıl Kullanılır?

1. Öncelikle `config.py` dosyasında Spotify API için gerekli olan `CLIENT_ID`, `CLIENT_SECRET` ve `REDIRECT_URI` gibi bilgileri doldurmalısınız. Ayrıca izin kapsamlarını belirlemek için `SCOPE` listesini güncellemelisiniz.

2. Ardından betiği çalıştırarak Sairus'u başlatın.

3. Sairus size çeşitli işlemler için komutlar sunacaktır. Bu komutları girerek Spotify üzerinde işlemler yapabilirsiniz.

## Kullanılabilir Komutlar:

- `müzik`: Müziği başlatmak veya durdurmak için bu komutu kullanabilirsiniz.
- `duraklat`, `durdur`, `müziği duraklat`, `müziği durdur`: Müziği durdurmak için bu komutları kullanabilirsiniz.
- `başlat`, `oynat`, `müziği başlat`, `müziği oynat`: Müziği başlatmak için bu komutları kullanabilirsiniz.
- `müzik çalıyor mu`, `çalıyor mu`: Şu anda müziğin çalıp çalmadığını öğrenmek için bu komutları kullanabilirsiniz.
- `hangi müzik çalıyor`, `ne çalıyor`: Şu anda çalınmakta olan şarkının adını ve sanatçısını öğrenmek için bu komutları kullanabilirsiniz.
- `yardım`: Yardım menüsünü görüntülemek için bu komutu kullanabilirsiniz.
- `kapat`, `programı kapat`: Sairus'u kapatmak için bu komutları kullanabilirsiniz.

## Önemli Not

- Sairus, Spotify API ile etkileşimde bulunabilmek için OAuth 2.0 yetkilendirmesi kullanmaktadır. Bu nedenle `spotipy` kütüphanesini kullanarak Spotify hesabınıza erişim sağlamaktadır. Lütfen bu betiği güvenli bir ortamda kullanmaya özen gösterin ve gerekli izinleri verdiğinizden emin olun.

- Betiği çalıştırmadan önce `spotipy` ve diğer gereksinimleri yüklediğinizden emin olun.

- Herhangi bir hata veya sorunla karşılaşırsanız, lütfen Burak ile iletişime geçin. 

## Geliştirici

- Burak (GitHub: burak)

---
*Oluşturma tarihi: 23.07.2023*

# Konuşma için farklı varyasyonlar.
closeProgramList = ["kapan", "kapat", "programı sonlandır", "sonlandır", "bitir", "çık", "çıkış", "son", "son ver", "sonlandırma", "kapatma",
                    "programı bitir", "programı kapat", "programı sona erdir", "programı sonla", "uygulamayı kapat", "uygulamayı durdur", "uygulamayı bitir"]

pauseMusicList = ["müziği durdur", "müzik dur", "durdur", "müziği kapat", "şarkıyı durdur", "şarkı dur", "şarkıyı kapat", "sesi durdur", "ses dur", "sesi kapat", "çalmayı durdur",
                  "çalma dur", "çalmayı kapat", "duraklat", "duraklat müziği", "müziği askıya al", "şarkıyı askıya al", "sesi askıya al", "çalmayı askıya al", "müziği duraklat", "şarkıyı duraklat"]

playMusicList = ["başlat", "oynat", "müzik başlat", "müziği başlat", "müziği çal", "şarkıyı başlat", "şarkıyı çal", "sesi aç", "müziği çalmaya başla", "şarkıyı çalmaya başla", "müziği aç", "şarkıyı aç", "çalmayı başlat", "çalmaya başla", "müziği oynat",
                 "şarkıyı oynat", "müziği çalmak için başlat", "şarkıyı çalmak için başlat", "çalmaya başlamak için", "oynatmaya başla", "müziği başlatmaya yardımcı ol", "şarkıyı başlatmaya yardımcı ol", "müziği oynatmaya başla"]

musicStatusList = ["müzik çalıyor mu", "çalıyor mu", "şarkı çalıyor mu", "müzik açık mı", "şarkı açık mı", "müzik çalıyor mu?", "şarkı çalıyor mu?", "müzik duraklatıldı mı", "şarkı duraklatıldı mı", "müzik duraklatıldı mı?", "şarkı duraklatıldı mı?",
                   "müzik devam ediyor mu", "şarkı devam ediyor mu", "müzik hâlâ çalıyor mu", "şarkı hâlâ çalıyor mu", "müzik devam ediyor mu?", "şarkı devam ediyor mu?", "çalmaya devam ediyor mu", "müziği kontrol et", "müziği sorgula", "çalıyor mu müzik"]

whatsPlayingList = ["hangi müzik çalıyor", "ne çalıyor", "hangi şarkı çalıyor", "çalan şarkı ne", "çalan müzik ne", "çalan şarkı nedir", "çalan müzik nedir", "hangi şarkı çalıyor şu anda", "hangi müzik çalıyor şu anda", "şu anda çalan şarkı ne", "şu anda çalan müzik ne",
                    "çalan şarkı hakkında bilgi ver", "çalan müzik hakkında bilgi ver", "çalan şarkının adı ne", "çalan müziğin adı ne", "çalan şarkı hangisi", "çalan müzik hangisi", "hangi müzik çalıyor şu an", "şu anda hangi müzik çalıyor", "şu anda çalan şarkıyı söyle", "şu anda çalan müziği söyle"]

# Uygulama bilgilerinizi buraya girin
CLIENT_ID = ""
CLIENT_SECRET = ""
# Spotify Developer Dashboard'da belirttiğiniz yönlendirme URI
REDIRECT_URI = "http://localhost:8000/callback"
# Spotify API yetkilendirmesi için gerekli izinler
SCOPE = "user-library-read app-remote-control user-modify-playback-state user-read-playback-state"

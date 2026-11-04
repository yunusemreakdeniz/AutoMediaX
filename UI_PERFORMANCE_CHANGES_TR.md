# AutoMediaX: Android Auto arayüz ve performans güncellemesi

## Kapsam
- Telefonun Android Auto bağlantı başlığındaki önceki/sonraki medya düğmelerinin dokunma alanı 52dp yerine 56dp yapıldı.
- Medya durumu sık değiştiğinde biriken arayüz çizim görevleri tek bekleyen göreve indirildi.
- Ekran denetleyicisi kapandıktan sonra bekleyen güncelleme görevi iptal ediliyor.
- GitHub Actions iş akışına kaynak kapsamı kontrolü eklendi.

## Özellikle değiştirilmedi
- Shizuku entegrasyonu ve izinleri.
- Sesli uyandırma ve çevrimdışı sesli asistan özellikleri (mevcut kaynakta bulunanlar).
- Sesli komut mantığı, mikrofon izinleri, servis bağlantıları ve yapay zekâ temizliği.

## Doğrulama sınırı
Bu ZIP'in kaynak sürüm ayarları 2.2.2'dir; 4.1.10 APK'sıyla eşdeğer olduğu doğrulanmamıştır.
Bu ortamda Android SDK/Gradle derlemesi çalıştırılmadı. Gerçek cihazda Android Auto testi gereklidir.

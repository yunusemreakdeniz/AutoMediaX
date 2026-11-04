# AutoMediaX gizlilik temizliği

- Özel Cloudflare ana sayfası bağlantısı kaldırıldı; başlangıç sayfası `about:blank`.
- `modules/chat` klasörü kaldırıldı. Zaten `settings.gradle` içinde üretimden hariç tutulmuştu.
- OpenAI, Groq, Gemini ve OpenRouter alan adlarının kaynak ve üretilen APK içinde bulunmadığını kontrol eden betik eklendi.
- GitHub Actions > Build privacy-clean APK > Run workflow ile derleme yapılabilir.
- Bu kaynak arşivi 2.2.2 sürüm ayarlarına sahiptir; önceki 4.1.10 APK'sıyla aynı özellikleri sunacağı garanti değildir.
- İş akışı yeni debug anahtarıyla imzalanabilir; eski uygulama üzerine yükleme imza uyuşmazlığı nedeniyle başarısız olabilir.
- Vosk bu kaynak ağacının etkin üretim modüllerinde yer almıyor; mevcut APK'daki çevrimdışı ses tanımanın korunacağı garanti edilmez.

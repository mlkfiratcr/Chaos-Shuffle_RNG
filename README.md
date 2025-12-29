# Chaos-Shuffle RNG 🎲

**Chaos-Shuffle RNG**, deterministik kaos teorisi (Logistic Map) ve bit seviyesi difüzyon tekniklerini (XOR & Rotation) kullanan, yüksek entropili bir sözde rastgele sayı üretecidir (PRBG).

## 📂 Proje Dökümantasyonu
Projenin tüm teknik detayları ve analiz raporlarına aşağıdaki bağlantılardan ulaşabilirsiniz:

- 📘 **[Algoritma Çalışma Mantığı](docs/Chaos-Shuffle_Algoritması_Çalışma_Mantığı.pdf)**: Kaotik sistemin matematiksel altyapısı ve mimari tasarım.
- 📊 **[Analiz Sonuçları](docs/Chaos-Shuffle_Algoritması_Analiz_Sonuçları.pdf)**: NIST testleri, bias analizi ve görsel dağılım testleri.
- 📝 **[Sözde Kod (Pseudocode)](docs/Chaos-Shuffle_Algoritması_Sözde_Kodu.pdf)**: Algoritmanın adım adım teknik akışı.
- 🚀 **[SMART Hedefler](docs/Chaos-Shuffle_Algoritması_SMART_Hedefler.pdf)**: Proje geliştirme süreci ve performans hedefleri.
- ⚖️ **[SWOT Analizi](docs/Chaos-Shuffle_Algoritması_SWOT_Analizi.pdf)**: Algoritmanın güçlü/zayıf yönleri ve stratejik analizi.

## 🚀 Kurulum ve Kullanım
```python
# Örnek Kullanım
from src.chaos_shuffle_rng import ChaosShuffleRNG

rng = ChaosShuffleRNG(seed=123456789012345)
print(rng.generate_hex(16))

# Chaos-Shuffle RNG Akış Şeması

```mermaid
graph TD
    Start([Başla]) --> Input[/15 Haneli Seed Al/]
    Input --> Init[Kaotik Durum x ve 64-bit State'i Başlat]
    Init --> Loop{Bit Üretimi Devam?}
    Loop -- Evet --> Chaos[Logistic Map Denklemi Uygula]
    Chaos --> XOR[Kaotik Maske ile State'i XOR'la]
    XOR --> Rotate[64-bit State'i 19 Bit Sola Döndür]
    Rotate --> Extract[En Düşük Biti Çıkar LSB]
    Extract --> Loop
    Loop -- Hayır --> Output[/Hex Çıktıyı Formatla/]
    Output --> End([Bitir])

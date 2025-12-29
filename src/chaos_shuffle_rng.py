import time

class ChaosShuffleRNG:
    """
    Chaos-Shuffle PRBG: Logistic Map ve Bitwise Shuffle kombinasyonu.
    Berat'ın Box-Box algoritmasına alternatif, kaotik bir yaklaşımdır.
    """
    def __init__(self, seed: int):
        # 15 haneli seed'i 64 bit sınırına çek
        self.state = seed & 0xFFFFFFFFFFFFFFFF
        # Kaotik sistem parametreleri (Logistic Map)
        self.mu = 3.99995  # Kaotik rejimi sağlayan katsayı
        self.x = ((seed % 10**7) / 10**7) 
        if self.x == 0: self.x = 0.5234 

    def generate_bit(self) -> int:
        # 1. Kaotik Aşama: Logistic Map x = mu * x * (1 - x)
        self.x = self.mu * self.x * (1 - self.x)
        kaotik_maske = int(self.x * 10**12) & 0xFF
        
        # 2. Karıştırma Aşaması: XOR ve Bit Rotasyonu
        self.state ^= (kaotik_maske << 56)
        # Sola dairesel kaydırma (Rotate Left 19 bit)
        self.state = ((self.state << 19) | (self.state >> 45)) & 0xFFFFFFFFFFFFFFFF
        
        # 3. Çıktı: En düşük anlamlı bit (LSB)
        return self.state & 1

    def generate_hex(self, byte_length=16):
        hex_result = ""
        for _ in range(byte_length * 2): # Her byte 2 hex karakteri
            nibble = 0
            for i in range(4): # 4 bit = 1 nibble (0-F)
                nibble = (nibble << 1) | self.generate_bit()
            hex_result += hex(nibble)[2:].upper()
        return hex_result

if __name__ == "__main__":
    # Challenge: Bu hex çıktısını üreten 15 haneli seed'i bulunuz!
    GIZLI_SEED = 123456789012345
    rng = ChaosShuffleRNG(GIZLI_SEED)
    print("="*40)
    print("CHAOS-SHUFFLE RNG ÇIKTISI (HEX):")
    print(rng.generate_hex(20))
    print("="*40)

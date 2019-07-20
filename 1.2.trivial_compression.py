class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)

    def _compress(self, gene):
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left 2 bits
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")
    def decompress(self):
        gene = []
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            bits = self.bit_string >> i & 0b11  # get just 2 relevent bits
            if bits == 0b00:
                gene.append("A")
            elif bits == 0b01:
                gene.append("C")
            elif bits == 0b10:
                gene.append("G")
            elif bits == 0b11:
                gene.append("T")
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return ''.join(gene[::-1])

    def __str__(self):
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof

    original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print(f"original is {getsizeof(original)} bytes")

    compressed = CompressedGene(original)
    print(f"compressed is {getsizeof(compressed.bit_string)} bytes")

    print(compressed)
    print(f"original and decompressed are the same: {original == compressed.decompress()}")

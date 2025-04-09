import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)

def build_codebook(root, current_code="", codebook=None):
    if codebook is None:
        codebook = {}
    
    if root.char is not None:
        codebook[root.char] = current_code
    else:
        build_codebook(root.left, current_code + "0", codebook)
        build_codebook(root.right, current_code + "1", codebook)
    
    return codebook

def huffman_encode(text, codebook):
    return ''.join([codebook[char] for char in text])

def huffman_decode(encoded_text, root):
    decoded = []
    current_node = root
    
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded.append(current_node.char)
            current_node = root
    
    return ''.join(decoded)

def calculate_compression_stats(frequencies, codebook):
    uniform_size = sum(freq * 3 for freq in frequencies.values())
    
    huffman_size = sum(freq * len(codebook[char]) for char, freq in frequencies.items())
    
    compression_ratio = huffman_size / uniform_size
    compression_percentage = (1 - compression_ratio) * 100
    
    return compression_ratio, compression_percentage

frequencies = {
    'A': 1,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 3,
    'F': 38,
    'G': 51
}

huffman_tree = build_huffman_tree(frequencies)

codebook = build_codebook(huffman_tree)
print("Кодовая таблица Хаффмана:")
for char, code in sorted(codebook.items()):
    print(f"{char}: {code}")

test_string = "GFFEDCBA" 
encoded = huffman_encode(test_string, codebook)
decoded = huffman_decode(encoded, huffman_tree)

print("\nПример кодирования/декодирования:")
print(f"Исходная строка: {test_string}")
print(f"Закодированная: {encoded}")
print(f"Раскодированная: {decoded}")

compression_ratio, compression_percentage = calculate_compression_stats(frequencies, codebook)
print("\nЭффективность сжатия:")
print(f"Коэффициент сжатия: {compression_ratio:.3f}")
print(f"Степень сжатия: {compression_percentage:.2f}%")
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def arithmetic_encode(symbols, probabilities, string):
    low = 0.0
    high = 1.0
    
    ranges = {}
    current_low = 0.0
    for sym, prob in zip(symbols, probabilities):
        ranges[sym] = (current_low, current_low + prob)
        current_low += prob
    
    for char in string:
        range_width = high - low
        high = low + range_width * ranges[char][1]
        low = low + range_width * ranges[char][0]
    
    value = (low + high) / 2
    binary_code = float_to_binary(value)
    
    return binary_code

def float_to_binary(value):
    binary = ""
    for _ in range(20):
        value *= 2
        bit = int(value)
        binary += str(bit)
        value -= bit
        if value == 0:
            break
    return binary

def calculate_compression_stats(original_length, encoded_length, bits_per_symbol=3):
    uniform_size = original_length * bits_per_symbol
    compression_ratio = encoded_length / uniform_size
    compression_percentage = (1 - compression_ratio) * 100
    return compression_ratio, compression_percentage

symbols = ['a', 'b', 'c', 'd', 'e', 'f']
probabilities = [0.10, 0.15, 0.05, 0.50, 0.10, 0.10]
string = "acefdb"

binary_code = arithmetic_encode(symbols, probabilities, string)

original_length = len(string)
encoded_length = len(binary_code)
compression_ratio, compression_percentage = calculate_compression_stats(
    original_length, encoded_length)

print("Исходная строка:", string)
print("Закодированная двоичная строка:", binary_code)
print("Длина закодированной строки:", encoded_length, "бит")
print("Коэффициент сжатия:", f"{compression_ratio:.3f}")
print("Степень сжатия:", f"{compression_percentage:.2f}%")
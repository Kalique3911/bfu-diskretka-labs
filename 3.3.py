import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def rle_compress(data):
    compressed = bytearray()
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        repeat_count = 1
        while i + repeat_count < n and data[i + repeat_count] == current_char and repeat_count < 255:
            repeat_count += 1
        
        if repeat_count > 1:
            compressed.append(repeat_count)
            compressed.append(ord(current_char))
            i += repeat_count
        else:
            non_repeat_start = i
            non_repeat_count = 0
            while i + non_repeat_count < n and (non_repeat_count == 0 or data[i + non_repeat_count] != data[i + non_repeat_count - 1]) and non_repeat_count < 255:
                non_repeat_count += 1
            
            if non_repeat_count > 1 and i + non_repeat_count < n and data[i + non_repeat_count] == data[i + non_repeat_count - 1]:
                non_repeat_count -= 1
            
            compressed.append(0)
            compressed.append(non_repeat_count)
            for j in range(non_repeat_count):
                compressed.append(ord(data[i + j]))
            i += non_repeat_count
    
    return compressed

def calculate_compression_ratio(original, compressed):
    original_size = len(original)
    compressed_size = len(compressed)
    ratio = compressed_size / original_size
    compression_percentage = (1 - ratio) * 100
    return ratio, compression_percentage

original_string = "adddqhtyyyyyyyyikloppppppppppp"

compressed_data = rle_compress(original_string)

compression_ratio, compression_percentage = calculate_compression_ratio(original_string, compressed_data)

print("Исходная строка:", original_string)
print("Длина исходной строки:", len(original_string), "байт")
print("Сжатые данные (в байтах):", list(compressed_data))
print("Длина сжатых данных:", len(compressed_data), "байт")
print("Коэффициент сжатия:", f"{compression_ratio:.3f}")
print("Степень сжатия:", f"{compression_percentage:.2f}%")

#Если символ повторяется (2 и более раз), записываем [количество_повторений, символ]
#Если символы не повторяются, записываем [0, количество_символов, сами_символы]
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def text_to_binary(text, encoding='ascii'):
    binary_str = ''
    for char in text:
        binary_str += format(ord(char), '08b')
    return binary_str

def calculate_parity_bits(data_bits):
    m = len(data_bits)
    for r in range(1, 100):
        if 2**r >= m + r + 1:
            return r
    return 0

def insert_parity_bits(data_bits):
    m = len(data_bits)
    r = calculate_parity_bits(data_bits)
    
    hamming_code = [None] * (m + r)
    
    data_index = 0
    for i in range(1, len(hamming_code)+1):
        if (i & (i - 1)) != 0:  
            if data_index < m:
                hamming_code[i-1] = int(data_bits[data_index])
                data_index += 1
            else:
                hamming_code[i-1] = 0 
    
    for i in range(r):
        pos = 2**i - 1
        xor_result = 0
        for j in range(pos, len(hamming_code), 2**(i+1)):
            for k in range(j, min(j + 2**i, len(hamming_code))):
                if k != pos and hamming_code[k] is not None:
                    xor_result ^= hamming_code[k]
        hamming_code[pos] = xor_result
    
    return ''.join(map(str, hamming_code))

def introduce_errors(hamming_code, error_positions):
    code_list = list(hamming_code)
    for pos in error_positions:
        if 1 <= pos <= len(code_list):
            code_list[pos-1] = '1' if code_list[pos-1] == '0' else '0'
    return ''.join(code_list)

def detect_and_correct_errors(hamming_code):
    code_list = list(map(int, hamming_code))
    error_pos = 0
    r = 0
    while 2**r <= len(code_list):
        r += 1
    
    for i in range(r):
        pos = 2**i
        xor_result = 0
        for j in range(pos-1, len(code_list), 2*pos):
            for k in range(j, min(j + pos, len(code_list))):
                xor_result ^= code_list[k]
        if xor_result:
            error_pos += pos
    
    if error_pos != 0 and error_pos <= len(code_list):
        code_list[error_pos-1] ^= 1
        print(f"Обнаружена и исправлена ошибка в позиции {error_pos}")

    data_bits = []
    for i in range(1, len(code_list)+1):
        if (i & (i - 1)) != 0: 
            data_bits.append(str(code_list[i-1]))
    
    return ''.join(data_bits)

def binary_to_text(binary_str):
    text = ''
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text


input_text = "computer"

binary_code = text_to_binary(input_text)
print(f"Исходный двоичный код: {binary_code}")
print(f"Длина: {len(binary_code)} бит")

block1 = binary_code[:32]
block2 = binary_code[32:]
    
if len(block2) < 32:
    block2 = block2.ljust(32, '0')
    
print("\nБлок 1 (32 бита):", block1)
print("Блок 2 (32 бита):", block2)

hamming_block1 = insert_parity_bits(block1)
hamming_block2 = insert_parity_bits(block2)
    
print("\nБлок 1 с контрольными битами Хемминга:")
print(hamming_block1)
print(f"Длина: {len(hamming_block1)} бит")
  
print("\nБлок 2 с контрольными битами Хемминга:")
print(hamming_block2)
print(f"Длина: {len(hamming_block2)} бит")

corrupted_block1 = introduce_errors(hamming_block1, [3])
corrupted_block2 = introduce_errors(hamming_block2, [25])
    
print("\nБлок 1 с ошибкой в 3 бите:")
print(corrupted_block1)
 
print("\nБлок 2 с ошибкой в 25 бите:")
print(corrupted_block2)

print("\nИсправление ошибок и восстановление данных:")
    
corrected_data1 = detect_and_correct_errors(corrupted_block1)
corrected_data2 = detect_and_correct_errors(corrupted_block2)
    
print("\nИсправленный блок 1 (без контрольных битов):", corrected_data1)
print("Исправленный блок 2 (без контрольных битов):", corrected_data2)
    
restored_binary = corrected_data1[:32] + corrected_data2[:32]
print("\nВосстановленный двоичный код:", restored_binary)
    
restored_text = binary_to_text(restored_binary)
print("\nВосстановленный текст:", restored_text)

print("\nResult:", "успешно" if restored_text == input_text else "ошибка")
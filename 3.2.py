import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def hamming_distance(a, b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))

def min_hamming_distance(codes):
    min_dist = float('inf')
    for i in range(len(codes)):
        for j in range(i+1, len(codes)):
            dist = hamming_distance(codes[i], codes[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def find_error(code, codes, min_dist=2):
    for correct_code in codes.values():
        if hamming_distance(code, correct_code) < min_dist:
            return correct_code
    return None

def correct_error(code, codes, min_dist=3):
    for correct_code in codes.values():
        if hamming_distance(code, correct_code) <= (min_dist - 1) // 2:
            return correct_code
    return None

codes_dist_2 = {
    'а': '00000',
    'б': '00111',
    'в': '11001',
    'г': '11110',
    'д': '01010',
    'е': '01101',
    'ж': '10011',
    'з': '10100'
}

codes_dist_3 = {
    'а': '000000',
    'б': '001111',
    'в': '110011',
    'г': '111100',
    'д': '010101',
    'е': '011010',
    'ж': '100110',
    'з': '101001'
}

print("Минимальное расстояние для кодов с dist >= 2:", min_hamming_distance(list(codes_dist_2.values())))
print("Минимальное расстояние для кодов с dist >= 3:", min_hamming_distance(list(codes_dist_3.values())))

print("\nДемонстрация обнаружения ошибки (dist >= 2):")
test_code = '00001'
print(f"Тестовый код: {test_code}")
correct = find_error(test_code, codes_dist_2)
if correct:
    print(f"Обнаружена ошибка! Ближайший правильный код: {correct}")
else:
    print("Ошибка не обнаружена")

print("\nДемонстрация исправления ошибки (dist >= 3):")
test_code = '000001' 
print(f"Тестовый код: {test_code}")
corrected = correct_error(test_code, codes_dist_3)
if corrected:
    print(f"Исправленный код: {corrected}")
else:
    print("Ошибка не может быть исправлена")
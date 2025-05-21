// M ≤ 2ⁿ / (C(n,0) + C(n,1) + ... + C(n,t)), где t = floor((d-1)/2)

const hammingDistance = (string1, string2) => {
    if (string1.length !== string2.length) {
        throw new Error("Strings must be of equal length")
    }

    let distCounter = 0

    for (let n = 0; n < string1.length; n++) {
        if (string1[n] !== string2[n]) {
            distCounter++
        }
    }

    return distCounter
}

const generateAllSixBitStrings = () => {
    const result = []

    for (let i = 0; i < 64; i++) {
        const binaryString = i.toString(2).padStart(6, "0")
        result.push(binaryString)
    }

    return result
}

const allSixBitStrings = generateAllSixBitStrings()

let arr = []

for (i = 0; i < allSixBitStrings.length; i++) {
    arr = [allSixBitStrings[i]]
    for (j = 0; j < allSixBitStrings.length; j++) {
        if (!arr.some((str) => hammingDistance(allSixBitStrings[j], str) <= 2)) {
            arr.push(allSixBitStrings[j])
        }
    }
    // arr.length >= "абвгдежз".length && console.log(arr)
}

console.log(`
2.

1) Выбранные 4-битные коды:
    а: 0000
    б: 0011
    в: 0101
    г: 0110
    д: 1001
    е: 1010
    ж: 1100
    з: 1111
    Минимальное расстояние между любыми двумя кодами равно 2

2) Ошибка:
    Пусть получено: 0001 => нет совпадения с допустимыми кодами => ошибка обнаружена

3) Выбранные 6-битные коды:
    а: 000000
    б: 000111
    в: 011001
    г: 011110
    д: 101010
    е: 101101
    ж: 110011
    з: 110100
    Минимальное расстояние равно 3

4) Ошибка:
    Пусть получено: 000101 => нет совпадения с допустимыми кодами => ошибка обнаружена

    Вычисляем расстояния до всех кодов:
    а (000000): 000101 и 000000 => 2 (биты 3,5)
    б (000111): 000101 и 000111 => 1 (бит 5)
    в (011001): 000101 и 011001 => 4
    г (011110): 000101 и 011110 => 5
    д (101010): 000101 и 101010 => 4
    е (101101): 000101 и 101101 => 3
    ж (110011): 000101 и 110011 => 5
    з (110100): 000101 и 110100 => 4

    Ближайший код - б (000111) с расстоянием 1.
    Ошибка исправлена, исходная буква: б.

    `)

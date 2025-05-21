const blockOne = "01100011011011110110110101110000"
const blockTwo = "01110101011101000110010101110010"

const getUnderсontrolBitesIndexes = () => {
    let undercontrolBitesForPositions = {}

    for (let i = 0; i < 6; i++) {
        let undercontrolBites = []
        let position = 2 ** i - 1
        for (let j = position; j < 38; j += (position + 1) * 2) {
            for (let k = j; k < j + (position + 1) && k < 38; k++) {
                undercontrolBites.push(k + 1)
            }
        }
        undercontrolBitesForPositions[position + 1] = undercontrolBites
    }

    return undercontrolBitesForPositions
}

const getBlockWithControlBites = (block) => {
    let blockWithPositions = block

    for (let i = 0; i < 6; i++) {
        blockWithPositions = blockWithPositions.slice(0, 2 ** i - 1) + "P" + blockWithPositions.slice(2 ** i - 1, blockWithPositions.length)
    }

    let controlBites = {}
    let blockWithControlBites = blockWithPositions
        .split("")
        .map((bite, index) => {
            if (bite === "P") {
                let undercontrolBites = ""

                for (let j = index; j < blockWithPositions.length; j += (index + 1) * 2) {
                    undercontrolBites += blockWithPositions.slice(j, j + index + 1)
                }

                let contolBitesSum = undercontrolBites
                    .slice(1, undercontrolBites.length)
                    .split("")
                    .map((el) => Number(el))
                    .reduce((acc, curVal) => acc + curVal)

                let controlBite = contolBitesSum % 2 === 0 ? "0" : "1"

                controlBites[index + 1] = controlBite

                return controlBite
            } else {
                return bite
            }
        })
        .join("")

    return { blockWithControlBites, controlBites }
}

const blockOneControlBites = getBlockWithControlBites(blockOne).controlBites
const blockTwoControlBites = getBlockWithControlBites(blockTwo).controlBites

const errorBlockOne = "01101101001101100111101101101010110000"
const errorBlockTwo = "10001110010101111010001110101011110010"

const findErrorBite = (block, wantedControlBites) => {
    let underсontrolBitesIndexes = getUnderсontrolBitesIndexes()

    let givenControlBites = Object.keys(underсontrolBitesIndexes).map((key) => {
        let givenControlBiteSum = underсontrolBitesIndexes[key]
            .map((position) => Number(position) - 1)
            .slice(1)
            .reduce((acc, curValue) => acc + Number(block[curValue]), 0)
        let givenControlBite = givenControlBiteSum % 2 === 0 ? "0" : "1"
        return givenControlBite
    })

    let errorControlBitesPositions = givenControlBites.map((bite, index) => bite !== Object.values(wantedControlBites)[index] && Object.keys(wantedControlBites)[index]).filter((el) => el)

    let errorPosition = errorControlBitesPositions.reduce((acc, curVal) => acc + Number(curVal), 0)

    return { errorPosition, givenControlBites }
}

findErrorBite(errorBlockOne, blockOneControlBites)
findErrorBite(errorBlockTwo, blockTwoControlBites)

console.log(`
1.

1) Исходные данные:
   - Слово "computer" в бинарном виде:
     01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010

2) Исходные блоки для анализа:
   - Первый блок (32 бита): ${blockOne}
   - Второй блок (32 бита): ${blockTwo}

3) Добавление контрольных битов (P) и их расчет:
   - Позиции контрольных битов: 1, 2, 4, 8, 16, 32
   
   Первый блок с контрольными битами (38 бит):
   ${getBlockWithControlBites(blockOne).blockWithControlBites}
   
   Рассчитанные контрольные биты:
   ${JSON.stringify(getBlockWithControlBites(blockOne).controlBites, null, 2)}
   
   Второй блок с контрольными битами (38 бит):
   ${getBlockWithControlBites(blockTwo).blockWithControlBites}
   
   Рассчитанные контрольные биты:
   ${JSON.stringify(getBlockWithControlBites(blockTwo).controlBites, null, 2)}

4) Анализ блоков с ошибками:
   - Ошибочный первый блок (38 бит): ${errorBlockOne}
     * Ошибка введена в 3-й бит (0 → 1)
     * Результат проверки: ${JSON.stringify(findErrorBite(errorBlockOne, blockOneControlBites))}
   
   - Ошибочный второй блок (38 бит): ${errorBlockTwo}
     * Ошибка введена в 25-й бит (0 → 1)
     * Результат проверки: ${JSON.stringify(findErrorBite(errorBlockTwo, blockTwoControlBites))}

Детали работы функций:

Функция getUnderсontrolBitesIndexes():
- Определяет биты данных, контролируемые каждым контрольным битом
${JSON.stringify(getUnderсontrolBitesIndexes(), null, 2)}

Функция findErrorBite():
- Для первого блока:
   * Ожидаемые контрольные биты: ${JSON.stringify(blockOneControlBites)}
   * Фактические контрольные биты: ${JSON.stringify(Object.fromEntries(Object.keys(blockOneControlBites).map((key, index) => [key, findErrorBite(errorBlockOne, blockOneControlBites).givenControlBites[index]])))}
   * Сравнение: ${JSON.stringify(
       Object.fromEntries(
           Object.entries(blockOneControlBites).map(([key, value]) => [key, value === findErrorBite(errorBlockOne, blockOneControlBites).givenControlBites[Object.keys(blockOneControlBites).indexOf(key)] ? "Совпадает" : "Не совпадает"])
       )
   )}

- Для второго блока:
   * Ожидаемые контрольные биты: ${JSON.stringify(blockTwoControlBites)}
   * Фактические контрольные биты: ${JSON.stringify(Object.fromEntries(Object.keys(blockTwoControlBites).map((key, index) => [key, findErrorBite(errorBlockTwo, blockTwoControlBites).givenControlBites[index]])))}
   * Сравнение: ${JSON.stringify(
       Object.fromEntries(
           Object.entries(blockTwoControlBites).map(([key, value]) => [key, value === findErrorBite(errorBlockTwo, blockTwoControlBites).givenControlBites[Object.keys(blockTwoControlBites).indexOf(key)] ? "Совпадает" : "Не совпадает"])
       )
   )}
`)

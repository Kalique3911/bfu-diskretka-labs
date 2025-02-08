let str = "КОМБИНАТОРИКА"
let splitStr = str.split("")
let words = []

for (let a = 0; a < splitStr.length; a++) {
    let accesibleLettersB = [...splitStr]
    accesibleLettersB.splice(a, 1)
    for (let b = 0; b < accesibleLettersB.length; b++) {
        let accesibleLettersC = [...accesibleLettersB]
        accesibleLettersC.splice(b, 1)
        for (let c = 0; c < accesibleLettersC.length; c++) {
            let accesibleLettersD = [...accesibleLettersC]
            accesibleLettersD.splice(c, 1)
            for (let d = 0; d < accesibleLettersD.length; d++) {
                let accesibleLettersE = [...accesibleLettersD]
                accesibleLettersE.splice(d, 1)
                for (let e = 0; e < accesibleLettersE.length; e++) {
                    words.push(splitStr[a] + accesibleLettersB[b] + accesibleLettersC[c] + accesibleLettersD[d] + accesibleLettersE[e])
                }
            }
        }
    }
}

console.log([...new Set(words)].length)

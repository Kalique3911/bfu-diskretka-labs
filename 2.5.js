let length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
let width = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]

let grid = width.map((number) => length.map((letter) => letter + number))
let paths = []

let pathFinder = (coordinate, path = "", end = { square: "22s", length: 21, width: 18 }, count = false) => {
    if (coordinate.square === end.square) {
        paths.push(path + end.square)
        return true
    }

    let lengthEnd = false
    let widthEnd = false
    if (grid[coordinate.width + 1] === undefined || coordinate.width === end.width || count === 1) {
        count = 0
        widthEnd = true
    }
    if (grid[coordinate.width][coordinate.length + 1] === undefined || coordinate.length === end.length) {
        lengthEnd = true
    }

    if (!widthEnd) {
        ;(count === 0 || count) && count++
        pathFinder({ square: grid[coordinate.width + 1][coordinate.length], length: coordinate.length, width: coordinate.width + 1 }, path + coordinate.square, end, count)
    }
    if (!lengthEnd) {
        count = 0
        pathFinder({ square: grid[coordinate.width][coordinate.length + 1], length: coordinate.length + 1, width: coordinate.width }, path + coordinate.square, end, count)
    }
}

pathFinder({ square: "1a", length: 0, width: 0 }, "", { square: "22s", length: 21, width: 18 }, 0)

console.log(paths.length)

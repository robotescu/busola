let grade = 0
input.calibrateCompass()
basic.forever(function () {
    grade = input.compassHeading()
    if (grade >= 315 || grade < 45) {
        basic.showString("N")
    } else if (grade >= 45 && grade < 135) {
        basic.showString("E")
    } else if (grade >= 135 && grade < 225) {
        basic.showString("S")
    } else if (grade >= 225 && grade < 315) {
        basic.showString("W")
    }
})

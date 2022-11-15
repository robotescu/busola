input.calibrate_compass()
grade = 0

def on_forever():
    global grade
    grade = input.compass_heading()
    if grade >= 315 or grade < 45:
        basic.show_string("N")
    elif grade >= 45 and grade < 135:
        basic.show_string("E")
    elif grade >= 135 and grade < 225:
        basic.show_string("S")
    elif grade >= 225 and grade < 315:
        basic.show_string("W")

basic.forever(on_forever)


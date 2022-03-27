def add_up():
    num1 = input("Type a number\n" )
    num2 = input("Type a number\n" )
    try:
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}")
    except:
        print("/n Error: please input only numerical values.")
        add_up()
add_up()
def light_switch():
    light = False
    if light:
        print("Light is on")
        light = False
    else:
        print("Light is off")
        light = True
light_switch()
light_switch()
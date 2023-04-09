import turtle

# turtle.color('purple','yellow')
# turtle.bgcolor('black')

# for i in range(4):
#     turtle.right(90)
#     turtle.forward(100)

# for i in range(25):
#     turtle.right(15)
#     turtle.forward(10)

# если условие = правда
#     действие

# num1 = int(input('введите число'))
# num2 = int(input('введите число'))



# if num1 != num2:
#     print(f'{num1+num2} не равно {num2}')
# elif: type(num1) ==t
#     print(f'{num1} не равно {num2}')
while True:
    s = input('введите фигуру')

    if s == "squere":
        for i in range(4):
                if len(s) > 1:
                    turtle.right(int(s[3]))
                if len(s) > 2:
                    turtle.forward(int(s[2]))
                else:
                    turtle.right(int(s[1]))
                    turtle.forward(100)
        else:
            turtle.right(90)
        turtle.forward(100)
    elif s[0] =="circle":
        for i in range(25):
             turtle.right(15)
             turtle.forward(10)
    else:
        break
     
        
        














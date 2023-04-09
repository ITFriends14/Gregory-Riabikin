import turtle

# for i in range(10)
# for i in range(list):

# run = 10
# while run:
#   run -= 10

turtle.begin_fill()

turtle.color('red' ,'blue')
turtle.bgcolor('black')
#turtle.right(90)
#turtle.forward(100)
               
#turtle.right(90)
#turtle.forward(100)

#turtle.right(90)
#turtle.forward(100)

#turtle.right(90)
#turtle.forward(100)


#num = 100
#n_color = 0

#for i in range(400):
#    turtle.color(colors[n_color])
#    turtle.right(30)
#    turtle.forward(num - i)
#    if n_color != len(colors) - 1:
#        n_color += 1
#    else:
#        n_color = 0


colors = ['red', 'blue', 'green', ' yellow' , 'orange']
num = 100
n_color = 0

for i in range(100):
    turtle.color(colors[n_color])
    turtle.circle(num)
    turtle.forward(num - i)
    if n_color != len(colors) - 1:
        n_color += 1
    else:
        n_color = 0







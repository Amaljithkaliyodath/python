import turtle as tur
 

tur.bgcolor('black')
tur.pensize(4)
tur.speed(10)

for i in range(5):

      
    for color in ('green', 'yellow', 'red',
                  'pink', 'blue', 'orange',
                  'cyan','black'):
        tur.color(color)
         

        tur.circle(100)
         

        tur.right(10)
    
    

    tur.hideturtle()
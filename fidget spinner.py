## fidget spinner

form turtle import *

rev = {'turn': 0}
def spinner();
    clear()
    angle = rev['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    rirght(120)
    forward(100)
    
    dot(120,'blue')
    back(100)
    right(120)
    forward(100)
    
    dot(120,'green')
    back(100)
    right(120)
    update()
    
def animate()
    if rev['turn']>0:
        rev['turn']-=1
        
    spinner()
    ontimer(animate, 20)
   
def flick()
    rev['turn']+=10
    
setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()
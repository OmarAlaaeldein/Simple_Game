import turtle
import random
import tkinter

class singleton:
    def __new__(cls, *args, **kwargs):
        """
           Generate the windows singleton object to prevent creation and instantiation of more than one instance
        """
        if not hasattr(cls,'instance'):
            cls.instance=super(singleton,cls).__new__(cls)
        return cls.instance
class create(singleton):
    def __init__(self,title='Race of Turtles',page_color='forestgreen'):
        """
           Generate the windows singleton object and configure the title and the page color of the window
           :param title: sets the title for the windows to be created, default is "Race of Turtles"
           :param page_color: sets the color of the window to be created, default page_color is "forestgreen"
           :return: None
        """
        # create a variable window with global scope to access it later and terminate it whenever
        window = turtle.Screen() # create a singleton object called window to be displayed
        window.bgcolor('forest green')

    def exit(self):
        """
           used mainly for exiting the object windows on a click prompt, takes no arguments
        """
        window.exitonclick() # exit the window in a click prompt, takes no argument



class simple_shapes:
    def square(self,size,x=None,y=None):
        """
        draws a square with given size
        :param x(int): horizontal coordinate in object window, takes integer values as pixel displacement from origin point, default: None
        :param y(int): vertical coordinate in object window, takes integer values as pixel displacement from origin point, default: None
        :param size(int): sets the edge length for the drawn polygon
        """
        try:
            turtle.setpos(x,y) # move the turtle object to position x,y in windows object, default x,y is 0,0
        except:
            pass
        turtle.color('black')  #Return the current pencolor and the current fillcolor as a pair of color specification
        # strings or tuples as returned by pencolor() and fillcolor() if a single argument exist, set both colors to that argument
        turtle.pendown()  # Pull the pen down – drawing when moving
        turtle.begin_fill()  # To be called just before drawing a shape to be filled.
        for i in range(4):  # draws a square with edge length equal to :param size
            turtle.forward(size)
            turtle.right(90)
        turtle.end_fill() # fill all the drawn shape with fillcolor() which is purple
    def square2(self,f,size,x=None,y=None):
        """
        draws a square with given size
        :param x(int): horizontal coordinate in object window, takes integer values as pixel displacement from origin point, default: None
        :param y(int): vertical coordinate in object window, takes integer values as pixel displacement from origin point, default: None
        :param size(int): sets the edge length for the drawn polygon
        """
        try:
            f.setpos(x,y) # move the turtle object to position x,y in windows object, default x,y is 0,0
        except:
            pass
        f.color('black')  #Return the current pencolor and the current fillcolor as a pair of color specification
        # strings or tuples as returned by pencolor() and fillcolor() if a single argument exist, set both colors to that argument
        f.pendown()  # Pull the pen down – drawing when moving
        f.begin_fill()  # To be called just before drawing a shape to be filled.
        for i in range(4):  # draws a square with edge length equal to :param size
            f.forward(size)
            f.right(90)
        f.end_fill() # fill all the drawn shape with fillcolor() which is purple
    def rectangle(self,length,width,x=0,y=0):
        """
            draws a rectangle with given size
            :param x(int): horizontal coordinate in object window, takes integer values as pixel displacement from origin point
            :param y(int): vertical coordinate in object window, takes integer values as pixel displacement from origin point
            :param length(int): sets the rectangle length
            :param width(int): sets the rectangle width
        """
        try:
            turtle.setpos(x,y) # move the turtle object to position x,y in windows object, default x,y is 0,0
        except:
            pass
        turtle.color('purple')
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)
        turtle.end_fill()
    def circle(self):
        pass


class finish_line(simple_shapes):               # class to make a finish line


    def __init__(self,x=296,y=-100,size=13):
        """
        Init function to make the finish  line
        :param x: the x value for the finish line
        :param y: the y value for the finish line
        :param size: the size of the finish line
        """
        m=turtle.Turtle()
        n=turtle.Turtle()
        o=turtle.Turtle()
        for i in [m,n,o]:
            i.penup()
            i.speed(0)
            i.hideturtle()

        for i in range(size):                   # making the first column of squares in the finish line
            turtle.penup()                      # taking up the pen so it doesnt write
            m.penup()                      # taking up the pen so it doesnt write
            n.penup()                      # taking up the pen so it doesnt write
            o.penup()                      # taking up the pen so it doesnt write
            super().square2(m,10,x, y + 20 * i)    # drawing squares in the position specified
            y-=10
            super().square2(n,10, x + 10, y + 20 * i)
            y+=10
            super().square2(o,10, x + 20, y + 20 * i)
        m.forward(10)
        m.left(90)
        super().square2(m,10)

class Dirt:                                     # makes the dirt at the bottom of the screen
    def __init__(self):
        turtle.penup()
        turtle.setpos(-480, -396)
        turtle.pendown()
        turtle.color('dark olive green')
        turtle.begin_fill()
        turtle.forward(470 * 2 + 20)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(470 * 2 + 20)
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()

class words:        # class to fill the words necessary for the game
    def write_title(self,x=-200,y=300,title='Ninja Turtle Race',default_font=('Arial', 40, 'bold')):
        """
        Method responsible for writing the title in the specified position
        :param x:   The x axis value
        :param y: The y axis value
        :param title: The title to be displayed
        :param default_font: Tuple that has the font and size amd formatting
        :return: None
        """
        turtle.penup()                              # removes the pin before going to the location of the title
        turtle.speed(0)                             # makes the speed the fastest possible
        turtle.setpos(x, y)                         # sets the position of the turtle that will write in the specified position
        turtle.write(title, font=default_font)      # function that writes the title with the specified formatting

    def description(self,x=-155,y=260,description='Wait and Choose(Click) the turtle you bet will win',default_font=('Arial', 12, 'italic')):
        """
        Method that writes the desciption of the game which tells how to play the game
        :param x: The x axis value
        :param y: The y axis value
        :param description: The sentences needed for the description
        :param default_font: The formatting for the description
        :return: None
        """
        turtle.setpos(x, y)                             # moves the turtle to the position of the descrption will be written at
        turtle.write(description, font=default_font)    # function that writes the desciption
        turtle.hideturtle()                             # this is to hide the turtle after writing the words to move it freely after that

class Racers:
    def __init__(self,x0=-350,y0=100):
        """
        Init method that intiates the colors of the players and sets them to type turtles and sets the shape for them as turtles
        :param x0: The x axis value
        :param y0: The y axis value
        """
        colors = ['blue', 'red', 'purple', 'orange']                                         # the colors for the players
        a, b, c, d = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()     # defining the type of the players to a turtle

        self.a, self.b, self.c, self.d = a, b, c, d                                         # making them attributes for the class
        objs = [a, b, c, d]
        self.objs = objs                                                                    # the list of available players
        decrementer = 0
        for i in range(len(objs)):                                                          # iterating over the players to position them where they will start the race
            objs[i].penup()                                                                 # removing the pen before moving the turtle to its position
            objs[i].shape('turtle')                                                         # choosing the shape of the player to a turtle
            objs[i].color(colors[i])                                                        # setting the color based on the list of colors above
            objs[i].setpos(x0, y0 + decrementer)                                            # sets the position of the turtles
            decrementer -= 50                                                               # decrementing to the position of the next turtle
            objs[i].pendown()                                                               # pen down again to leave a trail after the racer

    def move(self,a,b,c,d,col):
        """
        Method that is responsible for the movement of the racers
        :param a: the first racer
        :param b: the second racer
        :param c: the third racer
        :param d: the forth racer
        :param col: it takes in the color of the racer that will be chosen by the user
        :return: None
        """
        while True:                                     # a loop for the racers to keep racing randomly untill reaching the finish line
            inp=col
            a.forward(random.randint(2,5))              # randominzing the movement speed of the first player
            b.forward(random.randint(2,5))              # randominzing the movement speed of the second player
            c.forward(random.randint(2,5))              # randominzing the movement speed of the third player
            d.forward(random.randint(2,5))              # randominzing the movement speed of the forth player

            # conditions to check if the racer had reached the finish line
            if a.position()>=(269+30+25,100):           # stop the race if a wins
                val='blue'
                break
            if b.position()>=(269 + 30+25, 50):         # stop the race if b wins
                val='red'
                break
            if c.position()>=(269 + 30+25, 0):          # stop the race if c wins
                val='purple'
                break
            if d.position()>=(269 + 30+25, -50):        # stop the race if d wins
                val='orange'
                break

        turtle.penup()

        # conditions to see if the player have chosen the turtle correctly or not
        if val == 'blue':
            turtle.color('blue')
            turtle.setpos(-140, 200)  # sets the position of the turtle in the middle to write the state of the game in the end
            turtle.write('Leonardo Wins', font=('Arial', 30, 'bold'))
        elif val == 'red':
            turtle.color('red')
            turtle.setpos(-120, 200)  # sets the position of the turtle in the middle to write the state of the game in the end
            turtle.write('Raphael Wins', font=('Arial', 30, 'bold'))
        elif val == 'purple':
            turtle.color('purple')
            turtle.setpos(-135, 200)  # sets the position of the turtle in the middle to write the state of the game in the end
            turtle.write('Donatello Wins', font=('Arial', 30, 'bold'))
        elif val == 'orange':
            turtle.color('orange')
            turtle.setpos(-160, 200)  # sets the position of the turtle in the middle to write the state of the game in the end
            turtle.write('Michelangelo Wins', font=('Arial', 30, 'bold'))

        # Writing the status of the game
        if val==inp:
            turtle.setpos(-65, 0)
            turtle.color('black')
            turtle.write('Nice', font=('Arial', 50, 'bold'))
        else:
            turtle.setpos(-135, 0)
            turtle.color('black')
            turtle.write('You LOSE', font=('Arial', 50, 'bold'))
    def click(self,x,y):
        """
        Method that takes the position of the turtle chosen to play
        :param x: The x axis value
        :param y: The y axis value
        :return: None
        """
        # the 4 racers
        a=self.a
        b=self.b
        c=self.c
        d=self.d

        # waits for the click on the turtle
        turtle.onscreenclick(None)

        # conditions to determine which turtle was chosen
        if x < -350+50 and x>-350-50 and y>100-10 and y<100+10:
            inp='blue'
            self.move(a, b, c, d,inp)
        elif x < -350+50 and x>-350-50 and y>50-10 and y<50+10:
            inp = 'red'
            self.move(a, b, c, d,inp)
        elif x < -350+50 and x>-350-50 and y>0-10 and y<0+10:
            inp='purple'
            self.move(a, b, c, d,inp)
        elif x < -350+50 and x>-350-50 and y>-50-10 and y<-50+10:
            inp = 'orange'
            self.move(a, b, c, d,inp)
        else:
            inp="u didn't choose correct"
            self.move(a, b, c, d,inp)


    def play(self):
        """
        Starts the race after the click
        :return: None
        """
        turtle.onscreenclick(self.click,1)          # takes the lick from the user
        turtle.listen()                             # makes the screen listen for input
        turtle.mainloop()

def main():
    """
    Function main to make the game and write the information in it
    :return: None
    """
    global finish
    global dirt
    create()            # creating game instance
    info=words()             # writing the words necessary
    info.write_title()       # title method
    info.description()       # description method
    dirt=Dirt()              # making the dirt in its position
    finish=finish_line()     # creating the finish line

    racers=Racers()          # creates the racers
    racers.play()            # takes the input from the user and starts the game

    del dirt                 # deleting the game instance
    del finish               # deleting the game instance


from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
root=Tk()
root.title('Ninja Turtles Game')

canvas = Canvas(root, width = 450, height = 650)
canvas.configure(bg='white')
canvas.pack()

image = Image.open('2.png')
# The (450, 350) is (height, width)
image = image.resize((400, 400), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(image = my_img)
img = ImageTk.PhotoImage(image)
canvas.create_image(450//2, (650//2)-100, anchor=CENTER, image=img)
# canvas.


def close():
    """
    Deletes the game for the ability to start another
    Exits the game and launcher
    :return:
    """
    # window.bye()

    sys.exit()          # exits the launcher

try:    # making the buttons for the game
    b =Button(root, text='Start the game', bg='light green',command=main,height=2,width=15)             # the main button that runs the game
    myFont = font.Font(family='Comic Sans MS', size=15+4, weight='bold')
    b['font']=myFont
    # b.place(x=300,y=500,anchor)
    b.place(relx=0.5, rely=0.8, anchor=CENTER)

    c=Button(root,text='Close the game', bg='coral3',command=close)                                     # the button that closes the launcher
    myFont = font.Font(family='Comic Sans MS', size=13+4, weight='bold')
    c['font']=myFont
    c.place(relx=0.5, rely=0.93, anchor=CENTER)
except:
    print('weird')

root.mainloop()






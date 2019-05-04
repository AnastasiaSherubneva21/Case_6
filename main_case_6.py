from tkinter import *
import time


class Cell:
    def __init__(self, black_points, x=10, y=10, i=10, j=10):
        self.isAlive = False
        self.nextStatus = None
        self.pos_screen = (x, y)
        self.pos_matrix = (i, j)
        self.black_points = black_points
        self.open()

    def redraw(self, event):
        jj = int((event.x - 10) / self.pos_matrix[0])  # где 10 - это размер клетки
        ii = int((event.y - 10) / self.pos_matrix[1])

        pos = (ii, jj)

        if pos in self.black_points:
            self.canvas.itemconfig(self.grid[pos][0], fill='white')
            self.black_points.remove(pos)
        else:
            self.canvas.itemconfig(self.grid[pos][0], fill='black')
            self.black_points.append(pos)

    def dictionary_play(self):
        d = {}
        for i in range(0, 40):
            for j in range(0, 40):
                pos = (i, j)
                set_pos = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1),
                           (i + 1, j - 1), (i + 1, j + 1)}
                if pos in self.black_points:
                    if 2 <= len(set_pos & set(self.black_points)) <= 3:
                        d[pos] = 1
                    else:
                        d[pos] = 0
                else:
                    if len(set_pos & set(self.black_points)) == 3:
                        d[pos] = 1
                    else:
                        d[pos] = 0
        return d

    def print_dict(self, d):
        self.black_points = []
        for i in d:
            if d[i] == 1:
                self.canvas.itemconfig(self.grid[i][0], fill='black')
                self.black_points.append(i)
            else:
                self.canvas.itemconfig(self.grid[i][0], fill='white')



    def play(self, event):
        set_list = set()
        len_last = -1
        len_now = -2
        while len(self.black_points) != 0 and len_last != len_now:
            d = self.dictionary_play()
            self.print_dict(d)
            len_last = len(set_list)
            bp_tuple = tuple(self.black_points)
            set_list.add(bp_tuple)
            len_now = len(set_list)
            time.sleep(1)
        print('GAME OVER')




    def open(self):
        self.root = Tk()
        self.life = 'black'
        self.death = 'white'
        self.grid = {}
        self.root.title("Game of Life")
        self.frame = Frame(self.root, width=400, height=400)  # создаём окно
        self.frame.pack()
        self.butstart = Button(self.root, bg='gray', text='Start', font='arial 15')
        self.butstart.pack()
        self.butstart.bind('<Button-1>', self.play)
        self.canvas = Canvas(self.frame, width=400, height=400)  # создаёт холст на котором можно рисовать
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.redraw)
        self.canvas.bind('<ButtonPress-3>', self.redraw)


    def __str__(self):
        return str(self.isAlive)

    def __repr__(self):
        return str(self.isAlive)

    def switchStatus(self):
        self.isAlive = not self.isAlive

    def create_grid(self):
        """This function creates the board on which the game will take place"""
        x = 10
        y = 10

        for i in range(50):
            for j in range(50):
                pos = (i, j)
                rect = self.canvas.create_rectangle(x, y, x+10, y+10, fill="white")
                # state=HIDDEN, tags=('hid','0'))

                self.grid[pos] = [rect, False]

                x += 10
            x = 10
            y += 10


black_points = []
p = Cell(black_points)
p.create_grid()
p.root.mainloop()

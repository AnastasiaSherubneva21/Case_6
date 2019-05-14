from tkinter import *
import time

class Cell:
    def __init__(self, black_points, s, x=10, y=10, i=10, j=10, time=0):
        self.isAlive = False
        self.nextStatus = None
        self.pos_screen = (x, y)
        self.pos_matrix = (i, j)
        self.black_points = black_points
        self.open()
        self.time = time
        self.s = s


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
        for i in range(self.s):
            for j in range(self.s):
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
        return_s_t = 1
        self.time = 1
        set_list = set()
        len_last = -1
        len_now = -2
        while len(self.black_points) != 0 and len_last != len_now and return_s_t == 1:
            d = self.dictionary_play()
            self.print_dict(d)
            len_last = len(set_list)
            bp_tuple = tuple(self.black_points)
            set_list.add(bp_tuple)
            len_now = len(set_list)
            self.root.update()
            time.sleep(1)
            return_s_t = self.return_self_time()

        lst_gameover = [(15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 15), (15, 16), (15, 17), (15, 18),
                        (15, 19), (15, 21), (15, 25), (15, 27), (15, 28), (15, 29), (15, 30), (15, 31), (16, 9),
                        (16, 13), (16, 15), (16, 19), (16, 21), (16, 22), (16, 24), (16, 25), (16, 27), (17, 9),
                        (17, 12), (17, 13), (17, 15), (17, 19), (17, 21), (17, 23), (17, 25), (17, 27), (17, 28),
                        (17, 29), (17, 30), (17, 31), (18, 9), (18, 15), (18, 16), (18, 17), (18, 18), (18, 19),
                        (18, 21), (18, 25), (18, 27), (19, 9), (19, 10), (19, 11), (19, 12), (19, 13), (19, 15),
                        (19, 19), (19, 21), (19, 25), (19, 27), (19, 28), (19, 29), (19, 30), (19, 31), (21, 9),
                        (21, 10), (21, 11), (21, 12), (21, 13), (21, 15), (21, 19), (21, 21), (21, 22), (21, 23),
                        (21, 24), (21, 25), (21, 27), (21, 28), (21, 29), (21, 30), (21, 31), (22, 9), (22, 13),
                        (22, 15), (22, 19), (22, 21), (22, 27), (22, 31), (23, 9), (23, 13), (23, 15), (23, 19),
                        (23, 21), (23, 22), (23, 23), (23, 24), (23, 25), (23, 27), (23, 28), (23, 29), (23, 30),
                        (23, 31), (24, 9), (24, 13), (24, 16), (24, 18), (24, 21), (24, 27), (24, 28), (25, 9),
                        (25, 10), (25, 11), (25, 12), (25, 13), (25, 17), (25, 21), (25, 22), (25, 23), (25, 24),
                        (25, 25), (25, 27), (25, 29), (25, 30), (25, 31)]
        if return_s_t != 2:
            for i in self.black_points:
                try:
                    self.canvas.itemconfig(self.grid[i][0], fill='white')
                except:
                    pass
            try:
                for i in lst_gameover:
                    self.canvas.itemconfig(self.grid[i][0], fill='black')
            except:
                pass


    def stop(self, event):
        self.time = 2


    def return_self_time(self):
        return self.time

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
        self.butstop = Button(self.root, bg='gray', text='Stop', font='arial 15')
        self.butstop.pack()
        self.butstop.bind('<ButtonPress-1>', self.stop)


    def __str__(self):
        return str(self.isAlive)


    def __repr__(self):
        return str(self.isAlive)


    def switchStatus(self):
        self.isAlive = not self.isAlive


    def create_grid(self, s):
        """This function creates the board on which the game will take place"""
        x = 10
        y = 10

        for i in range(s):
            for j in range(s):
                pos = (i, j)
                rect = self.canvas.create_rectangle(x, y, x+10, y+10, fill="white")
                self.grid[pos] = [rect, False]
                x += 10
            x = 10
            y += 10


s = int(input('Введите размер игровой доски: '))
black_points = []
p = Cell(black_points, s)
p.create_grid(s)
p.root.mainloop()
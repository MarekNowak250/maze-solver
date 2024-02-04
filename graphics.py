from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_colour = "black"):
        line.draw(self.__canvas, fill_colour)
        

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        
    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_colour, width=2
        )
        canvas.pack(fill=BOTH, expand=1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from graphics import Line, Point

class Cell:
    def __init__(self, top_left, bottom_right, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._win = win


    def draw(self):
        if self._win is None:
            return
        
        top_color = "black" if self.has_top_wall else "white"
        self._win.draw_line(Line(Point(self._top_left.x, self._top_left.y), Point(self._bottom_right.x, self._top_left.y)), top_color)
        
        bottom_color  = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(Line(Point(self._top_left.x, self._bottom_right.y), Point(self._bottom_right.x, self._bottom_right.y)), bottom_color)
        
        left_color = "black" if self.has_left_wall else "white"
        self._win.draw_line(Line(Point(self._top_left.x, self._top_left.y), Point(self._top_left.x, self._bottom_right.y)), left_color)
        
        right_color = "black" if self.has_right_wall else "white"
        self._win.draw_line(Line(Point(self._bottom_right.x, self._top_left.y), Point(self._bottom_right.x, self._bottom_right.y)), right_color)


    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        mid_x = (self._top_left.x +self._bottom_right.x) // 2
        mid_y = (self._top_left.y +self._bottom_right.y) // 2 
        to_cell_mid_x = (to_cell._top_left.x + to_cell._bottom_right.x) // 2
        to_cell_mid_y = (to_cell._top_left.y + to_cell._bottom_right.y) // 2 
        
        line = Line(Point(mid_x, mid_y), Point(to_cell_mid_x, to_cell_mid_y))
        if undo:
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(line, "gray")

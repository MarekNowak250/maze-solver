import time
from cell import Cell
from graphics import Point
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()


    def _create_cells(self):
        for col_index in range(self._num_cols):
            col_cells = []
            for row_index in range(self._num_rows):
                cell = self.create_cell(col_index, row_index)
                col_cells.append(cell)                
                self._draw_cell(cell)
            self._cells.append(col_cells)

    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self._num_cols -1][self._num_rows -1]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        self._draw_cell(entrance)
        self._draw_cell(exit)
    

    def _break_walls_r(self, i, j):
        curr_item = self._cells[i][j]
        curr_item.visited = True
        
        while True:
            to_visit = []

            if i -1 >= 0:
                left = self._cells[i-1][j]
                if not left.visited:
                    to_visit.append((i-1, j, 'left'))
            if i +1 < self._num_cols:
                right = self._cells[i+1][j]
                if not right.visited:
                    to_visit.append((i+1, j, 'right'))
            if j-1 >= 0:
                top = self._cells[i][j-1]
                if not top.visited:
                    to_visit.append((i, j-1, 'top'))
            if j+1 < self._num_rows:
                bottom = self._cells[i][j+1]
                if not bottom.visited:
                    to_visit.append((i, j+1, 'bottom'))

            if len(to_visit) == 0:
                self._draw_cell(curr_item)
                return

            visit_index = random.randint(0, len(to_visit)-1)
            to_visit_item = to_visit[visit_index]
            to_visit_cell = self._cells[to_visit_item[0]][to_visit_item[1]]
            direction = to_visit_item[2]

            if direction == 'top':
                to_visit_cell.has_bottom_wall = False
                curr_item.has_top_wall = False
            elif direction == 'bottom':
                to_visit_cell.has_top_wall = False
                curr_item.has_bottom_wall = False
            elif direction == 'left':
                to_visit_cell.has_right_wall = False
                curr_item.has_left_wall = False
            else:
                to_visit_cell.has_left_wall = False
                curr_item.has_right_wall = False

            # self._draw_cell(curr_item)
            # self._draw_cell(to_visit_cell)

            self._break_walls_r(to_visit_item[0], to_visit_item[1])

    
    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):   
        self._animate(.25)

        visiting_cell = self._cells[i][j]
        visiting_cell.visited = True

        if i== self._num_cols-1 and j == self._num_rows -1:
            return True
        
        for direction in ['right', 'left', 'bottom', 'top']:
            curr_cell = None
            coords = None

            if direction == 'top' and  j-1 >= 0:
                curr_cell = self._cells[i][j-1]
                coords = (i, j-1)
                if curr_cell.visited or curr_cell.has_bottom_wall:
                    continue
            elif direction == 'left' and  i-1 >= 0:
                curr_cell = self._cells[i-1][j]
                coords = [i-1, j]
                if curr_cell.visited or curr_cell.has_right_wall:
                    continue
            elif direction == 'bottom' and  j+1 < self._num_rows:
                curr_cell = self._cells[i][j+1]
                coords = (i, j+1)
                if curr_cell.visited or curr_cell.has_top_wall:
                    continue
            elif direction == 'right' and i +1 < self._num_cols:
                curr_cell = self._cells[i+1][j]
                coords = (i+1, j)
                if curr_cell.visited or curr_cell.has_left_wall:
                    continue
            else:
                continue  
            
            visiting_cell.draw_move(curr_cell)
            if self._solve_r(coords[0], coords[1]):
                return True
            visiting_cell.draw_move(curr_cell, undo=True)
        
        return False
            

    def _reset_cells_visited(self):
        for col_index in range(self._num_cols):
            for row_index in range(self._num_rows):
                self._cells[col_index][row_index].visited = False


    def create_cell(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        cell = Cell(Point(x1, y1), Point(x2, y2), self._win)
        return cell


    def _draw_cell(self, cell, sleep = 0.05):
        cell.draw()
        self._animate(sleep)


    def _animate(self, sleep = .05):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(sleep)

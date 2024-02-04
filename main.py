from graphics import Window 
from maze import Maze

def main():
    win = Window(800, 600)
    # win.draw_line(Line(Point(10, 20), Point(30, 40)), "black")
    # win.draw_line(Line(Point(100, 200), Point(400, 500)), "red")
    # cell = Cell(win, Point(10, 20), Point(80, 80))
    # cell2 = Cell(win, Point(90, 90), Point(140, 140))
    # win.draw_cell(cell)
    # win.draw_cell(cell2)
    # cell.draw_move(cell2)

    # cell3 = Cell(win, Point(220, 20), Point(320, 40))
    # cell4 = Cell(win, Point(240, 50), Point(340, 90))
    # win.draw_cell(cell3)
    # win.draw_cell(cell4)
    # cell3.draw_move(cell4, True)

    maze = Maze(10, 10, num_rows=6, num_cols=8, cell_size_x=80, cell_size_y=60, win=win)

    maze.solve()
    win.wait_for_close()

main()

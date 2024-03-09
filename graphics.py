#this holds all graphical classes for the solver

from tkinter import *

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("Sudoku Solver")
        self.__canvas = Canvas(self.__root, bg="white", width = width, height = height)
        self.__can.pack(fill = BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.__running = False

    def wait_to_close(self):
        self.__running = True
        while self.__running:
            self.redraw() #TODO this isn't really an animation, might want to alter this bit accordingly?  Need more research into tkinter
        print("App closed")

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
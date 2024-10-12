from tkinter import Tk
from Sudoku_gui import Gui
from stuff import resource_path





window = Tk()
window.geometry("1100x650")
window.title("Sudoku Game")
icon_path = resource_path("logo.ico")
window.iconbitmap(icon_path)




sudoku_gui = Gui(window)






window.mainloop()
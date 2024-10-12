# import tkinter as tk
# from tkinter import messagebox
#
# class SudokuGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Sudoku")
#
#         # Tablero original y solución
#         self.original_board = [
#             [5, 3, 0, 0, 7, 0, 0, 0, 0],
#             [6, 0, 0, 1, 9, 5, 0, 0, 0],
#             [0, 9, 8, 0, 0, 0, 0, 6, 0],
#             [8, 0, 0, 0, 6, 0, 0, 0, 3],
#             [4, 0, 0, 8, 0, 3, 0, 0, 1],
#             [7, 0, 0, 0, 2, 0, 0, 0, 6],
#             [0, 6, 0, 0, 0, 0, 2, 8, 0],
#             [0, 0, 0, 4, 1, 9, 0, 0, 5],
#             [0, 0, 0, 0, 8, 0, 0, 7, 9]
#         ]
#
#         self.solution_board = [
#             [5, 3, 4, 6, 7, 8, 9, 1, 2],
#             [6, 7, 2, 1, 9, 5, 3, 4, 8],
#             [1, 9, 8, 3, 4, 2, 5, 6, 7],
#             [8, 5, 9, 7, 6, 1, 4, 2, 3],
#             [4, 2, 6, 8, 5, 3, 7, 9, 1],
#             [7, 1, 3, 9, 2, 4, 8, 5, 6],
#             [9, 6, 1, 5, 3, 7, 2, 8, 4],
#             [2, 8, 7, 4, 1, 9, 6, 3, 5],
#             [3, 4, 5, 2, 8, 6, 1, 7, 9]
#         ]
#
#         self.entries = [[None]*9 for _ in range(9)]
#         self.create_board()
#
#     def create_board(self):
#         for i in range(9):
#             for j in range(9):
#                 if self.original_board[i][j] == 0:
#                     self.entries[i][j] = tk.Entry(self.master, width=3, font=('Arial', 20), justify='center')
#                     self.entries[i][j].grid(row=i, column=j)
#                 else:
#                     self.entries[i][j] = tk.Label(self.master, text=str(self.original_board[i][j]), width=3, font=('Arial', 20), bg='lightgray', relief='raised')
#                     self.entries[i][j].grid(row=i, column=j)
#
#         check_button = tk.Button(self.master, text="Check", command=self.check_solution)
#         check_button.grid(row=9, column=0, columnspan=4)
#
#         reset_button = tk.Button(self.master, text="Reset", command=self.reset_board)
#         reset_button.grid(row=9, column=5, columnspan=4)
#
#     def check_solution(self):
#         correct = True
#         for i in range(9):
#             for j in range(9):
#                 widget = self.entries[i][j]
#                 if isinstance(widget, tk.Entry):
#                     value = widget.get()
#                     if value.isdigit() and value != "0":
#                         value = int(value)
#                     else:
#                         # Handle invalid input (optional)
#                         continue
#                     if value != self.solution_board[i][j]:
#                         widget.config(bg='red')
#                         correct = False
#                     else:
#                         widget.config(bg='lightgreen')
#         if correct:
#             messagebox.showinfo("¡Felicidades!", "Has completado el Sudoku correctamente.")
#
#     def reset_board(self):
#         for i in range(9):
#             for j in range(9):
#                 widget = self.entries[i][j]
#                 if isinstance(widget, tk.Entry):
#                     widget.delete(0, tk.END)
#                 else:
#                     widget.config(bg='lightgray')
#
# def main():
#     root = tk.Tk()
#     sudoku_gui = SudokuGUI(root)
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()



d = [1,2,3]
c = [1,2,3]

f = d+c
print(f)








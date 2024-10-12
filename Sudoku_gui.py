from os import write
from tkinter import Toplevel, PhotoImage, Canvas, Button, Label, Entry


from stuff import resource_path
from sounds import Sounds



class Gui:
    def __init__(self, window):

        self.window2 = None
        self.background = None
        self.window2_is_active = False

        self.nivel = self.get_niveles()
        self.boton = 0
        self.sounds = Sounds()
        self.window = window
        self.entry = None





        self.canva = Canvas(window, width=1100, height=650)

        self.background_image = PhotoImage(file=resource_path("background_image.png"))
        self.canva.create_image(0, 0, anchor="nw", image=self.background_image)
        self.canva.create_text(550, 90, text="Sudoku Game", font="Algerian 100 bold")

        self.canva.pack()

        self.background_frezzer = PhotoImage(file=resource_path("Bottones/frezzer.png"))
        self.canva.create_text(130, 220, text="Facil", font=("Bradley Hand ITC", "30", "bold"))
        self.facil = Button(window, width=220, height=380, anchor="nw", image=self.background_frezzer, highlightthickness=0,
                       font="Arial 120 bold", text="", compound="center",command=self.nivel_facil)
        self.facil.place(x=20, y=250)

        self.background_androides = PhotoImage(file=resource_path("Bottones/cell.png"))
        self.canva.create_text(420, 220, text="Medio", font=("Bradley Hand ITC", "30", "bold"))
        self.medio = Button(window, width=220, height=380, anchor="nw", image=self.background_androides, highlightthickness=0,
                       font="Arial 140 bold", compound="center",text="🔒", fg="#29103F",command=self.nivel_medio)
        self.medio.place(x=300, y=250)

        self.background_cell = PhotoImage(file=resource_path("Bottones/buu.png"))
        self.canva.create_text(700, 220, text="Dificil", font=("Bradley Hand ITC", "30", "bold"))
        self.dificil = Button(window, width=220, height=380, anchor="nw", image=self.background_cell, highlightthickness=0,
                         font="Arial 120 bold", text="🔒", compound="center", fg="#29103F", command=self.nivel_dificil)
        self.dificil.place(x=580, y=250)

        self.background_buu = PhotoImage(file=resource_path("Bottones/jiren.png"))
        self.canva.create_text(975, 220, text="Imposible", font=("Bradley Hand ITC", "30", "bold"))
        self.imposible = Button(window, width=220, height=380, anchor="nw", image=self.background_buu, highlightthickness=0,
                           font="Arial 120 bold", text="🔒", compound="center", fg="#29103F",command=self.nivel_imposible)
        self.imposible.place(x=860, y=250)

        self.verificar_nivel()

    def get_niveles(self):
        data = []
        with open(resource_path("nivel.txt")) as file:
            content = file.read()
            for i in range(1,len(content)):
                data.append(content[i])
        return data

    def modificar(self,index,value):
        print("modificar",index, value)
        temp = [self.checar_nivel()] + self.get_niveles()
        temp[int(index)] = str(value)

        with open(resource_path("nivel.txt"),"w") as file:
            for char in temp:
                file.write(str(char))






    def verificar_nivel(self):
        nivel = self.checar_nivel()

        if nivel >= 1:
            self.medio.config(text="")

        if nivel >=2:
            self.dificil.config(text="")

        if nivel >= 3:
            self.imposible.config(text="")
    def checar_nivel(self):
        with open(resource_path("nivel.txt"), "r") as file:
            text = file.read()
            return int(text[0])


    def nivel_facil(self):

        data = [
            [0,0,0,0,6,0,0,3,8],
            [0,9,8,0,0,0,4,7,5],
            [5,0,0,9,4,0,0,1,2],
            [0,6,0,2,0,1,0,0,0],
            [0,0,0,0,3,0,0,0,0],
            [0,0,0,6,0,0,7,0,0],
            [7,0,4,0,8,6,2,9,1],
            [2,0,0,0,0,9,3,5,0],
            [0,0,0,3,1,0,0,0,0]

        ]
        solucion = [
            [1,4,2,7,6,5,9,3,8],
            [6,9,8,1,2,3,4,7,5],
            [5,7,3,9,4,8,6,1,2],
            [3,6,7,2,9,1,5,8,4],
            [4,2,5,8,3,7,1,6,9],
            [8,1,9,6,5,4,7,2,3],
            [7,3,4,5,8,6,2,9,1],
            [2,8,1,4,7,9,3,5,6],
            [9,5,6,3,1,2,8,4,7]
        ]


        if not self.window2_is_active:
            self.window2_is_active = True
            self.sounds.facil()

            self.boton = 0
            self.window2 = Toplevel(self.window)
            self.window2.geometry("1100x650")
            self.window2.title("Facil")
            icon_path = resource_path("logo.ico")
            self.window2.iconbitmap(icon_path)




            self.Sudoku(self.window2,data,solucion,"background_niveles/background_nivel_uno.png","#F5B566","black","#2EAB5A",
                        "#EB8C40","#06B1BB","black")



            def on_close():
                self.sounds.inicio()  # Reproducir la canción inicial
                self.window2.destroy()
                self.window2_is_active = False
            self.window2.protocol("WM_DELETE_WINDOW", on_close)

            self.window2.mainloop()

    def nivel_medio(self):

        data = [
            [5,9,0,0,0,0,0,0,0],
            [0,2,7,0,1,0,3,0,9],
            [4,3,8,9,0,0,0,0,6],
            [0,4,3,0,0,0,0,0,0],
            [0,0,0,0,8,0,0,0,0],
            [8,0,0,6,0,2,7,1,0],
            [3,0,0,8,0,0,4,0,0],
            [0,0,0,1,0,0,0,0,0],
            [0,0,0,7,3,5,6,0,0]
        ]
        solucion = [
            [5,9,1,2,6,3,8,7,4],
            [6,2,7,4,1,8,3,5,9],
            [4,3,8,9,5,7,1,2,6],
            [1,4,3,5,7,9,2,6,8],
            [7,6,2,3,8,1,9,4,5],
            [8,5,9,6,4,2,7,1,3],
            [3,7,5,8,2,6,4,9,1],
            [2,8,6,1,9,4,5,3,7],
            [9,1,4,7,3,5,6,8,2]
        ]

        if self.checar_nivel() >= 1:

            if not self.window2_is_active:
                self.window2_is_active = True
                self.sounds.medio()
                self.window2 = Toplevel(self.window)
                self.window2.geometry("1100x650")
                self.window2.title("Medio")
                self.window2.iconbitmap(resource_path("logo.ico"))
                self.boton = 1

                self.Sudoku(self.window2,data,solucion,"background_niveles/background_nivel_dos.png",
                            "#372128", "#6BCF83","#6694AD","#82D144",
                            "#8A8D78","#6BCF83" )


                def on_close():
                    self.sounds.inicio()  # Reproducir la canción inicial
                    self.window2.destroy()
                    self.window2_is_active = False
                self.window2.protocol("WM_DELETE_WINDOW", on_close)

                self.window2.mainloop()

    def nivel_dificil(self):



        data = [
            [0,0,0,0,0,0,8,0,0],
            [0,0,0,3,9,0,0,0,0],
            [0,0,3,0,4,0,2,7,1],
            [4,0,6,0,1,0,0,0,0],
            [0,0,7,8,3,0,0,5,0],
            [0,0,0,0,0,6,0,0,7],
            [0,0,8,9,0,0,7,0,5],
            [0,1,0,0,0,0,0,0,6],
            [2,0,0,0,0,0,0,0,0]
        ]

        solucion = [
            [5, 4, 2, 1, 6, 7, 8, 9, 3],
            [8, 7, 1, 3, 9, 2, 5, 6, 4],
            [9, 6, 3, 5, 4, 8, 2, 7, 1],
            [4, 5, 6, 7, 1, 9, 3, 8, 2],
            [1, 2, 7, 8, 3, 4, 6, 5, 9],
            [3, 8, 9, 2, 5, 6, 4, 1, 7],
            [6, 3, 8, 9, 2, 1, 7, 4, 5],
            [7, 1, 5, 4, 8, 3, 9, 2, 6],
            [2, 9, 4, 6, 7, 5, 1, 3, 8]

        ]

        if self.checar_nivel() >= 2:
            if not self.window2_is_active:
                self.window2_is_active = True
                self.sounds.dificil()
                self.window2 = Toplevel(self.window)
                self.window2.geometry("1100x650")
                self.window2.title("Dificil")
                self.window2.iconbitmap(resource_path("logo.ico"))
                self.boton = 2


                self.Sudoku(self.window2,data,solucion,"background_niveles/background_nivel_tres.png","#00A2E8","black"
                            ,"#C2D1EC","#5D7C78","#CFECF3","black")



                def on_close():
                    self.sounds.inicio()  # Reproducir la canción inicial
                    self.window2.destroy()
                    self.window2_is_active = False
                self.window2.protocol("WM_DELETE_WINDOW", on_close)

                self.window2.mainloop()

    def nivel_imposible(self):

        data = [
            [0, 0, 0, 0, 0, 0, 9, 4, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 2, 7, 8, 0, 0, 0, 0, 0],
            [0, 0, 2, 4, 8, 0, 0, 0, 0],
            [8, 9, 0, 0, 2, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [0, 8, 0, 0, 5, 0, 0, 3, 9]
        ]
        solucion =[
            [6, 3, 8, 7, 1, 2, 9, 4, 5],
            [9, 5, 1, 6, 4, 3, 8, 7, 2],
            [4, 2, 7, 8, 9, 5, 6, 1, 3],
            [5, 6, 2, 4, 8, 1, 3, 7, 9],
            [8, 9, 3, 5, 2, 7, 4, 6, 1],
            [7, 1, 4, 3, 6, 9, 5, 2, 8],
            [3, 4, 9, 1, 7, 8, 2, 5, 6],
            [2, 7, 5, 9, 3, 6, 1, 8, 4],
            [1, 8, 6, 2, 5, 4, 7, 3, 9]
        ]

        if self.checar_nivel() >= 3:
            if not self.window2_is_active:

                self.sounds.imposible()
                self.window2_is_active = True
                self.window2 = Toplevel(self.window)
                self.window2.geometry("1100x650")
                self.window2.title("Imposible")
                self.window2.iconbitmap(resource_path("logo.ico"))
                self.boton = 3


                self.Sudoku(self.window2,data,solucion,"background_niveles/background_nivel_cuatro.png","#D6C0BC","#F83701",
                            "#3F3997","#8A4391","#D2CFB0","#F83701")



                def on_close():
                    self.sounds.inicio()  # Reproducir la canción inicial
                    self.window2.destroy()
                    self.window2_is_active = False
                self.window2.protocol("WM_DELETE_WINDOW", on_close)

                self.window2.mainloop()

    def Sudoku(self,window2,data,solucion,imagen,color_lineas, color_de_numeros, color_de_entrada,color_de_revisar,color_de_limpiar,color_de_letra_entrada):
        self.background = PhotoImage(file=resource_path(imagen))
        canva2 = Canvas(window2, width=1100, height=650)
        canva2.create_image(0, 0, anchor="nw", image=self.background)
        canva2.pack()
        canva2.create_line(85, 222, 1015, 222, fill=color_lineas, width=6)
        canva2.create_line(85, 417, 1015, 417, fill=color_lineas, width=6)

        canva2.create_line(400, 20, 400, 620, fill=color_lineas, width=6)
        canva2.create_line(700, 20, 700, 620, fill=color_lineas, width=6)

        limpiar = Button(window2, text="Limpiar", font=("Arial Rounded MT Bold", "15", "bold"), bg=color_de_limpiar,command=lambda :self.limpiar(window2,color_de_entrada))
        limpiar.place(x=2, y=610)
        revisar = Button(window2, text="Revisar", font=("Arial Rounded MT Bold", "15", "bold"), bg=color_de_revisar,command=lambda :self.revisar(solucion,data,window2,color_de_entrada))
        revisar.place(x=1000, y=610)

        #
        # video = Button(self.window2,width=50, text="Video", font=("Arial Rounded MT Bold", "15", "bold"),bg=color_lineas,command=lambda :self.revisar(solucion,data,self.window2,color_de_entrada))
        # video.place(x=200, y=615)


        y = 60
        for filas in data:
            x = 150
            for columnas in filas:
                if columnas:
                    canva2.create_text(x, y, text=columnas, font=("Arial", 40, "bold"),fill=color_de_numeros,)
                else:
                    self.entry = Entry(window2, width=2, font=("Arial", 35, "bold"), justify='center',
                                  bg=color_de_entrada,fg=color_de_letra_entrada)  # Tamaño del Entry
                    self.entry.place(x=x - 27, y=y - 29)

                x += 100
            y += 65

    def close_window2(self):
        if self.window2 is not None:
            self.window2.destroy()
            self.window2_is_active = False


    def limpiar(self,window2,background):
        entradas = []
        for widget in self.window2.winfo_children():
            if isinstance(widget, Entry):
                entradas.append(widget)
                widget.delete(0, 'end')

        for entry in entradas:
            entry.config(bg=background)

    def revisar(self,solucion,data,window2, color_de_entrada):

        global nivel
        respuestas = []
        entradas = []
        for widget in self.window2.winfo_children():
            if isinstance(widget,Entry):
                respuestas.append(widget.get())
                entradas.append(widget)


        k = 0
        flag = 1
        if "" not in respuestas:
            print("Como todo completado")
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if not data[i][j]:
                        print(respuestas[k])
                        if respuestas[k].isdigit():
                            if int(respuestas[k]) != solucion[i][j]:
                                flag = 0
                                entradas[k].config(bg="#960017")
                            else:
                                entradas[k].config(bg=color_de_entrada)

                        k += 1



        if flag and "" not in respuestas :

            print("Como te e subidoo de nivell")

            self.close_window2()
            window3 = Toplevel()
            window3.geometry("1100x650")
            window3.title("Victoria")
            window3.iconbitmap(resource_path("logo.ico"))
            imagen = None
            text = ""
            color = None




            print(self.boton)
            print(self.nivel)

            if self.boton == 0:
                if int(self.nivel[0]):
                    nivel = self.checar_nivel()+1
                    print("lo agoo")
                    self.modificar(1,0)
                else:
                    nivel = self.checar_nivel()
                imagen = "Wins/win_frezzer.png"
                text = "Felicidades Has \ndebloqueado el \nsiguiente nivel"
                color = "#0F1C2D"

            if self.boton == 1:
                if int(self.nivel[1]):
                    nivel = self.checar_nivel()+1
                    self.modificar(2,0)
                else:
                    nivel = self.checar_nivel()
                imagen = "Wins/win_cell.png"
                text = "Felicidades Has \ndebloqueado el \nsiguiente nivel"
                color = "#D69DFB"

            if self.boton == 2:
                if int(self.nivel[2]):
                    self.modificar(3,0)
                    nivel = self.checar_nivel()+1
                else:
                    nivel = self.checar_nivel()

                imagen = "Wins/win_buu.png"
                text = "Felicidades Has \ndebloqueado el \nsiguiente nivel"
                color = "#EF3BEC"
            if self.boton == 3:
                if int(self.nivel[3]):
                    self.modificar(4,0)
                    nivel = self.checar_nivel()+1
                else:
                    nivel = self.checar_nivel()
                imagen = "Wins/win_jiren.png"
                text = "!! Felicidades !! \n has terminado\nel juego :)))\nWUUUHUUUw "
                color = "#808FD6"

            self.nivel = self.get_niveles()
            print(self.nivel)
            self.background = PhotoImage(file=resource_path(imagen))
            canvas = Canvas(window3, width=1100, height=650)
            canvas.create_image(0,0,anchor="nw",image=self.background)
            canvas.pack()
            canvas.create_text(0,0,anchor="nw",text=text,font=("Curlz MT" ,"120" ,"bold"),fill=color)

            self.modificar(0,nivel)
            self.verificar_nivel()
















from tkinter import *

cat = Tk()
cat.title("gato")
cat.minsize(600, 600)
cat.resizable(width=False, height=False)
cat.geometry("400x400+500+150")
linea = Canvas(cat, width=600, height=600, bg="#9D0E0E")
linea.pack(side=TOP)
linea.create_line(0, 200, 600, 200, width=0, fill="black", tags="line")
linea.create_line(0, 400, 600, 400, width=0, fill="black", tags="line")
linea.create_line(200, 0, 200, 600, width=0, fill="black", tags="line")
linea.create_line(400, 0, 400, 600, width=0, fill="black", tags="line")
shape = "x"
grid = ["0", "1", "2",
        "3", "4", "5",
        "6", "7", "8"]
color = None
boton = None


def click(event):
    global shape, grid
    across = int(linea.canvasx(event.x) / 200)
    down = int(linea.canvasy(event.y) / 200)

    square = across + (down * 3)

    if grid[square] == "x" or grid[square] == "o":
        return

    if shape == "o":
        linea.create_oval(across * 200, down * 200,
                          (across + 1) * 200, (down + 1) * 200,
                          width=5, outline="#04B404", tags="bola")
        grid[square] = "o"

        if grid[0] == "o" and grid[1]=="o" and grid[2]=="o" \
                or grid[3] == "o" and grid[4] == "o" and grid[5] == "o" \
                or grid[6] == "o" and grid[7] == "o" and grid[8] == "o" \
                or grid[0] == "o" and grid[3] == "o" and grid[6] == "o" \
                or grid[1] == "o" and grid[4] == "o" and grid[7] == "o" \
                or grid[2] == "o" and grid[5] == "o" and grid[8] == "o" \
                or grid[0] == "o" and grid[4] == "o" and grid[8] == "o" \
                or grid[2] == "o" and grid[4] == "o" and grid[6] == "o":
            return victoria("O")

        else:
            shape = "x"
    else:
        linea.create_line(across * 200, down * 200,
                          (across + 1) * 200, (down + 1) * 200,
                          width=5, fill="#152597", tags="x")
        linea.create_line(across * 200, (down + 1) * 200,
                          (across + 1) * 200, down * 200,
                          width=5, fill="#152597", tags="x")
        grid[square] = "x"
        if grid[0] == "x" and grid[1]=="x" and grid[2]=="x" \
                or grid[3] == "x" and grid[4] == "x" and grid[5] == "x" \
                or grid[6] == "x" and grid[7] == "x" and grid[8] == "x" \
                or grid[0] == "x" and grid[3] == "x" and grid[6] == "x" \
                or grid[1] == "x" and grid[4] == "x" and grid[7] == "x" \
                or grid[2] == "x" and grid[5] == "x" and grid[8] == "x" \
                or grid[0] == "x" and grid[4] == "x" and grid[8] == "x" \
                or grid[2] == "x" and grid[4] == "x" and grid[6] == "x":
            return victoria("X")

        else:
            shape = "o"

def victoria(r):
    cat.withdraw()
    vict = Toplevel()
    vict.title("Ganador")
    vict.resizable(width=False, height=False)
    vict.geometry("460x100+570+300")
    color = Canvas(vict, width=460, height=100, bg="#9D0E0E")
    color.place(x=0, y=0)
    texto = Label(vict, text="Victoria para:", font=("Goudy Stout",22),bg="#9D0E0E",fg="#2E2E2E")
    texto2 = Label(vict, text=str(r), font=("Goudy Stout",22),bg="#9D0E0E",fg="#2E2E2E")
    boton = Button(vict, width=7, height=2, command=vict.destroy, text="SALIR", bg="#660303", fg="#000000")
    boton.place(x=395, y=50)
    texto.pack()
    texto2.pack()

linea.bind("<Button-1>", click)
cat.mainloop()

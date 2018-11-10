import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana",12)
# print("keaotn")

retPath = [((1, 2, 3), (8, 0, 4), (7, 6, 5)), ((1, 2, 3), (0, 8, 4), (7, 6, 5)), ((0, 2, 3), (1, 8, 4), (7, 6, 5)), ((2, 0, 3), (1, 8, 4), (7, 6, 5)), ((2, 8, 3), (1, 0, 4), (7, 6, 5)), ((2, 8, 3), (1, 6, 4), (7, 0, 5)), ((2, 8, 3), (1, 6, 4), (0, 7, 5)), ((2, 8, 3), (0, 6, 4), (1, 7, 5)), ((2, 8, 3), (6, 0, 4), (1, 7, 5)), ((2, 8, 3), (6, 4, 0), (1, 7, 5)), ((2, 8, 3), (6, 4, 5), (1, 7, 0)), ((2, 8, 3), (6, 4, 5), (1, 0, 7)), ((2, 8, 3), (6, 4, 5), (0, 1, 7)),((2, 8, 3), (0, 4, 5), (6, 1, 7)), ((2, 8, 3), (4, 0, 5), (6, 1, 7)), ((2, 8, 3), (4, 5, 0), (6, 1, 7)), ((2, 8, 0), (4, 5, 3), (6, 1, 7)), ((2, 0, 8), (4, 5, 3), (6, 1, 7)), ((0, 2, 8), (4, 5, 3), (6, 1, 7)), ((4, 2, 8), (0, 5, 3), (6, 1, 7)), ((4, 2, 8), (5, 0, 3), (6, 1, 7)), ((4, 2, 8), (5, 3, 0), (6, 1, 7)), ((4, 2, 0), (5, 3, 8), (6, 1, 7)), ((4, 0, 2), (5, 3, 8), (6, 1, 7)), ((0, 4, 2), (5, 3, 8), (6, 1, 7)), ((5, 4, 2), (0, 3, 8), (6, 1, 7)), ((5, 4, 2), (3, 0, 8), (6, 1, 7)), ((5, 4, 2), (3, 1, 8), (6, 0, 7)), ((5, 4, 2), (3, 1, 8), (0, 6, 7))]

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self,"ruler.ico")
        tk.Tk.title(self, "N-Puzzle")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column = 0, stick="nsew")
        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def keaton(sttr):
    print(sttr)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="start page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="visit page 1",command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="visit page two",command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button_exit = tk.Button(self, text="quit",command=quit)
        button_exit.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PAGE ONE", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="back to home",command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="visit page 2",command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PAGE two", font = LARGE_FONT)
        # label.grid()

        # label1 = tk.Label(self, text="something")
        for puz in retPath:
            for x,line in enumerate(puz):
                for y, num in enumerate(line):
                    tk.Label(self,text=str(num)).grid(column=x,row=y)
        # label1.grid(column)
        # l.pack()
        # button1 = tk.Button(self, text="back to home",command=lambda: controller.show_frame(StartPage))
        # button1.pack()
        # button2 = tk.Button(self, text="visit page one",command=lambda: controller.show_frame(PageOne))
        # button2.pack()


app = Window()
app.mainloop()

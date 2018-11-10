import tkinter as tk
import time
from puzzleGen import puzzleGenerator


LARGE_FONT = ("Times", 20)

retPath = [((5, 4, 2), (3, 0, 8), (6, 1, 7)), ((5, 4, 2), (3, 1, 8), (6, 0, 7)), ((5, 4, 2), (3, 1, 8), (0, 6, 7))]
# retPath = [((1, 2, 3), (8, 0, 4), (7, 6, 5)), ((1, 2, 3), (0, 8, 4), (7, 6, 5)), ((0, 2, 3), (1, 8, 4), (7, 6, 5)), ((2, 0, 3), (1, 8, 4), (7, 6, 5)), ((2, 8, 3), (1, 0, 4), (7, 6, 5)), ((2, 8, 3), (1, 6, 4), (7, 0, 5)), ((2, 8, 3), (1, 6, 4), (0, 7, 5)), ((2, 8, 3), (0, 6, 4), (1, 7, 5)), ((2, 8, 3), (6, 0, 4), (1, 7, 5)), ((2, 8, 3), (6, 4, 0), (1, 7, 5)), ((2, 8, 3), (6, 4, 5), (1, 7, 0)), ((2, 8, 3), (6, 4, 5), (1, 0, 7)), ((2, 8, 3), (6, 4, 5), (0, 1, 7)),((2, 8, 3), (0, 4, 5), (6, 1, 7)), ((2, 8, 3), (4, 0, 5), (6, 1, 7)), ((2, 8, 3), (4, 5, 0), (6, 1, 7)), ((2, 8, 0), (4, 5, 3), (6, 1, 7)), ((2, 0, 8), (4, 5, 3), (6, 1, 7)), ((0, 2, 8), (4, 5, 3), (6, 1, 7)), ((4, 2, 8), (0, 5, 3), (6, 1, 7)), ((4, 2, 8), (5, 0, 3), (6, 1, 7)), ((4, 2, 8), (5, 3, 0), (6, 1, 7)), ((4, 2, 0), (5, 3, 8), (6, 1, 7)), ((4, 0, 2), (5, 3, 8), (6, 1, 7)), ((0, 4, 2), (5, 3, 8), (6, 1, 7)), ((5, 4, 2), (0, 3, 8), (6, 1, 7)), ((5, 4, 2), (3, 0, 8), (6, 1, 7)), ((5, 4, 2), (3, 1, 8), (6, 0, 7)), ((5, 4, 2), (3, 1, 8), (0, 6, 7))]
retPath = reversed(retPath)
lst = iter(retPath)

class NpuzzleWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, padx=100, pady=100)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (ChoosingParam, VisuResult):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ChoosingParam)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def startNpuzzle(self, var_size, var_choix):
        print("here")
        # time.sleep(2)
        size = int(var_size.get())
        print("var_size.get(): ", size)
        # HERE call the real function
        retPuzz = puzzleGenerator(size)
        print("ret puzz gen =", retPuzz)
        print("There")
        print("var_choix.get(): ", var_choix.get())
        self.show_frame(VisuResult)

class ChoosingParam(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Please choose a Size :", font=LARGE_FONT, fg="#4286f4")
        label1.pack(pady=10, padx=10)
        var_size = tk.StringVar(value="3")
        choice_two = tk.Radiobutton(self, text="2 X 2", variable=var_size, value="2")
        choice_three = tk.Radiobutton(self, text="3 X 3", variable=var_size, value="3")
        choice_four = tk.Radiobutton(self, text="4 X 4", variable=var_size, value="4")
        choice_five = tk.Radiobutton(self, text="5 X 5", variable=var_size, value="5")
        choice_two.pack()
        choice_three.pack()
        choice_four.pack()
        choice_five.pack()

        label = tk.Label(self, text="Please choose a Heuristic :", font=LARGE_FONT, fg="#2a6cd6")
        label.pack(pady=10, padx=10)

        var_choix = tk.StringVar(value="md")
        choice_manhatthan = tk.Radiobutton(self, text="Manhattan Distance", variable=var_choix, value="md")
        choice_manhatthan_linear = tk.Radiobutton(self, text="Manhattan + Linear Conflict", variable=var_choix, value="lc")
        choice_gashing = tk.Radiobutton(self, text="Not in Place", variable=var_choix, value="np")
        choice_Misplaced = tk.Radiobutton(self, text="n-MaxSwap", variable=var_choix, value="gt")
        choice_manhatthan.pack()
        choice_manhatthan_linear.pack()
        choice_gashing.pack()
        choice_Misplaced.pack()
        # a la fermeture de la fenetre
        # print("var_choix.get(): ", var_choix.get())

        # button = tk.Button(self, text="Start The N-Puzzle", command=lambda: controller.show_frame(VisuResult))
        button = tk.Button(self, text="Start The N-Puzzle", command=lambda: controller.startNpuzzle(var_size, var_choix))
        button.pack()





class VisuResult(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Frame1 = tk.Frame(self, borderwidth=2, relief="groove", bg='#80c0c0')
        self.Frame1.pack(side="top", padx=30, pady=30)

        self.Frame2 = tk.Frame(self, borderwidth=2)
        self.Frame2.pack(side="bottom", padx=30, pady=30)

        self.tex1 = tk.Label(self, text='Here we go, we save the puzzle in * 30 * iterations', fg='#228B22', font=LARGE_FONT)
        self.tex2 = tk.Label(self, text='This is the goal state <3', fg='red', font=LARGE_FONT)
        self.tex1.pack()

        puzz = next(lst)
        self.tabPuzz(puzz)


    def tabPuzz(self, puzz):
        Frame2 = self.Frame2
        Frame1 = self.Frame1
        self.exit_button = tk.Button(Frame2, width=7, height=2, text="Exit", command=self.quit)
        self.next_button = tk.Button(Frame2, width=7, height=2, text="Next Step", command=self.nextStep)

        y = 0
        x = 0
        for line in puzz:
            for num in line:
                tmp = str(num)
                if (num == 0):
                    tk.Label(Frame1, text=' %s ' % tmp, borderwidth=5, relief="sunken", padx=10, pady=10, foreground="maroon", font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
                else :
                    tk.Label(Frame1, text=' %s ' % tmp, borderwidth=5, relief="sunken", padx=10, pady=10, font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
                x += 1
            y +=1
            x = 0
        self.exit_button.grid(row=y + 1, column=x + 1)
        self.next_button.grid(row=y + 1, column=x)


    def nextStep(self):
        global lst
        try :
            puzz = next(lst)
            print("puzz", puzz)
            self.tabPuzz(puzz)
        except:
            self.tex2.pack(padx=30, pady=30)
            # self.tex2.grid(row=1000, column=1000, padx=30, pady=30)
            print("------ Final state reached ------")







        # label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)

        # button1 = tk.Button(
        #     self,
        #     text="Back to Home",
        #     command=lambda: controller.show_frame(ChoosingParam))
        # button1.pack()





app = NpuzzleWindow()
app.mainloop()











































# # MY CODE ---------------------
# class MyMainWindow(Frame):
#     def __init__(self, myWindow, **kwargs):
#         global lst
#         Frame.__init__(self, myWindow, width=768, height=576, padx=10, pady=10, **kwargs)
#         # Frame.__init__(self, myWindow, width=768, height=576, padx=10, pady=10, **kwargs,  bg = '#4286f4')
#         self.pack(fill=BOTH, expand=True, side=TOP)

#         self.Frame1 = Frame(myWindow, borderwidth=2, relief=GROOVE, bg='#80c0c0')
#         self.Frame1.pack(side=TOP, padx=30, pady=30)

#         self.Frame2 = Frame(myWindow, borderwidth=2)
#         # self.Frame2 = Frame(myWindow, borderwidth=2, bg='#157562')
#         self.Frame2.pack(side=BOTTOM, padx=30, pady=30)

#         self.tex1 = Label(self, text='Here we go, we save the puzzle in * 30 * iterations', fg='#228B22', font=LARGE_FONT)
#         self.tex2 = Label(self, text='This is the goal state <3', fg='red', font=LARGE_FONT)
#         self.tex1.pack()

#         puzz = next(lst)
#         self.tabPuzz(puzz)



#     def tabPuzz(self, puzz):
#         Frame2 = self.Frame2
#         Frame1 = self.Frame1
#         self.exit_button = Button(Frame2, width=7, height=2, text="Exit", command=self.quit)
#         self.next_button = Button(Frame2, width=7, height=2, text="Next Step", command=self.nextStep)

#         y = 0
#         x = 0
#         for line in puzz:
#             for num in line:
#                 tmp = str(num)
#                 if (num == 0):
#                     Label(Frame1, text=' %s ' % tmp, borderwidth=5, relief=SUNKEN, padx=10, pady=10, foreground="maroon", font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
#                 else :
#                     Label(Frame1, text=' %s ' % tmp, borderwidth=5, relief=SUNKEN, padx=10, pady=10, font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
#                 x += 1
#             y +=1
#             x = 0
#         self.exit_button.grid(row=y + 1, column=x + 1)
#         self.next_button.grid(row=y + 1, column=x)


#     def nextStep(self):
#         global lst
#         try :
#             puzz = next(lst)
#             print("puzz", puzz)
#             self.tabPuzz(puzz)
#         except:
#             self.tex2.pack(padx=30, pady=30)
#             # self.tex2.grid(row=1000, column=1000, padx=30, pady=30)
#             print("------ Final state reached ------")





# On crée une fenêtre, racine de notre interface
# myWindow = Tk()
# myWindow.eval('tk::PlaceWindow %s center' % myWindow.winfo_pathname(myWindow.winfo_id()))
# interface = MyMainWindow(myWindow)

# interface.mainloop()
# interface.destroy()



















# from tkinter import *



# retPath = [((1, 2, 3), (8, 0, 4), (7, 6, 5)), ((1, 2, 3), (0, 8, 4), (7, 6, 5)), ((0, 2, 3), (1, 8, 4), (7, 6, 5)), ((2, 0, 3), (1, 8, 4), (7, 6, 5)), ((2, 8, 3), (1, 0, 4), (7, 6, 5)), ((2, 8, 3), (1, 6, 4), (7, 0, 5)), ((2, 8, 3), (1, 6, 4), (0, 7, 5)), ((2, 8, 3), (0, 6, 4), (1, 7, 5)), ((2, 8, 3), (6, 0, 4), (1, 7, 5)), ((2, 8, 3), (6, 4, 0), (1, 7, 5)), ((2, 8, 3), (6, 4, 5), (1, 7, 0)), ((2, 8, 3), (6, 4, 5), (1, 0, 7)), ((2, 8, 3), (6, 4, 5), (0, 1, 7)),((2, 8, 3), (0, 4, 5), (6, 1, 7)), ((2, 8, 3), (4, 0, 5), (6, 1, 7)), ((2, 8, 3), (4, 5, 0), (6, 1, 7)), ((2, 8, 0), (4, 5, 3), (6, 1, 7)), ((2, 0, 8), (4, 5, 3), (6, 1, 7)), ((0, 2, 8), (4, 5, 3), (6, 1, 7)), ((4, 2, 8), (0, 5, 3), (6, 1, 7)), ((4, 2, 8), (5, 0, 3), (6, 1, 7)), ((4, 2, 8), (5, 3, 0), (6, 1, 7)), ((4, 2, 0), (5, 3, 8), (6, 1, 7)), ((4, 0, 2), (5, 3, 8), (6, 1, 7)), ((0, 4, 2), (5, 3, 8), (6, 1, 7)), ((5, 4, 2), (0, 3, 8), (6, 1, 7)), ((5, 4, 2), (3, 0, 8), (6, 1, 7)), ((5, 4, 2), (3, 1, 8), (6, 0, 7)), ((5, 4, 2), (3, 1, 8), (0, 6, 7))]
# # reversed(retPath)
# # lst = iter(retPath)


# class MyMainWindow(Frame):
#     def __init__(self, myWindow, **kwargs):
#         global lst
#         Frame.__init__(self, myWindow, width=768, height=576, padx=10, pady=10, **kwargs)
#         self.pack(fill=BOTH, expand = True)
#         self.nb_click = 0

#         self.Frame1 = Frame(myWindow, borderwidth=2, relief=GROOVE)
#         self.Frame1.pack(side=TOP, padx=30, pady=30)

#         self.Frame2 = Frame(myWindow, borderwidth=2)
#         self.Frame2.pack(side=BOTTOM, padx=30, pady=30)
#         # self.Frame2.pack(side=BOTTOM, padx=30, pady=30, fill=BOTH, expand=True)

#         # self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.", foreground="red")
#         # self.message.pack()

#         # self.exit_button = Button(self, text="Exit", command=self.quit)
#         # self.exit_button.pack(side="left")

#         # self.click_button = Button(self, text="Click here", command=self.click)
#         # self.click_button.pack(side="right")

#         self.tabPuzz()
#         # self.nextStep(Frame1, Frame2)


#     def tabPuzz(self):
#         global retPath
#         # puzz = next(lst)
#         # print("debut tabPuzz= ", puzz)
#         Frame2 = self.Frame2
#         Frame1 = self.Frame1
#         var = IntVar()
#         self.exit_button = Button(Frame2, width=7, height=2, text="Exit", command=self.quit)
#         self.next_button = Button(Frame2, width=7, height=2, text="Next Step", command=lambda: var.set(1))
#         # self.next_button = Button(Frame2, width=7, height=2, text="Next Step", command=self.nextStep(Frame1, Frame2))

#         retPath = reversed(retPath)
#         lst = iter(retPath)
#         puzz = next(lst)
#         while puzz:
#             y = 0
#             x = 0
#             for line in puzz:
#                 # print(line)
#                 for num in line:
#                     tmp = str(num)
#                     Label(Frame1, text=' %s ' % tmp, borderwidth=1, relief=SUNKEN, padx=2, pady=2).grid(row=y, column=x)
#                     x += 1
#                 y +=1
#                 x = 0

#             self.exit_button.grid(row=y + 1, column=x + 1)
#             self.next_button.grid(row=y + 1, column=x)

#             self.next_button.wait_variable(var)
#             var.set(0)
#             puzz = next(lst)
#             print("puzz : ", puzz)
#         self.quit

#         # print("debut tabPuzz= ", puzz)
#         # Frame2 = self.Frame2
#         # Frame1 = self.Frame1
#         # self.exit_button = Button(Frame2, width=7, height=2, text="Exit", command=self.quit)
#         # self.next_button = Button(Frame2, width=7, height=2, text="Next Step", command=self.nextStep(Frame1, Frame2))
#         # # self.next_button = Button(Frame2, width=7, height=2, text="Next Step", command=self.nextStep(Frame1, Frame2))
#         # y = 0
#         # x = 0
#         # for line in puzz:
#         #     print(line)
#         #     for num in line:
#         #         tmp = str(num)
#         #         Label(Frame1, text=' %s ' % tmp, borderwidth=1, relief=SUNKEN, padx=2, pady=2).grid(row=y, column=x)
#         #         x += 1
#         #     y +=1
#         #     x = 0

#         # self.exit_button.grid(row=y + 1, column=x + 1)
#         # self.next_button.grid(row=y + 1, column=x)



#     def nextStep(self, Frame1, Frame2):
#         global lst

#         puz = next(lst)
#         print("blalba")
#         # self.tabPuzz(Frame1, Frame2, puz)
#         # lst = iter(retPath)
#         # print("avant next lst in nextStep is = ", lst)
#         # puzz = next(lst)
#         # print("APRES next puzz in nextStep is = ", puzz)
#         # if puzz:
#         #     print("puzz", puzz)
#         #     self.tabPuzz(Frame1, Frame2, puzz)
#         # else :
#         #     print("iterations FIN")
#         #     self.quit




#     # def tabPuzz(self, Frame1, Frame2):
#     #     self.try_button = Button(Frame2, width=7, height=2, text="Exit", command=self.quit)
#     #     for tupple in retPath:
#     #         y = 0
#     #         for line in tupple:
#     #             x = 0
#     #             for num in line:
#     #                 tmp = str(num)
#     #                 Label(Frame1, text=' %s ' % tmp, borderwidth=1, relief=SUNKEN, padx=2, pady=2).grid(row=y, column=x)
#     #                 x += 1
#     #             y += 1
#     #     self.try_button.grid(row=y +1, column=x +1)






# # On crée une fenêtre, racine de notre interface
# myWindow = Tk()
# interface = MyMainWindow(myWindow)
# # for i in range(len(lst)):
# #     puz = next(lst)
# # interface.tabPuzz()
# # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
# interface.mainloop()
# interface.destroy()












# # Frame content objects
# # /!\ Utiliser le "cadre" a la place de la "fenetre" pour mettre dedans
# # au call des autres variables / widgets
# cadre = Frame(myWindow, width=1000, height=1000, borderwidth=1)
# cadre.pack(fill=BOTH)
# message = Label(cadre, text="Notre fenêtre")
# message.pack(side="top", fill=X)

# # On crée un label (ligne de texte). a la place "Text" peut avoir plusieurs lignes de texte
# champ_label = Label(myWindow, text=" N Puzzle ")

# # On affiche le label dans la fenêtre (positionner dans la fenetre)
# champ_label.pack()

# # input field
# var_texte = StringVar()
# ligne_texte = Entry(myWindow, textvariable=var_texte, width=30)
# ligne_texte.pack()

# var_case = IntVar()
# case = Checkbutton(myWindow, text="Ne plus poser cette question", variable=var_case)
# case.pack()

# # radio button (un seul selectionneé a la fois)
# var_choix = StringVar()
# choix_rouge = Radiobutton(myWindow, text="Rouge", variable=var_choix, value="rouge")
# choix_vert = Radiobutton(myWindow, text="Vert", variable=var_choix, value="vert")
# choix_bleu = Radiobutton(myWindow, text="Bleu", variable=var_choix, value="bleu")
# choix_rouge.pack()
# choix_vert.pack()
# choix_bleu.pack()

# # Liste deroulante
# liste = Listbox(myWindow)
# liste.pack()
# liste.insert(END, "Pierre")
# liste.insert(END, "Feuille")
# liste.insert(END, "Ciseau")

# # Exit button
# bouton_quitter = Button(myWindow, text="Exit", command=myWindow.quit)
# bouton_quitter.pack()


# # s'affiche a la fermeture de la fenetre
# print("var_case.get(): ", var_case.get())
# print("var_choix.get(): ", var_choix.get())
# print("liste.curselection(): ", liste.curselection())

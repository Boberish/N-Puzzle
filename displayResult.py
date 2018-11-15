import tkinter as tk
import time
from keatongen import puzzleGenSolvability
from gui_interface import staringNpuzzleWithGui
import settings


LARGE_FONT = ("Times", 20)

retPath = []
lst = None
alreadyBeenHere = False


class MyMainWindow(tk.Frame):
    def __init__(self, myWindow, **kwargs):
        global lst
        tk.Frame.__init__(self, myWindow, width=768, height=576, padx=10, pady=10, **kwargs)
        self.pack(fill="both", expand = True)

        self.Frame1 = tk.Frame(myWindow, borderwidth=2, relief="groove")
        self.Frame1.pack(side="top", padx=30, pady=10)

        self.Frame1bis = tk.Frame(myWindow, borderwidth=2)
        self.Frame1bis.pack(side="bottom", padx=30, pady=10)

        self.Frame2 = tk.Frame(myWindow, borderwidth=2)
        self.Frame2.pack(side="bottom", padx=30, pady=10)

        self.askingParameters()

    def askingParameters(self):
        label2 = tk.Label(self, text="Please :", font=LARGE_FONT, fg="#4286f4")
        label2.pack(pady=10, padx=10)
        var_solv = tk.StringVar(value=True)
        choice_solvable = tk.Radiobutton(self, text="Solvable", variable=var_solv, value=True)
        choice_unsolvable = tk.Radiobutton(self, text="Unsolvable", variable=var_solv, value=False)
        choice_solvable.pack()
        choice_unsolvable.pack()

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
        choice_Greedy = tk.Radiobutton(self, text="Super Fast", variable=var_choix, value="gr")
        choice_Dijkstra = tk.Radiobutton(self, text="Uniform Cost Algorithm", variable=var_choix, value="uc")
        choice_manhatthan.pack()
        choice_manhatthan_linear.pack()
        choice_gashing.pack()
        choice_Misplaced.pack()
        choice_Greedy.pack()
        choice_Dijkstra.pack()

        button = tk.Button(self, text="Start The N-Puzzle", command=lambda: self.startNpuzzle(var_size, var_choix, var_solv))
        button.pack()

    def startNpuzzle(self, var_size, var_choix, var_solv):
        global retPath
        global lst

        interface.destroy()

        size = int(var_size.get())
        solv = var_solv.get()

        if solv == '0':
            unsolvablePuzzle = puzzleGenSolvability(False, size)
            self.printUnsolvablePuzzle(unsolvablePuzzle)
            return 0

        retPuzz = puzzleGenSolvability(True, size)
        retPath = staringNpuzzleWithGui(size, retPuzz, var_choix)

        nbStepPath = str(len(retPath))
        retPath = reversed(retPath)
        lst = iter(retPath)

        puzz = next(lst)
        self.printPuzzle(puzz, nbStepPath)

    def printUnsolvablePuzzle(self, puzz):
        tk.Label(self.Frame1bis, text='This Puzzle is Unsolvable ', fg='#cc0052', font=LARGE_FONT).grid(row=1, column=1)

        self.exit_button = tk.Button(self.Frame2, width=7, height=2, text="Exit", padx=10, pady=10, command=self.quit)

        y = 0
        x = 0
        for line in puzz:
            for num in line:
                tmp = str(num)
                if (num == 0):
                    tk.Label(self.Frame1, text=' %s ' % tmp, borderwidth=5, relief="sunken", padx=10, pady=10, foreground="#cc0052", font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
                else :
                    tk.Label(self.Frame1, text=' %s ' % tmp, borderwidth=5, relief="sunken", padx=10, pady=10, font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
                x += 1
            y +=1
            x = 0

        self.exit_button.grid(row=y + 1, column=x + 1)

    def printPuzzle(self, puzz, nbStepPath):
        tk.Label(self.Frame1bis, text='Here we go, we solve the puzzle in ' + str(nbStepPath) + ' steps \n and with ' + str(settings.nbIteration) + ' Iterations. \n Memory complexity: ' + str(settings.memComplexity) + '.', fg='#005580', font=LARGE_FONT).grid(row=1, column=1)

        self.next_button = tk.Button(self.Frame2, width=7, height=2, text="Next Step", padx=10, pady=10, command=lambda: self.nextStep(x, y, nbStepPath))
        self.exit_button = tk.Button(self.Frame2, width=7, height=2, text="Exit", padx=10, pady=10, command=self.quit)

        y = 0
        x = 0
        for line in puzz:
            for num in line:
                tmp = str(num)
                if (num == 0):
                    tk.Label(self.Frame1, text=' %s ' % tmp, borderwidth=5, relief="sunken", padx=10, pady=10, foreground="#cc0052", font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
                else :
                    tk.Label(self.Frame1, text=' %s ' % tmp, borderwidth=5, relief="sunken", padx=10, pady=10, font=LARGE_FONT).grid(row=y, column=x, padx=10, pady=10)
                x += 1
            y +=1
            x = 0

        self.exit_button.grid(row=y + 1, column=x + 1)
        self.next_button.grid(row=y + 1, column=x)

    def nextStep(self, x, y, nbStepPath):
        global lst
        try :
            puzz = next(lst)
            print("puzz", puzz)
            self.printPuzzle(puzz, nbStepPath)
        except:
            tk.Label(self.Frame1bis, text='This is the goal!', fg='red', font=LARGE_FONT).grid(row=0, column=1, padx=30, pady=30)
            print("------ Final state reached ------")



# On crée une fenêtre, racine de notre interface
myWindow = tk.Tk()
myWindow.attributes("-topmost", True)
myWindow.eval('tk::PlaceWindow %s center' % myWindow.winfo_pathname(myWindow.winfo_id()))

interface = MyMainWindow(myWindow)
interface.mainloop()
try:
    interface.destroy()
except:
    pass
from parserOne import parsing, init, doit
import settings


def staringNpuzzleWithGui(size, puzzle, var_choix):
    settings.initGlobals()
    settings.size = size
    settings.heristicChoice = var_choix.get()
    print("HEuristic Choice == ", settings.heristicChoice)

    init(puzzle)
    path, settings.nbIteration, settings.memComplexity = doit(puzzle)
    return path

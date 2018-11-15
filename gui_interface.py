from parserOne import init, doit
import settings


def staringNpuzzleWithGui(size, puzzle, var_choix):
    settings.initGlobals()
    settings.size = size
    settings.heristicChoice = var_choix.get()

    init(puzzle)
    path, settings.nbIteration, settings.memComplexity = doit(puzzle)
    return path

from parserOne import parsing, init, doit
import settings


def staringNpuzzleWithGui(size, puzzle, heristicChoice):
    settings.initGlobals()
    settings.size = size
    settings.heristicChoice = heristicChoice

    init(puzzle)
    path, settings.nbIteration, settings.memComplexity = doit(puzzle)
    return path

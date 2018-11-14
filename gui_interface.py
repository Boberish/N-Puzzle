from parserOne import parsing, init, doit
import settings


def staringNpuzzleWithGui(size, puzzle, heristicChoice):
    settings.initGlobals()
    print("Before the parsing")
    settings.size = size
    settings.heristicChoice = heristicChoice

    print("puzzle after tuple: ", puzzle)

    init(puzzle)
    path = doit(puzzle)
    print("final path?: ", path)
    return path

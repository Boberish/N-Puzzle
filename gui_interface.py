from parserOne import parsing, init, doit
import settings


def staringNpuzzleWithGui(size, puzzle, heristicChoice):
    settings.initGlobals()
    print("Before the parsing")
    settings.size = size
    settings.heristicChoice = heristicChoice

    # puzzle = puzzleGenSolvability(True)
    print("puzzle after tuple: ", puzzle)

    init(puzzle)
    path = doit(puzzle)
    print("final path?: ", path)
    return path

    # puzzle = parsing(puzzle)
    # print("staringNpuzzleWithGui: ", puzzle)
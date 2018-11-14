import random
import settings
from parserOne import is_solvable, init, make_goal
# settings.initGlobals()
# size = settings.size

def randpuz():
    seq = []
    puz = []

    for num in range(settings.size*settings.size):
        seq.append(num)
    for num in range(settings.size*settings.size):
        ran = random.choice(seq)
        puz.append(ran)
        seq.remove(ran)
    realfin = []
    for line in range(0, settings.size * settings.size,settings.size):
        realfin.append(puz[line:line + settings.size])
    done = tuple(tuple(x) for x in realfin)
    init(done)
    return (is_solvable(done), done)

def puzzleGenSolvability(solv, size):
    settings.size = size
    if solv == True:
        while 1:
            hold,puz= randpuz()
            if hold == 0:
                break
    else:
        while 1:
            hold2,puz = randpuz()
            if hold2 == 1:
                break
    print(puz)
    return(puz)

# thing(False)
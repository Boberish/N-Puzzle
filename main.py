from parserOne import *
from settings import *

def main():
    settings.initGlobals()
    start = parsing(opening())
    print("Staring puzzle", start)
    init(start)
    doit(start)


main()
from parserOne import *
from settings import *

def main():
    settings.initGlobals()
    start = parsing(opening())
    print("HERE in main start", start)
    init(start)
    doit(start)


main()

while :
do
    python realpuzgen.py -u 3 > iter5check.txt
    python3 parser.py iter5check.txt a
done
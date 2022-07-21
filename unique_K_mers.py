import sys
import ast

if __name__ == '__main__':
    with open('mot.txt', 'r') as m:
        mot = ast.literal_eval(m.read())
    with open('fat.txt', 'r') as f:
        fat = ast.literal_eval(f.read())
    diff=fat-mot


    as.str()
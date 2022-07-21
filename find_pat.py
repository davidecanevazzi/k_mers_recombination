import sys
import ast

if __name__ == '__main__':
    name='ciao'
    c=0
    with open('fat_unique_8_kmers.txt', 'r') as u:
        uniques = ast.literal_eval(u.read())
    with open('statistic_up.fasta') as dau:
        for i in dau:
            if(i[0]=='>'):
                name=i
            else:
                for k_mer in uniques:
                    if k_mer in i:
                        c=c+1
                print(name+' '+str(c))
            c=0

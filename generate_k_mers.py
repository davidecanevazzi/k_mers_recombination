import sys



def k_mer_split(read,dim,step):
    k_mer=[]
    i=0
    num=1
    while i< len(read)-dim:
        k_mer.append(read[i:i+dim])
        i+=step
        num=num+1
    return k_mer
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    res=set()
    with open("fat_mit_filtered.fasta") as fasta:
        for i in fasta:
            if(i[0]=='>'):
                append=1
            else:
                res=set().union(set(k_mer_split(i,12,1)),res)

    with open('fat.txt', 'w') as f:
        f.write(str(res))

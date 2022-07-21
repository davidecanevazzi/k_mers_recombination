import ast

if __name__ == '__main__':
    res=set()
    file=""
    with open('fat_uniq_12_mers.txt', 'r') as u:
        k_mers = ast.literal_eval(u.read())
    with open("fat_mit_filtered_checked.fasta") as fasta:
        for j in fasta:
            file=file+j

    for i in k_mers:
        if file.count(i) > 10:
            res.add(i)

    print(res)
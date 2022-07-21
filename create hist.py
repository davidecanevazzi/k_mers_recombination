
import seaborn as sns

from scipy.stats import norm

import matplotlib.pyplot as plt



count=list()
if __name__ == '__main__':
    with open('statistic_8_mer_count.txt', 'r') as stat:
        for i in stat:
            if(i[0]!='>'):
                count.append(int(i))

    x_tick=range(12)
    #plt.hist(count)
    #plt.xticks(x_tick)
    #plt.show()

    #p=sns.histplot(data=count)

    sns.distplot(count,bins=12,fit=norm, kde=False)


    plt.show()
import numpy as np
from numpy.random import rand
import click
import pandas as append
import matplotlib.pyplot as plt
import matplotlib.cm as cm


@click.command()
@click.option("--reps", "reps", default=1000, help="Number of repetitions")
@click.option("--N", "N", default=18300, help="Number of austronauts")
@click.option("--s", "s", default=11, help="How many are selected")
@click.option("--w", "w", default=0.95, help="weight of skill, experience, hard work ")

def main(reps,N,s,w):
    
    def random_score(N):
        return rand(N)

    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def difference(lst1, lst2):
        lst3 = [value for value in lst1 if value not in lst2]
        return lst3
    
    def select(N,s,w):
        skill = random_score(N)
        luck = random_score(N)
        A=[]

        for i,j in zip(skill, luck):
            A.append((i,j,w*i+(1-w)*j))
   
        A_overal = sorted(A, key=lambda a: a[2], reverse = True)
        A_skill = sorted(A, key=lambda a: a[0], reverse = True)
        A_luck = sorted(A, key=lambda a: a[1], reverse = True)

#        for i in range(s):
#            print(A_overal[i],'\t',A_skill[i])
    
        #print(A_overal)
        #print(A_skill[:s])

        groups = ['A{}'.format(i) for i in range(1,s+1)]
    
        overal_scores_1 = [a[2] for a in A_overal[:s]]
        skill_scores_1 = [a[0]*0.95 for a in A_overal[:s]]
        luck_scores_1 = [a[1]*0.05 for a in A_overal[:s]]
    
        same = intersection(A_overal[:s], A_skill[:s])
        diff = difference(A_overal[:s], same)

        order_skill_same = [A_skill.index(a) for a in same]
        order_luck_same = [A_luck.index(a) for a in same]

        order_skill_diff = [A_skill.index(a) for a in diff]
        order_luck_diff = [A_luck.index(a) for a in diff]

        print(len(same))
        
        for i in range(len(same)):
            print(same[i],'\tskill:',order_skill_same[i],'\tluck:',order_luck_same[i])
        print('\n')
        for i in range(len(diff)):
            print(diff[i],'\tskill:',order_skill_diff[i],'\tluck:',order_luck_diff[i])
        mean_luck_selected = (np.mean(luck_scores_1),len(same))
        return(mean_luck_selected, same)
 
    mean_run_collection = []
    for i in range(reps):
        mean_run_collection.append(select(N,s,w))

       #fig, ax = plt.subplots(2)
       #fig.tight_layout()

       #ax[0].bar(groups, skill_scores_1)
       #ax[0].bar(groups, luck_scores_1, 0.4, bottom = skill_scores_1)
       #ax[0].bar(groups, overal_scores_1, 0.4)
       #ax[0].set_title('W/5% Luck')

       #ax[1].bar(groups, overal_scores_1)
       #ax[1].bar(groups, skill_scores_1, bottom = overal_scores_1)
       #ax[1].set_title('Only Skill')

       #plt.show()

if __name__ == '__main__':
    main()

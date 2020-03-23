# from pathlib import Path
import glob
#import file
#|374|[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower)|[python](./Python/374_Guess%20Number%20Higher%20or%20Lower.py)|Easy|
def generatetable():
    lines = []
    for fn in glob.glob(r'E:\郭志\Leetcode\Python\*.py'):
        fn = fn.split('\\')[-1].split('.')[0]
        no, title = fn.split('_')
        leetcode_ln = title.replace(' ','-').replace('---','-')
        leetcode_ln = f'https://leetcode.com/problems/{leetcode_ln}'
        git_ln = fn.replace(' ','%20')
        git_ln = f'{git_ln}.py'
        line = (int(no), f'|{no}|[{title}]({leetcode_ln})|[python]({git_ln})')
        lines.append(line)

    lines = [l[1] for l in sorted(lines)]
    output_fn = r'E:\郭志\Leetcode\table.txt'
    with open(output_fn,"w") as f:
        f.write('\n'.join(lines))

    
#generatetable()

    
    

    


if __name__ == '__main__':
    generatetable()

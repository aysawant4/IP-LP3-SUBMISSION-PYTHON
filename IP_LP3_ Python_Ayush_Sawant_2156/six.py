#CODING QUESTIONS:6
import re

n=str(input())
s=re.sub('not.*?poor','good',n)
print(s)

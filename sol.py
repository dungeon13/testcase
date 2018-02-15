from itertools import permutations
n=int(input())
for i in range(n):
  a=0
  s=input()
  lis=[s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]
  lis1=[]
  for ele in lis:
    if len(ele)==4:
      lis1.append(ele)
  print(lis1)
  perms=[''.join(p) for p in permutations('chef')]
  for ele1 in lis1:
    if ele1 in perms:
      a+=1
  if a>0:
    print('lovely',a)
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

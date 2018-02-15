from itertools import permutations
n=int(input())
def sub_string(s):
  l=len(s)
  return [s[i:j+1] for i in range(l) for j in range(i,l)]
for i in range(n):
  a=0
  lis=sub_string(input())
  perms=[''.join(p) for p in permutations('chef')]
  for ele in lis:
    if ele in perms:
      a+=1
  if a>0:
    print('lovely ',a)

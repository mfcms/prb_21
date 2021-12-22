import sys
def pal(a):
    k=0
    b=[x for y in a.split() for x in y]
    for i in range(len(a)//2):
        if b[i]!=b[-i-1]:
            k+=1
    return k
a=input('Введите фразу: ')
j=pal(a)
if j>0:
      print('Фраза не является палиндромом')
else:
    print('Фраза является палиндромом')

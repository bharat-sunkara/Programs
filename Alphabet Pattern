#https://www.hackerrank.com/challenges/alphabet-rangoli
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
N = int(input())
lis0 = []
lis0_str = ''
length = 0
for i in range((N-1), -(N), -1):
    lis0.append(alp[abs(i)])
    
length = len('-'.join(lis0))  
lis0_str = ''.join(lis0)

for i in range(N):
    print('-'.join(list(lis0_str[:i+1]+lis0_str[len(lis0_str)-i:])).center(length,'-'))
    
for i in range(N-2,-1,-1):
    print('-'.join(list(lis0_str[:i+1]+lis0_str[len(lis0_str)-i:])).center(length,'-'))    
    

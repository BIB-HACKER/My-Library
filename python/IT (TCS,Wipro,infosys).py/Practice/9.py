#permutation

def fact(n):
    if(n==0 or n==1):
        return n
    return n*fact(n-1)  #3 * 2 * 1 = 6
                        #4 * 3 * 2 = 24
                        #5 * 4 * 3 * 2 * 1 = 120
                        
s=input("enter-->") # abc/abcc/hello
mp={}
for i in range(len(s)):
    mp[s[i]]=mp.get(s[i],0)+1
    # print(o)
print(mp)
permutation=fact(len(s))
print(permutation)
for freq in mp.values(): # 1,1,2,1
    print(freq,end=" ")
    permutation=permutation//fact(freq)
print("\n",permutation)
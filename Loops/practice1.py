# find in given number how many of them are positive
# num=[1,-2,3,-4,5,6,-7,-8,9,10]
num=[1,-2,3,-4,5,6,-7,-8,9,10]
cnt=0
for i in num:
    if i>0:
        cnt+=1

print(cnt)

# print the multiplication table for a given number up to 10 ,but skip the fifth iteration
n=10
i=2
for num in range(1,n+1):
    if num==5:
        continue
    print(i,'x',num,'=',num*i)


## print reverse a string
inputstr="riya"
length=len(inputstr)
ansstr=""
for char in range(length-1,-1,-1):
    ansstr+=inputstr[char]
print(ansstr)
# second method
ansstr=""
for char in inputstr:
    ansstr=char+ansstr
print(ansstr)
      
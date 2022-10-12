prices=[7,5,3,9]
i=0
j=1
pro=0
while(j<len(prices)):
    if prices[i]<prices[j]:
        pro=max(pro,prices[j]-prices[i])
    else:
        i=j
    j+=1
print(pro)
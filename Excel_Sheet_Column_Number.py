columnTitle="AC"
i=0
sum=0
while (i<len(columnTitle)):
    sum+= 26*(ord(columnTitle[i])-64)
    i=i+1
print(sum+ord(columnTitle[i])-64)

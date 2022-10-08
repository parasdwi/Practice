# numRows=2
# out=[[1],[1,1]]
# for i in range(numRows-2):
#     out.append([1,1])
#     for j in range(1,i+2):
#         out[i+2].insert(j,out[i+1][j-1]+out[i+1][j])
# print (out)

numRows=2
out=[[1]]
if numRows==1:
    print(out)
for i in range(1,numRows):
    out.append([1])
    for j in range(1,i):
        out[i].append(out[i-1][j-1]+out[i-1][j])
    out[i].append(1)
print(out)

import math
from numpy import *
S= [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
n=4
rootn=int(math.sqrt(n))
row_q=2//rootn
col_q=2//rootn
type(row_q*rootn)
# a=S[row_q*rootn:row_q*rootn+rootn-1 ,[col_q*rootn,col_q*rootn+rootn-1]]
# a=S[1:2 ,[col_q*rootn,col_q*rootn+rootn-1]]

a = S[row_q*rootn:row_q*rootn+rootn,]

print(a)
# slice = S[0:2,0:2]
# print(slice)



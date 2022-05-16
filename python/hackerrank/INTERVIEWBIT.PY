# A = [5,4,3,2,1]
# for i in A:
#     if i%2==1:
#         A.append(i)
# A.sort()
# print(A[0])

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
A = [3,10,-9,8,5]
b =0
for i in A:
    if i==3 or i%5==0:
        b = b+i
print(b)
# return i
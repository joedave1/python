X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[1,8,1],
    [1,7,3],
    [1,1,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)

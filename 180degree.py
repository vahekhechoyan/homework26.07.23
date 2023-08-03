mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat1 = mat[-1][::-1]
mat2 = mat[-2][::-1]
mat3 = mat[-3][::-1]
mat4 = mat[-4][::-1]

ls = list()
ls.append(mat1)
ls.append(mat2)
ls.append(mat3)
ls.append(mat4)
print(ls)



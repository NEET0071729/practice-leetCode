import numpy as np

a = np.array([1 ,2, 3])
b = np.array([[ 1.0, 2.0, 3.0],[ 4.0, 5.0, 6.0]])
print(a)
print(b)

#get dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#change data type
a = np.array([1 ,2, 3], dtype= 'int8')
print(a.dtype)

#get size
print(a.itemsize)

#get number of elements
print(a.size)
print(b.size)

#get total size
print(a.nbytes)

#get element 
print(b[1, -2]) #b[ r, c] both r and c follow same rule as normal python i.e start at 0

#get a specific row
print(b[1,:])

#get column
print(b[:, 1])

b = np.array([[ 1, 2, 3, 4, 5],[ 6, 7, 8, 9, 10]])

#fancy stuff [startindex:endindex:step] endpoint is exclusive
print(b[1, 2::2 ])

#subtitute a column
b[:, 2] = [10, 25]
print(b)

#get element in 3d (go for inside out)
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
b[ :, 0, 0] = 10
print(b)

#initialise a array all zero
b = np.zeros((2, 3 , 3))
print(b)

#all ones initialise with datatype
b = np.ones(( 1, 3, 2), dtype='int8')
print(b)
print(b.dtype)

#anyother number
b = np.full((3, 2), 88)
print(b)

#anyother number(full_like)
b = np.full_like( b, 99)
print(b)

#initialise a array of random decimal numbers between 0 and 1
#wierdly you doun't pass a tuple but direct shape
b = np.random.rand( 2, 3)
print(b)

#filling a known shape with random decimal
b = np.random.random_sample(b.shape)
print(b)

#initialize a array of random integer
# np.random.randint(start:end, size= ( 2, 3))
#end is exclusive
b = np.random.randint(7, size= ( 2, 3))
print(b)

#the identity matrix
b = np.identity(4)
print(b)

#repeat an array
arr = np.array([[ 1, 2, 3]])
re = np.repeat( arr, 3, axis= 0)
print(re)

#exercise
b = np.ones((5,5), dtype='int8')
b[1:4, 1:4] = 0
b[ 2, 2] = 9
print(b)

#Beware a copy
a = np.array([ 1, 2, 3])
b = a
b[0] = 10 #a[0] will become 10 also
#So we uae a copy function
a = np.array([ 1, 2, 3])
b = a.copy()
b[0] = 10
print(a)

###Mathematics
a = np.array([ 7, 8, 9, 10])
b = a/2
print(b)

# can add two arrays
b = np.array([ 1, 1, 1, 1])
print(a + b)

#take sin of all the value
b = np.sin(a)


#linear algebra
a = np.ones(( 2, 3))
print(a)

b = np.full(( 3, 2), 2)
print(b)

print(np.matmul(a, b))

#find the determinant of a matrix
c = np.identity(3)
print(np.linalg.det(c))
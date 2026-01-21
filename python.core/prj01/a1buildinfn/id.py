i = [1, 3, 5]
j = [1, 3, 5]
k = [1, 3, 5]
l = [1, 3, 7]
m = [1.0, 3.0, 5.0]
n = i
print("i datatype:", type(i), "i value:", i, "i address:", id(i))
print("j datatype:", type(j), "j value:", j, "i address:", id(j))
print("k datatype:", type(k), "k value:", k, "i address:", id(k))
print("l datatype:", type(l), "l value:", l, "i address:", id(l))
print("m datatype:", type(m), "m value:", m, "i address:", id(m))
print("n datatype:", type(n), "n value:", n, "i address:", id(n))
n[1] = 30
print("i datatype:", type(i), "i value:", i, "i address:", id(i))
print("n datatype:", type(n), "n value:", n, "i address:", id(n))
print(i == n)
'''
i datatype: <class 'list'> i value: [1, 3, 5] i address: 2344512299776
j datatype: <class 'list'> j value: [1, 3, 5] i address: 2344512151744
k datatype: <class 'list'> k value: [1, 3, 5] i address: 2344514826048
l datatype: <class 'list'> l value: [1, 3, 7] i address: 2344512106752
m datatype: <class 'list'> m value: [1.0, 3.0, 5.0] i address: 2344514819008
n datatype: <class 'list'> n value: [1, 3, 5] i address: 2344512299776
i datatype: <class 'list'> i value: [1, 30, 5] i address: 2344512299776
n datatype: <class 'list'> n value: [1, 30, 5] i address: 2344512299776
True
'''
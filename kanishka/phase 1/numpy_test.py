import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)
np2 = np.arange(10)
print(np2)
np3 = np.arange(0,2,10)
print(np3)
np4 = np.zeros(10)
print(np4)
np5 = np.zeros((2,10))
print(np5)
np6 = np.full((10),4)
print(np6)
np7 = np.full((2,10),7)
print(np7)
my_list = [1,2,3,4,5,6,7]
np8 = np.array(my_list)
print(np8)
# slicing numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])
# return 2,3,4,5
print(np1[1:5])
# return from something till the end of the array
print(np1[3:])
#return negative slices
print(np1[])
np9 = np.array(my_list)
print(np9)
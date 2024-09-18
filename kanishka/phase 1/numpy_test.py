import numpy as np
#np1 = np.array([1,2,3,4,5])
#create a view
#np2 = np1.view()
#print(f'original NP1{np1}')
#print(f'original NP2{np2}')
#np1[0] = 66
#np2[2] = 42
#print(f'changed NP1{np1}')
#print(f'original NP2{np2}')
#create a copy
#np2 = np1.copy()
#print(f'original NP1{np1}')
#print(f'original NP2{np2}')
#np1[0] = 66
#print(f'changed NP1{np1}')
#print(f'original NP2{np2}')

#create a 1D array and get shape
#np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#print(np1)
#print(np1.shape)
#np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
#print(np2)
#print(np2.shape)
#reshape 3D array
#np3 = np1.reshape(2,3,2)
#print(np3)
#print(np3.shape)
#flatten to 1D
#np4 = np3.reshape(-1)
#print(np4)
#print(np4.shape)

#np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#for x in np1:
 #  print(x)
#2D array
#np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#for x in np2:
 #   print(x)
#for y in x:
   # print(y)
#3D array
#np3 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#for x in np3:
    #print(x) 
 #for y in x:
  #print(y)
  #for z in y:
   #  print(z)
   #use np.nditer()
#for x in np.nditer(np3):
   #  print(x)  
   
 #sorting numpy arrays
 
 #numeric
#np1 = np.array([6,5,3,7,8])
#print(np1)
#print(np.sort(np1))

#alphabetic
#np2 = np.array(["kanishka","John","Array"])
#print(np2)
#print(np.sort(np2))

#searching 
#np1 = np.array([1,2,3,4,5,6,7,8,9,10,4])
#x = np.where(np1 == 4)
#print(np1)
#print(x)
#print(x[0])
#print(np1[x[0]])   
#y = np.where(np1 % 2 != 0)
#print(np1)
#print(y) 
#print(np1[y[0]])

#filtering numpy arrays with boolean index lists
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
#x= [True, True, False, False, False, False, False, False, False, False]
#print(np1)
#print(np1[x])
#filtered = []
#for thing in np1:
#    if thing > 5:
 #       filtered.append(True)
  #  else:
  #      filtered.append(False)
#print(np1)
#print(filtered)
#print(np1[filtered])

#shortcut
filtered = np1 % 2==0
print(np1)
print(filtered)
print(np1[filtered])

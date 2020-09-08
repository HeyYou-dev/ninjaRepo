""" random int taking as input """

import   random
n = int(input('Enter size of array'))

arr=[]

for i in range(n):

    r3 = random.randint(-5, 5)

    arr.append(r3)

"""Login to find maximum sum of subarray goes here"""

#assume maximumn subarray sum is 0

print(arr)

best = 0

for i in range(0, len(arr)):
    
    suma=0
    for k in range(i, len(arr)):
                
        suma = max(arr[k], suma
        +arr[k])

        best = max(best, suma)


print(best)

         
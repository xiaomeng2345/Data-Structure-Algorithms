from time import time #import time function from time mudule

def computer_average(n):
    '''perform n appends to an empty list and return average time elapsed'''
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start)/n

for k in range(5,10):
    n = 10**k
    print(computer_average(n))

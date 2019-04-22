import  ctypes

class DynamicArray:
    '''A dynamic array class akin to a simplified Python list'''
    def __init__(self):
        '''creat an empty array'''
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # low level array

    def __len__(self):
        '''return number of elements stored in the array'''
        return  self._n

    def __getitem__(self, k):
        '''return element ant index k'''
        if not 0<=k<self._n:
            raise IndexError('invalid index')
        return self._A[k] #retrieve from array

    def append(self,obj):
        '''add object to end of array'''
        if self._n == self._capacity:
            self.resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self,c): #nonpublic utitity
        '''Resize internal array to capacity c'''
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        '''return new array with capacity c'''
        return(c*ctypes.py_object)()





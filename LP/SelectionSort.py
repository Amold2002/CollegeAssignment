def selectionSort(array,size):
    for i in range(size):
        index = i
        for j in range(i+1,size):
            if(array[j]< array[index]):
                index = j
            value = array[i]
            array[i]=array[index]
            array[index]=value

arr = [25,67,32,45,12,90,6]
size = len(arr)
selectionSort(arr,size)
print(arr)


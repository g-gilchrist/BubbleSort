#==============================================================================
#    Author: Grant Gilchrist
#    Problem: BubbleSort
#==============================================================================

# create a bubbleSort function and a swapElement function
# I then called the bubble sort functiont that accepts the list and the list length
# By running the list through two four loops it checks each variable against all the other variables in the list.
# The variables are then accepted by the swapElemnts function. if the variable is less than the next variable the variables swap locations in the list
# Finally I call the PrintSorted function where I print a list witht the original order and the new sorted list.

AlphaList=[3,44,45,10,15,16,9,11]
OmegaList=[3,44,45,10,15,16,9,11]
length = len(OmegaList)

def main():          
    bubbleSort(list,length)
    PrintSorted()

def bubbleSort(OmegaList,length):                 
    for index1 in range(length):
        for index2 in range(length-1) :
            swapElement(index1,index2)
        
def swapElement(x,y):
    if OmegaList[x] < OmegaList[y]:
        OmegaList[x], OmegaList[y] = OmegaList[y], OmegaList[x]

def PrintSorted():    
    print('\n'f'Unsorted List: {AlphaList}')
    print(f'  Sorted List: {OmegaList}')
        
main()
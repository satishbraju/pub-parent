def unique(list1):
  
    # initialize a null list
    unique_list = []
  
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list)
    return(unique_list)
  
# driver code
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
a = unique(list1)
#print(a)
  
  
#list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
#print("\nthe unique values from 2nd list is")
#unique(list2)
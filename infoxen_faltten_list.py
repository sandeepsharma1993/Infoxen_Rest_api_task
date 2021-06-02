#1. Write a program to flatten the nested list.
#Input:- [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
#Output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


lists= [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]

flat_list = []

def flatten_list(lists):
    for element in lists:
        if type(element) == list:
            flatten_list(element)
        else:
            flat_list.append(element)

flatten_list(lists)

print('Original List',lists)
print('flat List',flat_list)

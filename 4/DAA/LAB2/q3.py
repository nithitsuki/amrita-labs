#3. Given ‘m’ sorted lists/arrays, each containing ‘n’ elements, print them efficiently in sorted order. For Example: 
[10, 20, 30, 40] 
[15, 25, 35, 45] 
[27, 29, 37, 48] 
[31, 34, 40, 51] 
[19, 18, 22, 28] 


def merge_sorted_lists(lists):
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    merged_list.sort()
    return merged_list

sorted_lists = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [31, 34, 40, 51],
    [19, 18, 22, 28]
]
result = merge_sorted_lists(sorted_lists)   

print(result)


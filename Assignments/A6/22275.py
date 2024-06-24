#22275:二叉搜索树的遍历

def binary_search_tree(l:list):
    if len(l) <= 1:
        return l
    for index in range(1, len(l)):
        if l[index] > l[0]:
            return binary_search_tree(l[1:index]) + binary_search_tree(l[index:]) + [l[0]]
    else:
        return binary_search_tree(l[1:]) + [l[0]]
    
n = int(input())
print(*binary_search_tree([int(x) for x in input().split()]))

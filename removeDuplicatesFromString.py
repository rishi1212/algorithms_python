def removeDuplicates(string):
    unique=''
    for i in string:
        if i not in unique:
            unique+=i
    return unique

a='geeksforgeeks'
print removeDuplicates(a)

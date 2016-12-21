l = [2, 5, 6, 1, 98, 14]
l = [2, 5, 6, 1, 98, 14, 1,2,3,4,5,3,2,1,2,3,4,4]

def bubble_sort(l):
   print(l)
   temp_l = ''
   for j in range(len(l)):
       for i in range(len(l)-1):
           if l[i] > l[i + 1]:
               temp_l = l[i]
               l[i] = l[i + 1]
               l[i+1] = temp_l
               print(l)



def bubble(l):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaps = True
    return l


def insertion(l):
    if l == []: return []
    new_l = [l[0]]
    for index in range(1, len(l)):
        for place in range(len(new_l)):
            if new_l[place] > l[index]:
                new_l.insert(place, l[index])
                break
        else:
            new_l.append(l[index])
    return new_l


def selection(l):
    new_l = []
    while l:
        m = min(l)
        new_l.append(m)
        l.remove(m)
    return new_l


def selection(l):
    for i in range(len(l)):
        #m = min(enumerate(l[i:]), key=lambda x:x[1])[0] + i
        m = l.index(min(l[i:]))
        l[i], l[m] = l[m], l[i]




def merge(l):
    if len(l) < 2:
        return l
    
    midpoint = len(l)//2
    left = merge(l[:midpoint])
    right = merge(l[midpoint:])
    
    new_l = []
    
    while left and right:
        if left[0] > right[0]:
            new_l.append(right.pop(0))
        else:
            new_l.append(left.pop(0))
    
    return new_l + left + right



def merge(l):
    if len(l) < 2: return l
    
    lhs = merge(l[len(l)//2:])
    rhs = merge(l[:len(l)//2])
    new_l = []
    while lhs and rhs:
        if lhs[0] < rhs[0]:
            new_l.append(lhs.pop(0))
        else:
            new_l.append(rhs.pop(0))
    return new_l + lhs + rhs

























import random

l = list(range(30))
random.shuffle(l)
print(bubble(l))

l = list(range(30))
random.shuffle(l)
print(insertion(l))

l = list(range(30))
random.shuffle(l)
selection(l)
print(l)

l = list(range(30))
random.shuffle(l)
print(merge(l))

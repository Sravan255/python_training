# list
s=[4,3,2,1]
print(s)
# append: appends single element at the end of list
s.append(5)
print(s)
s.append([1,2,3])
print(s)
#extend 
b=[1,2,3,4]
b.extend([1,2,3])
print(b)

#inset #inserts element at the specified index
#  0,1,2,3 only consiter in inset
l=[2,0,0,2]
l.insert(2, 's')
print(l)

# pop : removes element at the specified index
s=[1,2,3]
print(s)
a=l.pop(3)
print(a)
# remove ; remove the first occurence of the elemnt
r=[3,4,5,4,5]
r.remove(4)
print(r)
# clear ;remove all elements from the list and list becomes empty
s=[1,3,4,6,7,8,9]
s.clear()
print(s)

#reverse: reverse the original list
l=[9,8,7,6,5]
l.reverse()
print(l)

#sort ;sort is the original list
k=[3,4,2,1,5]
k.sort()
print(k)
k=[5,1,3,2,4]
k.sort(reverse=True)
print(k)
#count ;count the number of time element has appeared in the list
l=[3,4,2,3,1,]
print(l.count(3))

#index; returns the index of the element from the give index
w=[1,2,4,3,7,8]
print(w.index(4))
print(w.index(4,2))





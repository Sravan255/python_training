#SET METHODS
#create a empty dict and print its type
k={}
print(type(k))
#create a empty set and print its type
k=set()
print(type(k))
#add 5 non-sequences and 5 sequences to that set with add method
k.add(2002)
k.add(20.02)
k.add(20+20j)
k.add('True')
k.add('none type')
k.add('sravan')
k.add(range(1,2,3))
#k.add({1,2,3})
k.add((4,5,6))
#k.add({1:2 , 2:3}) #error,m set will not allow dict
print(k)
#add 5 non-sequences and 5 sequences with update method
k=set()
#k.update(2002)   # cannot add non-sequences int with update
#k.update(20.02)   # cannot add non-sequences float with update
#k.update(20+20j)   # cannot add non-sequences complex with update
#k.update('True')   # cannot add non-sequences boole with update
#k.update('none type')  # cannot add non-sequences none with update
k.update('sravan')
k.update(range(1,2,3))
k.update({1,2,3})
k.update((4,5,6))
k.update({1:2 , 2:3}) 
print(k)

#print a set and remove first element from that set

print(k)
k.pop()
print(k)
#remove one existing and one non-existing element from that set
k.remove('a')
print(k)

#discard one existing and one non-existing element from that set
k.discard('r')
k.discard('w')
print(k)
#remove all elements from the set

#create a set {1,2,3,4}, a list [3,4,5,6]. 
s={1,2,3,4}
l={3,4,5,6}

#write union of set and list
print(s.union(l))
#write intersection of set and list
print(s.intersection(l))
#write difference of set and list
print(s.difference(l))
#write symmetric difference of set and list
print(s.symmetric_difference(l))
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
s1={1,2,3,4}
s2={3,4,5,6}
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)


#DICT METHODS
#create a empty dict
d={}

#update dict with another dict
d.update({1:'a', 2:'3'})
#update dict with another list
d.update([[1, 'a'],[2, 'b'],[3,'c']])
#update dict with another tuple
d.update(((1, 'd'),(2,'e'),(3,'f')))
#update dict with another set
d.update({(1, 'k'),(2, 'j'),(3,'d')})
#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
#remove the pair with key 4
d.pop(4)

#remove the pair with key 100
#d.pop (100)  #error 100 is not present
#remove the pair with key 100 if not there return 'z'
d.pop(100,'z')
#remove the last pair
d.popitem()
#remove all elements from the dict
d.clear()
print(d)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
#get the value of key 4
print(d.get(4))
#get the value of key 100
#print(d.get(100)
#get the value of key 100, if key is not present get 'z'
print(d.get(100,'z'))

#get the value of key 4 with setdefault
print(d.setdefault(4))
#get the value of key 100 with setdefault
print(d.setdefault(100))
#get the value of key 100 with setdefault, if key is not there add 100 with 'z'
print(d.setdefault(101,'z'))
#get all keys of dict and print its type
a=d.keys()
print(type(a))
#get all values in dict and print its type
b=d.values()
print(type(b))
#get all items in dict and print its type
c=d.items
print(type(c))




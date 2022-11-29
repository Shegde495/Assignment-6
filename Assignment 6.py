#1. Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
s={'a':4,'b':5,'c':6,'d':1}
a=sorted(s.items(),key=operator.itemgetter(1),reverse=False)
print("Ascending",dict(a))
d=sorted(s.items(),key=operator.itemgetter(1),reverse=True)
print("Descending",dict(d))


#2. Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
s={0:10,1:20}
k={2:30}
s.update(k)
print(s)

#3. Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#4. Write a Python script to check if a given key already exists in a dictionary.
s={'a':1,'b':4,'c':7,'d':9}
k=input("Enter the search key element : ")
if k in s.keys():
    print("Key is present in the given dictionary")
else:
    print("Key not present in the given dictionary")


#5. Write a Python program to iterate over dictionaries using for loops.
s={'a':1,'b':4,'c':7,'d':9}
for k,v in s.items():
    print(k,v)


#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
s=int(input())
d=dict()
for i in range(1,s+1):
    d[i]=i**2
print(d)

#7. Write a Python script to merge two Python dictionaries.
def merge(a,b):
    a.update(b)
    return a
d1={'a':1,'b':4,'c':7,'d':9}
d2={'e':1,'f':4,'g':7,'h':9}
print(merge(d1,d2))

#8.  Write a Python program to sum all the items in a dictionary.
s={'a':1,'b':4,'c':7,'d':9}
print(sum(s.values()))


#9. Write a Python program to multiply all the items in a dictionary.
s={'a':2,'b':4,'c':3,'d':2}
c=1
for i in s.values():
    c=c*i
print(c)

#10. Write a Python program to remove a key from a dictionary.
s={'a':2,'b':4,'c':3,'d':2}
s.pop('a')
print(s)

#11. Write a Python program to sort a dictionary by key.
s={'d':2,'a':4,'b':3,'c':2}
for i in sorted(dict(s)):
    print((i,s[i]),end='')

#12. Write a Python program to get the maximum and minimum value in a dictionary.
s={'d':2,'a':4,'b':3,'c':7,'h':10,'k':5}
li=[]
for i in s.values():
    li.append(i)
print(max(li))
print(min(li))

#13. Write a Python program to remove duplicates from Dictionary.
s={'a':2,'b':4,'c':3,'d':2,'e':10,'f':4}
u=set()
d=dict()
for k,v in s.items():
    if v not in u:
        d[k]=v
        u.add(v)
    else:
        pass
print(d)

#14. Write a Python program to check a dictionary is empty or not.
s=[{},{'a':2,'b':4,'c':3,'d':2,'e':10,'f':4}]
for i in s:
    if len(i)> 0 :
        print("dictionary is not empty")
    else:
        print("Empty dictionary")

#15. Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
counter={}
li=list(d2.keys())
ki=list(d1.keys())
for k in d2.keys():
    if k in ki:
        counter[k]=d1[k]+d2[k]
    else:
        counter[k]=d2[k]
for i in d1.keys():
    if i not in li:
        counter[i]=d1[i]
print(counter)

#16. Write a Python program to find the highest 3 values in a dictionary.
s={'a':2,'b':6,'c':3,'d':2,'e':10,'f':4}
li=[]
for i in s.values():
    li.append(i)
k=sorted(li,reverse=True)
for i in range(3):
    print("The",i+1, "highest value is",k[i])

#17. Write a Python program to match key values in two dictionaries.
#Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
#Expected output: key1: 1 is present in both x and y
x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
li=list(x.items())
ki=list(y.items())
for i in li:
    if i in ki:
        print((i),"is present in both X and Y")

#18. Write a Python program to check if all dictionaries in a list are empty or not.
#Sample list : [{},{},{}]
#Return value : True
#Sample list : [{1,2},{},{}]
def check(li):
    for i in li:
        if len(i)==0:
            pass
        else:
            return 'False'
    return "True"
li1=[{},{},{}]
li2=[{1,2},{},{}]
print(check(li1))
print(check(li2))

#19. Write a Python program to remove duplicates from a list of lists.
#Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#New List : [[10, 20], [30, 56, 25], [33], [40]]
s=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
li=[]
for i in s:
    if i not in li:
        li.append(i)
print(sorted(li))

#20. Write a Python program to extend a list without append.
#Sample data: [10, 20, 30]
#[40, 50, 60]
#Expected output : [40, 50, 60, 10, 20, 30]
li1=[10, 20, 30]
li2=[40, 50, 60]
print(li2+li1)



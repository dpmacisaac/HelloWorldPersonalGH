import hello_world

#warmup
for i in range(2,40,2):
    print(i, end=",")
print(i+2)

#Lists
#like resizeable array (mutable)
fibs = [1,1,2,3,5,8]
print(fibs, type(fibs))

#for loop demos
for value in fibs:
    print(value)
for i in range(len(fibs)):
    print(i,":", fibs[i])
for i, value in enumerate(fibs):
    print(i, ":", value)


#negative indexes
print(fibs[-1])

#built in list functions
#len(), sum(),min(),max(),sorted(), etc.
#sorted() returns a copy of the list arguemnt sorted
print(sorted(fibs,reverse=True))
print(fibs)


#method is a function invoked by a class
#a function is passed a value in parameters and returns 
#list methods
#recall: method invocation syntax <object name>.<method name>()
print(fibs.index(5))
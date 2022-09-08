import csv
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
fibs.append(13)
print(fibs)
fibs.pop(-1)
print(fibs)
fibs.remove(5)
print(fibs)

fibs.sort(reverse=True)
print(fibs)

#nested lists (AKA 2D list AKA tables)
matrix = [[0,1,2],[3,4,5]]
print(matrix)

#tasks: define/call a funtion called pretty_print(table)
#that prints out a table in a nice 2D grid like format

def pretty_print(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()

pretty_print(matrix)

#File IO
print("\n------------------FILE/IO------------------\n")

def convert_to_numeric(values):
    for i in range(len(values)):
        try:
            numeric_val = float(values[i])
            #success
            values[i] = numeric_val
        except ValueError as e:
            print(e)
    return values

#CSV
def read_table(filename):
    table = []
    #1. open 
    infile = open(filename, "r")

    #2. read/write (process)
    # we can write our own CSV parsing algorithm (Bonus PA1)
    # or use the csv module (standard library)
    reader = csv.reader(infile)
    for row in reader:
        print(row)
        #we need to conver numeric values from string to numeric type
        row = convert_to_numeric(row)

        table.append(row)
    #3 close
    infile.close()

    return table

def write_table(table, filename):
    outfile = open(filename, "w")

    writer = csv.writer(outfile)
    writer.writerows(table)
    
    outfile.close()
    pass

table = read_table("data.csv")
print(table)

write_table(table, "data_copy.csv")

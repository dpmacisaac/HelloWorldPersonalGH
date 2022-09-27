import numpy as np

def get_column(table, header, col_name):
    index = header.index(col_name)
    new_table = []
    for row in table:
        new_table.append(row[index])
    return new_table

def get_frequencies (table, header, col_name):
    col = get_column(table,header,col_name)
    col.sort() # inplace_sort

    values = [] #75,76,77
    count = [] #2,1,1

    for value in col:
        if value not in values:
            values.append(value)
            count.append(1)
        else:
            count[-1] += 1

    return values,count
    
def dummy_def(x):
    print(str(x * 19),"dummies")
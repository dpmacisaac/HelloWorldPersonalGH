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


def group_by(table, header, group_by_col_name):
    group_by_col = get_column(table, header, group_by_col_name)
    group_by_col_index = header.index(group_by_col_name)

    group_names = sorted(list(set(group_by_col))) # eg [75,76,77]

    group_subtables = [[] for __ in group_names] # create list of len(groupnames) empty lists

    for row in table:
        group_by_val = row[group_by_col_index]
        subtable_index = group_names.index(group_by_val)
        group_subtables[subtable_index].append(row)

    return group_names, group_subtables

def comput_equal_width_cutoffs(values,num_bins):
    values_range = max(values) - min(values)
    bin_width = values_range/num_bins
    cutoffs = list(np.arrange(min(values),max(values), bin_width))
    cutoffs.append(max(values))
    cutoffs = [round(cutoff,2) for cutoff in cutoffs]
    return cutoffs

def compute_slope_intercept(x,y):
    meanx = np.mean(x)
    meany = np.mean(y)

    m = sum([(x[i]-meanx)*(y[i]-meany) for i in range(len(x))])/ \
        sum([(x[i]-meanx)** 2 for i in range(len(x))])
    # y = mx + b => b = y-mx
    b = meany-m* meanx
    return m,b

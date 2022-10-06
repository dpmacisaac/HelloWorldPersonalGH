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
    

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
                  ["toyota corolla", 75, 2711],
                  ["ford pinto", 76, 3025],
                  ["toyota corolla", 77, 2789]]
    msrps = get_column(msrp_table, header, "MSRP")
    print(msrps)

    modelyear_values, model_year_count = get_frequencies(msrp_table, header, "ModelYear")
    print(modelyear_values,model_year_count)


    msrp_mean = sum(msrps)/len(msrps)
    print("mean:", msrp_mean)

    msrp_mid = (min(msrps)+max(msrps))/2
    print("mid:", msrp_mid)

    squared_mean_deviations = [(msrp-msrp_mean) ** 2 for msrp in msrps]
    variance = sum(squared_mean_deviations)/len(squared_mean_deviations)
    standard_dev = variance ** (1/2)
    print("standar_dev:", standard_dev)


    assert np.isclose(standard_dev,np.std(msrps))
    

if __name__ == "__main__":
    main()
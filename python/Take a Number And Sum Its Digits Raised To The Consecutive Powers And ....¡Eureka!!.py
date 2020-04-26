def sum_dig_pow(a, b): 
    my_sum = 0
    my_list = []
    for item in range(a,b+1):
        j = str(item)
        _length = len(j)
        n = 1
        for k in range(0,_length):
            my_sum += pow(int(j[k]),n)
            n += 1
        if item == my_sum:
            my_list.append(item)
        my_sum = 0
    my_list.sort()
    return my_list
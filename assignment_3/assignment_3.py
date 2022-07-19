def list_to_dict(mylist):
    key = []
    value = []
    for i in range(0, len(mylist), 2):
        key = key + [mylist[i]]
    for i in range(1, len(mylist), 2):
        value = value + [mylist[i]]
    dict1 = zip(key, value)
    answer = dict(dict1)
    return answer


input_data = ['a', 1, 'b', 2, 'c', 4, 'd', 5]
print(list_to_dict(input_data))

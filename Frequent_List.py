list = [2, 3, 5, 6, 2, 2, 4, 5, 5, 5]
def most_frequent(list):
    counter = 0
    #num = list[0]

    for i in list:
        curr_frequency = list.count(i)
        if (curr_frequency>counter):
            counter = curr_frequency
            num = i
    return num

print(most_frequent(list))
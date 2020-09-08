def print_upper_words(array, must_start_with):
    for i in range(len(array)):
        for x in must_start_with:
            if array[i][0] is x:
                print(array[i])


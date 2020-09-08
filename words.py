def print_upper_words(list, must_start_with):
    ''' only prints words starting with must_start_with '''
    for i in range(len(list)):
        for x in must_start_with:
            if list[i][0] is x:
                print(list[i])


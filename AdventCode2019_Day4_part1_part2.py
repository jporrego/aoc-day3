

def meets_criteria(item):
    x = False
    item_list = list(str(item))
    item_enumerated = list(enumerate((str(item))))

    for char in item_list:
        if item_list.count(char) == 2:
            x = True
    
    for i, char in item_enumerated:
        try:
            if char > item_enumerated[i+1][1]:
                x = False
        except IndexError:
            pass
    
    return x


possible_passwords = list(filter(meets_criteria, range(356261, 846304)))

print(len(possible_passwords))

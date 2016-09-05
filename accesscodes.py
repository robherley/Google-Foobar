'''

@author: Rob Herley

'''

def answer(x):
    no_pali_list = palindromes(x)
    set_list = no_pali_list[0]
    match_list = set(set_list).intersection(reversedList(set_list))
    num_of_matches = len(list(match_list))
    return (len(set_list) - num_of_matches / 2) + no_pali_list[1]


def reversedList(x):
    new_list = []
    for word in x:
        new_list += [''.join(reversed(word))]
    return new_list

def palindromes(x):
    set_list = list(set(x))
    no_pali = []
    pali_count = 0
    for word in set_list:
        if word == ''.join(reversed(word)):
            pali_count += 1
        else:
            no_pali += [word]
    return [no_pali, pali_count]

L = ['x', 'y', 'xy', 'yy', '', 'yx']
print answer(L)
print palindromes(L)
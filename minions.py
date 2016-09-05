'''

@author: Rob Herley

'''
def answer(minions):
    count = -1
    minion_list = []
    for list_item in minions:
        count += 1
        minion_list += [[(float(list_item[0]))/((float(list_item[1]))/list_item[2]), count]]
    fixed_list = sorted(minion_list, key = lambda minion: minion[0])
    return output(fixed_list)

def output(list):
    final_list = []
    for item in list:
        final_list += [item[1]]
    return final_list

# print answer([[5, 1, 5], [10, 1, 2]])
# print answer([[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]])

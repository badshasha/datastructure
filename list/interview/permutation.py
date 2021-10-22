
# what is permutation
string_one = "lion is black"
string_two = "lion is black"


def permutano(list1 , list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

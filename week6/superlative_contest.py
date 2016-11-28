
def score(element):
    return sum([ord(char) for char in element])
 

def most(the_list):
    """ return the element of the_list that has the largest of something """
    #Do this with a loop.
    current_max_score = float("-inf")
    max_items = []
    for item in the_list:
        if score(item) > current_max_score:
            current_max_score = score(item)
            max_items = [item]

        elif score(item) == current_max_score:
            max_items.append(item)

    return max_items


def most(the_list):
    #return sorted(the_list, key=score)[-1]
    return max([(score(item), item) for item in the_list])[1]

list_of_words = ["hi", "mom", "how", "are", "you", "care", "a", "acre", "race"]

print(most(list_of_words))



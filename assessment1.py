
def is_hometown(town):

    if town.lower() == "oakland":
        return True
    else:
        return False


def full_name(first, last):
    
    return first + " " + last


def hometown_greeting(town, first, last):

    if is_hometown(town) is True:
        print "Hi" + " " + full_name(first, last) + ", " + "we're from the same place!"
    elif is_hometown(town) is False:
        print "Hi" + " " + full_name(first, last) + ", " + "where are you from?"

hometown_greeting("Oakland", "Allie", "P")

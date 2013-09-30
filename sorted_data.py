
from sys import argv


def sorted_data():

    script, filename = argv

    rest_rate = {}
    f = open(filename)

    # reading filename line by line until last line.
    # splitting each line by ":" so first part = key and second = value
    while True: 
        text = f.readline()
        if text == "":
            break
        words = text.split(":")
        rest_rate[words[0]] = words[1].strip()
     
    # creates list with keys in dictionary
    # sort through the list 
    # print out key and associated key value 
    keylist = rest_rate.keys()
    keylist.sort()
    for key in keylist:
        print "Restaurant \'%s\' is rated at %s." % (key, rest_rate[key])

    f.close()

sorted_data()
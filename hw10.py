import re # Regular Expression library. Used by read_list_from_file().


def bubble_sort(input_list):
    # Write the code for this function as described in
    # the presentation. Don't just return 0, but instead
    # return the total number of comparisons used.

    number_iter = 0
    exchanges = True
    passnum = input_list.__len__() - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            number_iter = number_iter + 1
            if input_list[i] > input_list[i + 1]:
                exchanges = True
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp
        passnum = passnum - 1

    '''sorted_list = False
    list_length = input_list.__len__()
    assert isinstance(list_length, object)
    was_sorted = False
    while was_sorted == False:
        loop_index = 0
        while ( loop_index < (list_length -1 )) :
           was_sorted = True
           if input_list[loop_index] > input_list[loop_index+1]:
                tmp_hlder = input_list[loop_index]
                input_list[loop_index] = input_list[loop_index+1]
                input_list[loop_index+1] = tmp_hlder
                was_sorted = False
                loop_index += 1
                continue
           else:
                loop_index += 1
                continue'''

    print 'The list length is {}'.format(input_list.__len__())
    return number_iter




###################################################
####### Do not change anything below here!! #######
####### (except possibly for testing, but   #######
####### then change it back before submitting. ####
###################################################
def is_sorted(L):
    # Check whether the list L is sorted in ascending order.
    n = len(L)
    i = 0
    while (i<n-1):
        if (L[i] > L[i+1]):
            return False
        i += 1
    return True

def read_list_from_file(filename):
    L = []
    try:
        F = open(filename, "r")
    except:
        print "Could not open file '%s'!" % (filename)
        return []
    for line in F:  # Read the file one line at a time.
        # Now split the line into words and concatenate those
        # onto the list L.
        wordlist = line.split()
        for word in wordlist:
            w = re.sub(r'[^a-zA-Z]','',word) # Remove non-alphabetic char's
            if (len(w)>0):
                L.append(w) # Only append if what's left is nonempty.
        
    return L

List = read_list_from_file('input.txt')
size = len(List)
print "Read a list of size = %d" % (size)

numops = bubble_sort(List)
if (is_sorted(List) and len(List)==size):
    print "bubble_sort() worked - the list IS sorted now."
    print "It used %d comparisons." % (numops)
else:
    if is_sorted(List)==False:
        print "bubble_sort() FAILED - the list is NOT sorted now."
    else:
        print "bubble_sort() changed the list. It now has size %d." % len(List)

# If it's not working and you cannot figure out why, make your
# own input.txt file with only a dozen or so words and print it
# out to help figure out what's going wrong. If you do so, just comment
# this line out again before you submit the assignment.
#print List

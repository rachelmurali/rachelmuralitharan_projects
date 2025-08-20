
def bwt(line):
    # create the first version of the string by adding $ and ^
    prev = "$" + str(line) + "^"
    rots = []   # initialize the string with the rotations
    rots.append(prev)
            
    # loop through and move the last character to the front of the previous rotation, saving that new string as the previous string
    for i in range(len(line) + 1):
        rot = prev[-1] + prev[:-1]
        prev = rot
        rots.append(rot)
            
    rots.sort()

    # get the elements of the last column to form the bwt transformed string, return the output
    final = ""
    for r in rots:
        final = final + r[-1]
    return final

def run_length_encoding(line):
    seq = ""
    for i in range(len(line)):
        if(i == 0):
            previous = line[0]    # in the first run of the loop, initialize the previous character as the first character and the count of that character to be 1
            count = 1
        elif(previous == line[i]):
            count += 1         # if the current character is the same as the previous, increase the occurance count
        elif(line[i] != previous):
            seq = seq + str(count) + previous  # if the previous is not equal to the current character and the occurance rate is greater than 1, store the count and character to seq
            previous = line[i]         # reset the previous character to the current character and the count to 1
            count = 1
    seq = seq + str(count) + previous
    return seq

def ibwt(line):
    n = len(line)
    table = [''] * n  # Initialize the table with empty strings
    
    # Perform the inverse BWT process by updating the table iteratively
    for _ in range(n):
        new_table = []  # Temporary list to store the new rows
        
        # Prepend the BWT string to each row in the table
        for i in range(n):
            new_table.append(line[i] + table[i])
        
        # Sort the new table
        table = sorted(new_table)

    # find the sorted string by finding where the final character is ^ and then return the string with no ^ or $
    for row in table:
        if (row[-1] == '^'):
            final = row[1:len(row)-1]
            return final
        else:
            return 'string given not in bwt format'   # returns this if ^ character not found
    

# read the bwt file, put the lines in a list, and close the file
f1 = open('/work2/07475/vagheesh/stampede2/forOthers/forBIO321G/bwt.txt', 'r')
lines1 = [line.strip() for line in f1]
f1.close()

# read the ibwt file, put the lines in a list, and close the file
f2 = open('/work2/07475/vagheesh/stampede2/forOthers/forBIO321G/ibwt.txt', 'r')
lines2 = [line.strip() for line in f2]
f2.close()

# run a loop the execute the code based on which file is longer

# if the bwt file is longer
if(len(lines1) >= len(lines2)):
    c = 0
    # display all 4 lines for the length of the ibwt file
    for i in range(len(lines2)):
        print(bwt(lines1[i]))
        transform = bwt(lines1[i])
        print(run_length_encoding(lines1[i]))
        print(run_length_encoding(transform))
        print(ibwt(lines2[i]))
        c += 1
    # continue to print the commands for the bwt file until the last line of the bwt file
    while(c < len(lines1)):
        print(bwt(lines1[c]))
        transform = bwt(lines1[c])
        print(run_length_encoding(lines1[c]))
        print(run_length_encoding(transform))
        c += 1
else:
    c = 0
    # display all 4 lines for the length of the bwt file
    for i in range(len(lines1)):
        print(bwt(lines1[i]))
        transform = bwt(lines1[i])
        print(run_length_encoding(lines1[i]))
        print(run_length_encoding(transform))
        print(ibwt(lines2[i]))
        c += 1
    # continue to print the commands for the ibwt file until the last line of the ibwt file
    while(c < len(lines2)):
        print(ibwt(lines2[c]))
        c += 1

    
    

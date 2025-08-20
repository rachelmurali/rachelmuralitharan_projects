

def lecture_hall(p):
    '''Given a class list returns the maximum 
    possible class count to fit in a lecture hall during a day'''

    count = 0
    if(len(classes) == 0):                      # if the class list is 0, return 0
        return 0
    else:
        times = []
        for time in classes:                    # remove the string class titles and only keep the time spans in the list
            times.append(time[1])

        countList = []                          # list to hold the max count of possible classes based on which class is initialy added to the scedule

        # this loop tests each possible class listing combo by altering which class is added to the scedule first
        #(each class is added to the scedule first once)
        for x in range(len(times)):             # loops through all the class timings
            
            previous = times[0]                 # sets the previous time to the first time in the list
            
            prevStart = times[0][0]             # sets first class start time
            prevEnd = times[0][1]               # sets first class end time
            
            times = times[1:]                   # cuts off the first time from the list
            times.append(previous)              # adds the first time to the list at the end
            
            count = lecture_hall_helper(times, 1, prevStart, prevEnd, 0)  # calls helper function
            countList.append(count)                                       # adds count returned from helper function to overall list
            
        return max(countList)                                             # returns max class count from list


def lecture_hall_helper(classes, count, prevStart, prevEnd, num):
    # helper function that recurses through the given combination of classes list and returns the count of classes that can fit in a scedule together
    
    classStart = classes[num][0]                              # gets current class start time
    classEnd = classes[num][1]                                # gets current class end time   

    # base case: if we have looped through all the classes, return count
    if(num == len(classes) - 1):                            
        return count

    # if the class starts after the previous end time, change prevEnd, add to count, and recurse
    if(classStart >= prevEnd):                                
        count += 1
        prevEnd = classEnd 
        return lecture_hall_helper(classes, count, prevStart, prevEnd, num + 1)
    
    # if the class ends before the previous start time, change prevStart, add to count, and recurse
    if(classEnd <= prevStart):                                
        count += 1
        prevStart = classStart
        return lecture_hall_helper(classes, count, prevStart, prevEnd, num + 1)

    # if no conditions are true, recurse without changing any variables except num + 1
    else:                                                     
        return lecture_hall_helper(classes, count, prevStart, prevEnd, num + 1)
    

    

if __name__ == "__main__":
    
    classes = [
        ('class-1', (1, 4)), ('class-2', (3, 5)), 
        ('class-3', (0, 6)), ('class-4', (5, 7)),
        ('class-6', (5, 9)), ('class-7', (6, 10)), 
        ('class-7', (6, 10)), ('class-8', (8, 11)), 
        ('class-9', (8, 12)), ('class-10', (2, 14)),
        ('class-11', (12, 16)), ('class-12', (1, 5)),
        ('class-13', (2, 4)),  ('class-14', (13, 17))]

    print("Maximum possible count is: ", lecture_hall(classes))



class hash_table_with_double_hashing:
    '''
    A Hash Table with Double Hashing
    '''
    # initialize hash Table

    def __init__(self, size):
        
        self.size = size
        
        # initialize table with all elements 0
        self.table = list(None for i in range(self.size))
        
        self.elementCount = 0
        self.comparisons = 0

    def __str__(self):
        ''' Print the hash table '''
        tmp = ''
        for i in range(self.size):
            tmp = tmp + "[ " + str(i) + " , " + str(self.table[i]) + " ] \n"
        
        return tmp
    

    def is_full(self):
        '''  Checks if the hash table is full or not '''
        if self.elementCount == self.size:
            return True
        else:
            return False

    # First hash function
    def h1(self, element):
        return element % self.size

    # Second hash function
    def h2(self, element):
        return 7 - (element % 7)

    

    def double_hashing(self, key):
        '''
        resolve collision by double hashing method
        '''
        pos_found = False   
        i = 1

        # loop to find the slot
        while i <= self.size:
            # find a new slot by probing
            new_slot = (self.h1(key) + i * self.h2(key)) % self.size
            print(self.h1(key) == 0)
            
            # if new slot is empty then break out of loop and return new slot
            if self.table[new_slot] == None:
                pos_found = True
                return pos_found, new_slot
            elif( self.h1(key) == 0 ):
                # if adding a duplicate element will cause errors, return false and tell the user so
                pos_found = False
                return pos_found, None
            else:
                # If the slot is not empty increment the attempt counter i
                i += 1
                
        return pos_found, new_slot




    def insert(self, key):
        ''' inserts a data item into the hash table '''

        # checking if the table is full
        if self.is_full():
            print("Hash Table Full")
            return False

        pos_found = False

        position = self.h1(key)

        # checking if the position is empty
        if self.table[position] == None:
            # We found an empty slot, store the element there
            self.table[position] = key
            self.elementCount += 1
            pos_found = True            # sets pos_found to true if added      

        # If collision occured
        else:
            while not pos_found:
                pos_found, position = self.double_hashing(key)
                if pos_found:
                    self.table[position] = key
                    self.elementCount += 1
                    pos_found = True    # sets pos_found to true if added
                elif(self.h1(key) == 0):    # makes sure no endless loop of searching will occur by checking if the double hash calculation will always be 0
                    pos_found = False
                    return pos_found        

        return pos_found

    def search(self, key):
        # takes in a key and returns a list of all the indexes that key is found in the hash table
        
        slot = self.h1(key)      
        index = []
        
        if(self.table[slot] == key):              # checks if key is in the first possible position it could be
            index.append(slot)
            
        i = 1
        new_slot = (self.h1(key) + i * self.h2(key)) % self.size # keeps checking possible positions with the double hash formula to get all occurances of key

        while (new_slot != slot):                  # loop stops when loop has passed through all positions of the hash once

            if(self.table[new_slot] == key):       # if an occurance of key was found, return that occurance
                index.append(new_slot)
            i += 1
            new_slot = (self.h1(key) + i * self.h2(key)) % self.size 

            if(new_slot == slot):                  # breaks when loop has checked every index of hash once
                break
            
        if(len(index) == 0):
            return False                           # returns False if no occurance of key was found
        return index


if __name__ == '__main__':
    
    table_size = 7
    hash_table = hash_table_with_double_hashing(table_size)
    count = 0

    print("You have a hash table of size 7. Fill the table with integers.\n")

    while (count < 7):                                   # allows user to add valid inputs into hash table until table is filled
        num = input("Enter the number you want to add to the hash table: ")
        try:                                             # accounts for user entering something other than an int
            num = int(num)
            if(hash_table.h1(num) == 0):
                pos_found = hash_table.insert(num)
                if(pos_found == False):                  # makes sure numbers where the hash function can not find an appropriate index are not added
                    print("As self.h1(key) is 0, and the index 0 is occupied, a proper index cannot be found. Please chose another number")
                else:
                    count += 1
            else:
                num = int(num)
                hash_table.insert(num)                   # inserts to hash 
                count += 1
        except:                                          # accounts for user entering something other than an int
            print("\nInvalid Input.\n")

        print("\nThis is your table.")
        print(hash_table)
        

    print("\nNow, enter the element you wish to find in the list. All the indexes with the key will be printed if the item is in the list.\n")
    print("If you have finished finding elements enter stop. If false is printed as a response, that means the element you entered is not in the table.")
    selection = 0
    
    while(selection != "stop"):                # allows user to get indexes of values in the hash until they chose to exit by entering stop
        key = input("\nEnter the number you wish to find in the hash table: ")
        if(key == 'stop'):
            break
        try:
            key = int(key)
            slot = hash_table.search(key)      # calls search function and prints results
            if(slot == False):
                print("index found:", slot)
            else:
                for i in slot:
                    print("index found:", i)
        except:                                # accounts for user entering something other than an int                
           print("\nInvalid input.\n")
            
    print("\nThank you for searching your hash table. Goodbye!")


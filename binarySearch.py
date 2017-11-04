class binarySearch(list):
    #typo in the test case - class name should be CamelCase
    """Binary Search Implementation code

    """
    def __init__(self, max_list, step):
        self.max_list = max_list
        self.step = step

        if max_list in self.toTwenty():
            self.extend(self.toTwenty())
        elif max_list in self.toForty():
            self.extend(self.toForty())
        elif max_list in self.ten_to_thousand():
            self.extend(self.ten_to_thousand())


        #a variable to store the length of the list to Search
        self.length = len(self)

    #return range(1,21)
    def toTwenty(self):
        return range(self.step, (self.max_list * self.step)+1, self.step)

    #return range(2, 41, 2)
    def toForty(self):
        return range(self.step, (self.max_list * self.step)+1, self.step)

    #return range(10, 1001, 10)
    def ten_to_thousand(self):
        return range(self.step, (self.max_list * self.step)+1, self.step)

    #search method to Implement the searching logic
    def search(self, item):
        first = 0
        last = self.length - 1
        found = False
        index = 0
        counter = 0

        if item == self[first]:
            index = first
            found = True
        elif item == self[last]:
            index = last
            found = True
        elif item not in self:
            found = True
            index = -1

        while first <= last and not found:
            midpoint = (first + last)//2 #split the list into halves
            # if number is equal to our middle term we return true
            if self[midpoint] == item:
                found = True
                index = midpoint

            # else check if number is in lower or upper list and loop though again
            else:
                counter += 1
                if item < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        return {'count':counter, 'index':index}

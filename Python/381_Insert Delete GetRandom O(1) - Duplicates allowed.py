class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.val_idxes = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.val_idxes[val].add(len(self.values))
        self.values.append(val)
        return len(self.val_idxes[val]) == 1

       
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.val_idxes[val]: return False
         
        del_idx = self.val_idxes[val].pop()
        last = self.values[-1]
        self.values[del_idx] = last
        self.val_idxes[last].add(del_idx)
        self.val_idxes[last].discard(len(self.values) - 1)
        self.values.pop()

        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        
        return random.choice(self.values)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false
otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element
exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

The class RandomizedSet is implemented using a hash table and an array. The hash table stores the values and their
indices in the array, while the array stores the actual values.

The insert method takes a value as input and adds it to the set if it does not already exist in the set.
 If the value already exists, it returns False to indicate that the operation was not successful.
 To check if the value exists in the set, the hash table is checked. If the value does not exist,
 the value is added to the end of the array, and the value-index pair is added to the hash table.
  The time complexity of this method is O(1) on average.

The remove method takes a value as input and removes it from the set if it exists in the set.
If the value does not exist, it returns False to indicate that the operation was not successful.
To check if the value exists in the set, the hash table is checked. If the value exists,
the index of the value in the array is obtained from the hash table, and the last value in the array is obtained.
 The value at the index is replaced with the last value in the array, and the index of the last value in the hash
 table is updated. The last value in the array is then removed, and the value-index pair for the removed value is
 removed from the hash table. The time complexity of this method is O(1) on average.

The getRandom method returns a random value from the set. To do this, a random value is chosen from the array using
the random.choice method. The time complexity of this method is O(1) on average.

Overall, the time complexity of each method is O(1) on average since all operations involve constant time hash table
 and array operations. The space complexity of the class is O(n), where n is the number of values in the set, since
 it uses a hash table and an array to store the values.

"""
import random


class RandomizedSet:
    import hashlib
    hashlib.shak
    def __init__(self):
        self.array = []
        self.array_values = {}

    def insert(self, val: int) -> bool:
        if val in self.array_values:
            return False
        else:
            self.array.append(val)
            self.array_values[val] = self.array.index(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.array_values:
            return False
        # yaha pr sabse pehle desired value ka index nikalo uspar last value replace kar do
        val_index = self.array_values[val]
        las_val = self.array[-1]
        self.array[val_index] = las_val
        self.array_values[las_val] = val_index
        self.array.pop()
        del self.array_values[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)




"""
LRU Cache

Problem Link:
https://leetcode.com/problems/lru-cache/description/

Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Test Case:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

"""
"""
Solution 1:
Please look for solution 2 as it is far shorter and better for interview perspective

Time Complexity: O(1) , for both get and put operation
Space Complexity: O(capacity) , for maintaining doubly linked list

class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyLinkedListNode(None, None)
        self.tail = DoublyLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get_head(self)->"DoublyLinkedListNode":
        return self.head

    def get_tail(self)->"DoublyLinkedListNode":
        return self.tail
    
    def add_from_head(self, key, value)->"DoublyLinkedListNode":
        node = DoublyLinkedListNode(key, value)
        current_first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = current_first_node
        current_first_node.prev = node
        return node
    
    def remove_from_tail(self)->"DoublyLinkedListNode":
        last_node = self.tail.prev
        if last_node == self.head:
            return None

        prev_of_last_node = last_node.prev
        prev_of_last_node.next = self.tail
        self.tail.prev = prev_of_last_node
        key_val = last_node.key
        del last_node
        return key_val
    
    def remove(self, node: "DoublyLinkedListNode")->None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del node





class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.capacity = capacity
        self.key_holders = {}       # dict to hold key and address
        self.key_size = 0
          

    def get(self, key: int) -> int:
        node = self.key_holders.get(key) # this will return memory address of the node
        if not node:
            return -1
        
        value = node.value
        self.dll.remove(node)
        node = self.dll.add_from_head(key, value)
        self.key_holders[key] = node
        return value
        
        

    def put(self, key: int, value: int) -> None:
        node = self.key_holders.get(key) # this will return memory address of the node
        if node:
            self.dll.remove(node)
            del self.key_holders[key]
            self.key_size -= 1
        
        if self.key_size == self.capacity:
            key_val_of_tail = self.dll.remove_from_tail()
            del self.key_holders[key_val_of_tail]
            self.key_size -= 1
        
        
        newly_created_node = self.dll.add_from_head(key, value)
        self.key_holders[key] = newly_created_node
        self.key_size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
"""
Time Complexity: O(1) , for both get and put
Space Complexity: O(capacity), size of LRU cache
"""        
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.ordered_dict = OrderedDict()
        self.capacity = capacity
        self.key_size = 0
          

    def get(self, key: int) -> int:
        value = self.ordered_dict.get(key) # this will return memory address of the node
        if value is None:
            return -1
    
        del self.ordered_dict[key]
        # Note: we are not increasing size here as the element already exists 
        # in the ordered dict before
        self.ordered_dict[key] = value
        return value
        
        

    def put(self, key: int, value: int) -> None:
        if self.ordered_dict.get(key) is not None:
            del self.ordered_dict[key]
            self.key_size -= 1
            
        if self.key_size == self.capacity:
            self.ordered_dict.popitem(last=False)
            self.key_size -= 1
        
        
        self.ordered_dict[key] = value
        self.key_size += 1

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


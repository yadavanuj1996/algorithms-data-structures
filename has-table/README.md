# Hash Table

## Hashing

Until now, the overall time complexity accomplished by most of the data structures in insertion, deletion, and search was up to O(logn) or O(nlogn), which is pretty good. But for a significantly large amount of data, this complexity starts to adversely affect the efficiency of an algorithm.

The ideal data structure is one that takes a constant amount of time to perform all three operations. And that is where hashing steps into the spotlight!

Hashing is a process used to store an object according to a unique key. This means that hashing always creates a key-value pair. A collection of such pairs forms a dictionary where every object or value can be looked up according to its key. Hence, the search operation can be performed in O(1).

The concept of hashing has given birth to several new data structures, but the most prominent one is the hash table.

### Hash Tables
If your algorithm prioritizes search operations, then a hash table is the best data structure for you. 
In Python, hash tables are generally implemented using lists as they provide access to elements in constant time.

In Python, we have several in-built types such as set and dict which can provide us the hash table functionality.

#### The Hash Function
- Restricting the Key Size
In the last lesson, we learned that a list can be used to implement a hash table in Python. A key is used to map a value on the list and the efficiency of a hash table depends on how a key is computed. At first glance, you may observe that we can directly use the indices as keys because each index is unique.

The only problem is that the key would eventually exceed the size of the list and, at every insertion, the list would need to be resized. Syntactically, we can easily increase list size in Python, but as we learned before, the process still takes O(n) time at the back end.

In order to limit the range of the keys to the boundaries of the list, we need a function that converts a large key into a smaller key. This is the job of the hash function.

![Screenshot 2022-11-16 at 8 08 26 PM](https://user-images.githubusercontent.com/22169012/202209657-97a87d13-05cf-40b0-9f02-3da247b54f9f.png)


A hash function simply takes an item’s key and returns the corresponding index in the list for that item. Depending on your program, the calculation of this index can be a simple arithmetic or a very complicated encryption method. However, it is very important to choose an efficient hashing function as it directly affects the performance of the hash table mechan

#### Approached for has function key generation
##### Arithmetic Modular
  - In this approach, we take the modular of the key with the list size:
  - index=key MOD table_size
  - Hence, the index will always stay between 0 and tableSize - 1.
```
def hash_modular(key, size):
    return key % size

lst = [None] * 10  # List of size 10
key = 35
index = hash_modular(key, len(lst))  # Fit the key into the list size
print("The index for key " + str(key) + " is " + str(index))

```

##### Truncation
  - Select a part of the key as the index rather than the whole key. Once again, we can use a mod function for this operation, although it does not need to be based on the list size:
  - key=123456 −> index=3456
```
def hash_trunc(key):
    return key % 1000  # Will always give us a key of up to 3 digits

key = 123456
index = hash_trunc(key)  # Fit the key into the list size
print("The index for key " + str(key) + " is " + str(index))
```

##### Folding
  - Divide the key into small chunks and apply a different arithmetic strategy at each chunk. For example, you add all the smaller chunks together:
  - key=456789,  chunk=2 −> index=45+67+89
```
def hash_fold(key, chunk_size):  # Define the size of each divided portion
    str_key = str(key)  # Convert integer into string for slicing
    print("Key: " + str_key)
    hash_val = 0
    print("Chunks:")
    for i in range(0, len(str_key), chunk_size):
        if(i + chunk_size < len(str_key)):
            # Slice the appropriate chunk from the string
            print(str_key[i:i+chunk_size])
            hash_val += int(str_key[i:i+chunk_size])  # convert into integer
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val


key = 3456789
chunk_size = 2
print("Hash Key: " + str(hash_fold(key, chunk_size)))

```

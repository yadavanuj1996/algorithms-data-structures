# Set (In built in python)

## Overview
A **set** is an unordered collection of unique elements in Python. Sets are mutable, but they can only contain immutable (hashable) objects. They are implemented using hash tables, making most operations very efficient.

## Key Characteristics
- **Unordered**: No guaranteed order of elements
- **Unique Elements**: Automatically eliminates duplicates
- **Mutable**: Can add/remove elements after creation
- **Hashable Elements Only**: Can contain strings, numbers, tuples (if they contain only hashable elements)
- **No Indexing**: Cannot access elements by index

## Creating Sets

```python
# Empty set
empty_set = set()  # Note: {} creates an empty dict, not set

# Set with initial values
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# From iterable
from_list = set([1, 2, 2, 3, 3, 4])  # Result: {1, 2, 3, 4}
from_string = set("hello")  # Result: {'h', 'e', 'l', 'o'}
```

## Set Methods and Operations

### Adding Elements
| Method | Description | Time Complexity | Example |
|--------|-------------|----------------|---------|
| `add(element)` | Add single element | O(1) average | `s.add(5)` |

### Removing Elements
| Method | Description | Time Complexity | Example |
|--------|-------------|----------------|---------|
| `remove(element)` | Remove element (raises KeyError if not found) | O(1) average | `s.remove(3)` |

### Testing and Comparison
| Method | Description | Time Complexity | Example |
|--------|-------------|----------------|---------|
| `len(s)` | Number of elements | O(1) | `len(my_set)` |
| `element in s` | Check membership | O(1) average | `5 in my_set` |
| `issubset(other)` | Check if subset | O(len(s)) | `s.issubset(other)` |
| `issuperset(other)` | Check if superset | O(len(other)) | `s.issuperset(other)` |

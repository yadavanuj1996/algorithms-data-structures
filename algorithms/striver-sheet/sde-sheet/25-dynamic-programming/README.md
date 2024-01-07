
![IMG_4904_2](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/fff32925-54bf-49a4-a8e1-5bb7772c9ee7)



Here's the algorithm summarized in bullet points:

- Initialize `result` to negative infinity, `prefix` to 1, `suffix` to 1, and `n` to the length of `nums`.
- Iterate through the elements of `nums`.
  - Update `prefix` by multiplying it with the current element.
  - Update `suffix` by multiplying it with the current element from the right end.
  - Update `result` by taking the maximum of `result`, `prefix`, and `suffix`.
  - If `prefix` becomes 0, reset it to 1.
  - If `suffix` becomes 0, reset it to 1.
- Return the final `result`, representing the maximum product of a subarray within the given list `nums`.

![IMG_4908](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/4331dab1-1770-4c59-9f29-d9ed528b6059)

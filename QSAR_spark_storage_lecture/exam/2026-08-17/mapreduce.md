# MapReduce (5 points)

*Big Data in Life Science — re-exam 2026-08-17*

Consider the following code, adapted from your MapReduce lab:

```python
from functools import reduce

fruits = ["Apple", "Strawberry", "Banana", "Pear",
          "Apricot", "Watermelon", "Orange", "Avocado", "Pineapple"]

# Step 1
fruits_letters = list(map(lambda s: [(s[0], 1)], fruits))

# Step 2
result = list(reduce(reduce_by_key, fruits_letters))
```

The helper function `reduce_by_key(list1, list2)` takes two sorted lists of `(key, count)` pairs and returns a single sorted list: for keys appearing in both lists their counts are summed; keys unique to one list are carried through unchanged.

**(a) [1 p]** What is the value of `result` after this code runs? Write out the list of pairs.

**(b) [1 p]** In one or two sentences, describe what the *map* step contributes and what the *reduce* step contributes to the overall computation.

**(c) [2 p]** The function used with `reduce()` in a MapReduce framework must be both **commutative** and **associative**. Explain in your own words what each of these two properties means, and why *both* are required when the reduce is executed in parallel across many machines.

**(d) [1 p]** Suppose you replaced the reduce function with `lambda x, y: x - y` (subtraction) operating on a list of numbers. If the framework splits this list differently across machines from one run to the next, would you get the same result each time? Explain briefly.

---

## Marking key

- **(a)** `[('A', 3), ('B', 1), ('O', 1), ('P', 2), ('S', 1), ('W', 1)]`
- **(b)** Map turns each fruit into a single-element list `[(first_letter, 1)]`; reduce successively merges these lists, summing counts per letter.
- **(c)** Commutative: `f(a, b) = f(b, a)` — order of the two arguments doesn't affect the result. Associative: `f(f(a, b), c) = f(a, f(b, c))` — grouping of successive applications doesn't affect the result. In parallel execution the framework may combine partial results in an unspecified order and grouping; without both properties the final answer would depend on how the framework happened to split and schedule the work.
- **(d)** No — subtraction is neither commutative nor associative. For example `(10 − 3) − 2 = 5` but `10 − (3 − 2) = 9`. Different splits give different answers. (A student pointing to either failing property is correct.)

**Point gradient:** 1 p recognition → 1 p paraphrase → 2 p concept → 1 p application.

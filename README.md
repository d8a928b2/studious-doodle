# Lab Assignment #5 – Using Trees and Priority Queues

## Exercise 1

**If your first name starts with a letter from A-J inclusively:**

Design the algorithm and method **following operations** for a binary
tree T:

- preorderNext(p): Return the position visited after p in a preorder
    traversal of T (or null if p is the last node visited).

- inorderNext(p): Return the position visited after p in an inorder
    traversal of T (or null if p is the last node visited).

Write a Java/Python to test your solution.

What are the worst-case running times of your algorithms?

**If your first name starts with a letter from K-Z inclusively:**

1. Design the algorithm and method **following operations** for a
    binary tree T:

- inorderNext(p): Return the position visited after p in an inorder
    traversal of T (or null if p is the last node visited).

- postorderNext(p): Return the position visited after p in a postorder
    traversal of T (or null if p is the last node visited).

Write a Java/Python to test your solution.

What are the worst-case running times of your algorithms?

(5 marks)

## Exercise 2

Give an efficient algorithm that computes and prints, for every position
p of a tree T, the element of p followed by the height of p’s subtree.
Write a Java/Python to test your solution.

**Hint**: Use a postorder traversal to find the height of each subtree.
The height for a subtree at p will be 0 if p is a leaf and otherwise one
more than the height of the max child. Print out the element at p and
its computed height during the postorder visit.

(3 marks)

## Exercise 3

**If your first name starts with a letter from A-J inclusively:**

Give an alternative implementation of the HeapPriorityQueue’s upheap
method that uses recursion (and no loop). **Hint**: Do a single upward
swap and recur (if necessary).

**If your first name starts with a letter from K-Z inclusively:**

Reimplement the SortedPriorityQueue using java array. Make sure to
maintain removeMin’s O(1) performance.

(2 marks)

## Appendix

### exceptions.py

### linked_queue.py

### tree.py

### binary_tree.py

### priority_queue_base.py

### heap_priority_queue.py

### doubly_linked_base.py

### positional_list.py

### sorted_priority_queue.py

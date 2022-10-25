# Using a priority queue
In python we can use a Heap Queue as priority queue. 
Heaps are binary trees for which every parent node has a value less than or equal to any of its children.

example

                               0

              1                                 2

      3               4                5               6

  7       8       9       10      11      12      13      14

15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

* The interesting property of a heap is that its smallest element is always the root, heap[0]. So get the lowest is constant

heapget() cost O(1)

* heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero

Index 0 is clearly the overall winner. The simplest algorithmic way to remove it and find the “next” winner is to move some loser (let’s say cell 30 in the diagram above) into the 0 position, and then percolate this new 0 down the tree, exchanging values, until the invariant is re-established. This is clearly logarithmic on the total number of items in the tree. By iterating over all items, you get an O(n log n) sort.

heappop cost O(n *log(n))

heapify cost O(n)

* A nice feature of this sort is that you can efficiently insert new items while the sort is going on

heappush cost O(log(n))

The priority queue is implemented with a list


## Time Complexity
the time complexity using a priority queue is O((|A| + |V|) * log|V|) = O(|A| * log|V|)

## space complexity
the space complecity is O(n)
becuase we use a visited map with n element
we use a distnace map with n elements
we use a heap with n elements
we use a father map with n elements


# Using a vector
## Time Complexity
the time complexity is O((|A| + |V|^2)) = O(|V|^2)
## space complexity

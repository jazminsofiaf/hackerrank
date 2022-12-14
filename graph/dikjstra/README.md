# Using a vector

## Time Complexity
the time complexity is O((|A| + |V|^2)) = O(|V|^2)
## space complexity
the space complecity is O(n)
becuase we use a not visited map with n element
we use a distnace map with n elements
we use a heap with n elements
we use a father map with n elements

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


# Using an index priority queue

An index priority queue is a simple array of values that can be access by index but it also has two extra array to maintain the priority:

1) Values[i] simple array of value with index i 
2) TreePosition[i] array of binary tree position of the element A[i]
3) Prio[p] array of index 'i' corresponding to array of values order by priority 

So we have Position[Prio[p]] = p.

example
Values = ['X','A','L','S','D',-] 
TreePosition = [4, 1, 3, 5, 2 ,-] 
Prio = [-, 1, 4, 2, 0, 3] 

so TreePosition[Prio[2]] = TreePosition[4] = 2
and Values[Prio[2]] = Values[4] = 'D'


* O(1) access to the top priority element   `Values[Prio[1]]= 'A'`

* O(log n) removal of the top priority element

* O(log n) insertion of a new element

* O(1) lookup of an arbitrary element’s priority key  `Values[Prio[2]]= 'D'`

* O(log n) removal of an arbitrary element

* O(log n) updating of an arbitrary element’s priority key



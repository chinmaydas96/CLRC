### Exercises 1.1-1
***
Give a real-world example that requires sorting or a real-world example that re-
quires computing a convex hull.

### `Answer`

* Everytime we arrange something ,we use various type of sorting algorithm unknowingly . From sorting of Alphabets to arranging vegitables by their size .

* For knowing the uses of convex hull ,we must try to understand what is a convex hull .Here is description at wikipedia .
  This image quite clear what is convex hull .
  ***
  ![Convex Hull](https://qph.ec.quoracdn.net/main-qimg-c9b2601253d4cbe8ab11570859ef2712-p)
  ***
  Two of uses that comes to my mind are :
  1. Robot Motion Planning 

	  In order to get from s to t, the shortest path will either be the straight line from s to t (if the obstacle doesn't intersect it) or one of the two polygonal chains of the convex hull.

	  ![Robot motion Planning](https://qph.ec.quoracdn.net/main-qimg-523e60e0af28b6f8a90942a17ea092ed-p)
  ***
  2. Use in image processing and pattern recognition.
  	Here is the example that given in opencv documentaion(image processing library) . 
  	The figure below displays convexity defects of a hand contour:
	  ***
	  ![Hand palm tracking](http://docs.opencv.org/2.4/_images/defects.png)
	  ***
  Source : Quora

### Exercises 1.1-2
***
Other than speed, what other measures of efficiency might one use in a real-world
setting?
  
### `Answer`

* Other than speed : 'Complexity' , 'Memory requirement' ,'Optimal method' is pretty used for efficiency .


### Exercises 1.1-3
***
Select a data structure that you have seen previously, and discuss its strengths and
limitations.

### `Answer`

I used array very often . 
* Strength : 
	1. It is used to represent multiple data items of same type by using only single name.
	2. It can be used to implement other data structures like linked lists, stacks, queues, trees, graphs etc.
	3. Easy to represent and understand.

* Limitation:

	1. It is static ,so it is fixed in size , It means memory allocated to array can't be reduced or increased .
	2. Searching and sorting is difficult and time consuming .  
	

### Exercises 1.1-4
***

How are the shortest-path and traveling-salesman problems given above similar?
How are they different?	

### `Answer`

* In both of problems we want that "lowest overall distance " travelled .
* The TSP solution requires its answer to be a cycle.However a shortest path will not (unless one is looking for shortest path 	  from a node to itself).
* TSP is an NP-complete problem and shortest path is known polynomial-time.

### Exercises 1.1-5
***
Come up with a real-world problem in which only the best solution will do. Then
come up with one in which a solution that is “approximately” the best is good
enough.

### `Answer`

* Sorting of a list (only the best solution will do, nearly sorted is not acceptable) .
* Finding the path between two points. (no matter what solution you used ,you still reach the point .So doesn'y matter)

***
### Exercises 1.2-1
***
Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

### `Answer`

* One of the example is Search engine. In search engine algorithmic content uses at application level such as crawling ,indexing , Ranking and Retrival .Crawling – where content is discovered; indexing, where it is analysed and stored in huge databases; and retrieval, where a user query fetches a list of relevant pages.Now a days search engine often uses machine learning technique for better user experience .


***
### Exercises 1.2-2
***
Suppose we are comparing implementations of insertion sort and merge sort on the
same machine. For inputs of size n, insertion sort runs in 8n^2 steps, while merge
sort runs in 64n lg n steps. For which values of n does insertion sort beat merge
sort?

### `Answer`
For approximately 2 < n < 43

***
### Exercises 1.2-3
***
What is the smallest value of n such that an algorithm whose running time is 100n^2
runs faster than an algorithm whose running time is 2^n on the same machine?

### `Answer`

n = 15






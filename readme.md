# Algorithms-Data-Structures

1) Character to String
String test=Character.toString('c');
2) 					Big O growth
		 O(1)<O(log n) < O(sqrt n) < O(n) < O(n log n) < O(n^2) < O(a^n) < O(n!)
		 
Growth of several common time complexities, and thus help you judge if your algorithm is fast enough to get  Accepted
		 Length Of Input(N)	 Worst Accepted Algorithm	 
		   <= [10..11]			O(N!), O(N^6)
		   <= [15..18]			O(2^N * N^2)
		   <= [18..22]			O(2^N * N)
		   <= 100			O(N^4)
		   <= 400			O(N^3)
		   <= 2K			O(N^2 * log N)
		   <= 10K			O(N^2)
		   <= 1M			O(N * log N)
		   <= 100M			O(N), O(log N), O(1)
		   
3) Integer.parseInt(br.readLine());
	Long.parseLong(String x);
4) char ch=x.charAt(i); i is int, x is string
5) String x=y.substring(0,2); if y=abcde then x=ab
	String x=y.substring(3);  if y=abcde then x=de
6) 	String array(x) to a
	int a[]=Arrays.streams(x).mapToInt(Integer::parseInt).toArray();
7) String to int
	String a=String.valueOf(b); b is int/long/short
8) ASCII value  A=65, a=97.  (int)b will return 66
9) BufferedReader br=new BufferedReader(new InputStreamReader(System.in))
	StringBuilder sb=new StringBuilder();
	replace ,delete stringbuilder methods useful 
10) Arrays.sort(arrName); to sort an array 
11) int intArray[] = {1,2,3}; 
    int cloneArray[] = intArray.clone(); 
	Array Cloning deep copy (not reference but new copy of array)
12) int x=y.indexOf('m'); if y="hello mate" then x=6
	int x=y.indexOf("mat"); if y="hello mate" then x=6
	// return first found index match
    similarly lastIndexOf function exist.
	
  
a)  Bitwise Operators	

1)	Bitwise Operators
	& (Bitwsie AND),| (Bitwsie OR), ~ (Bitwsie NOT), << (Left Shift),>> (Right Shift),^ (XOR)
	for left and right shift we can also use pow(2,k) rule for left shift multiply it.
2)	Using Bitwise operator we can calculate
    - isPowerOfTwo function in O(1) (x & x-1 will always be 0 if x is power of 2) (Pt. 3)
	- No. of 1 in binary format of number (Pt.3 & 5)
	-check if i(th) bit is set or not (using 1<<i) as 1<<i will be pow(2,i) and i will just
	 contain a single 1 at i(th) place.
	- To get power of 2 less than or equal to number N. First set all bits right from most
	  significant bit and then add 1 to it and right shift it (or divide by 2) (Pt.4)
3)  To get x-1 binary representation take the rightmost 1 in the binary representation of x and
	flip the bits to right of it including the right most 1 in x. (for all binary numbers)

4)  ( Program To get power of 2 less than or equal to number N )
	Let’s say binary form of a N is {1111}2 which is equal to 15.
	15 = pow(2,4)-1, where 4 is the number of bits in N.
	
	or 
	Let’s say binary form of a N is {101}2 which is equal to 5.
	next step=> flipping bits right of most significant bit 
				{111}2 which is equal to 7
	next step=>  adding 1 7+1=8 or {1000}2
	next step=>  dividing by 2 or right shifting by 1 {1000}2 >>1 = {100}2 or 4
	15 = pow(2,4)-1, where 4 is the number of bits in N.
	
	long largest_power(long N)
    {
        //changing all right side bits to 1.
        N = N| (N>>1);
        N = N| (N>>2);
        N = N| (N>>4);
        N = N| (N>>8);


    //as now the number is 2 * x-1, where x is required answer, so adding 1 and dividing it by
     2. 
                return (N+1)>>1;

    }
5)  If we do it by brute-force we will start dividing the number by 2 and count no. of 1
	that will take O(log N) time complexity where N is number (value not size).
	x & x-1 will always reduce a single 1 from binary representation as x-1 flips right most
	1 so x & x-1 will result in single 1 loss from binary representation 
	ex:- 6 & 5 = {110}2 & {101}2 = {100}2 =4
	CODE:- 
	int count_one (int n)
        {
            while( n )
            {
            n = n&(n-1);
               count++;
            }
            return count;
    }
	Time Complexity O(K) where k is no of 1 in binary representation.
	
	
	
	Applications of bit operations:-

	1) They are widely used in areas of graphics ,specially XOR(Exclusive OR) operations.
	2) They are widely used in the embedded systems, in situations, where we need to set/clear/toggle just one single bit of a 	
	   specific register without modifying the other contents. We can do OR/AND/XOR operations with the appropriate mask for the bit 	    position.
	3) Data structure like n-bit map can be used to allocate n-size resource pool to represent the current status.
	4) Bits are used in networking, framing the packets of numerous bits which is sent to another system generally through any type 	   of serial interface.

	
b) Basic Operators
	First, let's categorize them:
	1. Arithmetic   (+,-,*,/)
	2. Relational   (== , < , > , !=, <=, >=)
	3. Bitwise      (& ,|, ~, ^, <<, >>)
	4. Logical	(&&, ||, !)
	5. Assignment	(=, !=, /=, +=, -= , *=, %=) (check for bitwise operator combination with =)
	6. Increment	(++, -- )
	7. Miscellaneous
	
c) Arrays & Strings
	
	String :- String is an character array or sequence of characters.
	
	-Arrays are type of data structure that are used to store similar type of data or data of 
	 same data type in sequential manner.
	-Arrays have contigous or continuous memory allocation.
	-indexing starts from 0.
	-Multi Dimesion Array is possible(can be 1D,2D,3D and so on).
	-Declaration in JAVA
	 int a[]=new int[array_size];
	 int []a=new int[array_size];
	 int a[]={1,2,3,4};
	 int a[]=new int[] {1,2,3,4};
	 {
	 int a[];
	 a=new int[5];
	 } // the brackets are used only to display that both lines are part of same declaration
	
	
1)	Array
	Access :- 		O(1)
	Search :-		O(n) 		Linear 
				O(log n) 	Binary Search (NOTE: array has to be sorted for binary search) 
	Insertion :-		O(1) 		in end
				O(n) 		in middle as we have to shift the elements
	Deletion:- 		O(n)		shift all the elements
2)  Advantages of using arrays:-
	-Arrays allow random access of elements. This makes accessing elements by position faster.
	-Arrays have better cache locality that can make a pretty big difference in performance.

d) Sorting 
	Sorting is a process of arranging items in ascending or descending order. This process can
	be implemented via many different algorithms.
	
	Some famous Sorting algorithms:-
	-Bubble Sort
	-Selection Sort
	-Insertion Sort
	-Merge Sort
	-Quick Sort
	-Counting Sort
	-Radix Sort
	-Heap Sort
	
	NOTE : REMOVE O(Big Oh) by Ω in best case and by θ(theta) in average case, the O is used
	I have used it in such way for easy memorization of table
					   Ω				θ		    O	
					Best Case		Average Case		Worst Case		(Time Complexities)

	Bubble Sort		 	O(N)			  O(N^2)		  O(N^2)
	Insertion Sort 	 		O(N) 			  O(N^2)			  O(N^2)
	Selection Sort	 		O(N^2)			  O(N^2)			  O(N^2)
	Merge Sort 		      O(N log N)		O(N log N)			 O(N log N)
	
1) 	Bubble Sort - Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping
	the adjacent elements if they are in wrong order.
	Sorting In Place: Yes
	Stable: Yes
	Auxiliary Space: O(1)
	Usability:-In computer graphics it is popular for its capability to detect a very small 
				  error (like swap of just two elements) in almost-sorted arrays and fix it with 
				  just linear complexity (2n).
2)	Selection Sort - The selection sort algorithm sorts an array by repeatedly finding the 
	minimum element (considering ascending order) from unsorted part and putting it at the 
	beginning. 
	The algorithm maintains two subarrays in a given array.
		i) The subarray which is already sorted.
		ii) Remaining subarray which is unsorted.
	
	Sorting In Place : Yes
	Stable: No (For default implementation Not Stable)
	Auxiliary Space: O(1)
	Usability:- The good thing about selection sort is it never makes more than O(n) swaps and
		    can be useful when memory write is a costly operation.
	
3) 	Insertion sort
	Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our
	hands.
	Uses:-
	    i) Insertion sort is used when number of elements is small. It can also be useful when 
	   ii) Input array is almost sorted, only few elements are misplaced in complete big array.
	Sorting In Place: Yes
	Stable: Yes
	Auxiliary Space: O(1)
	Usability: Insertion sort is used when number of elements is small. It can also be useful when 
		   input array is almost sorted, only few elements are misplaced in complete big array.

4) 	Merge Sort
	Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself 
	for the two halves and then merges the two sorted halves. The merge() function is used for 
	merging two halves.
	
	Sorting In Place: No in a typical implementation
	Stable: Yes
	Auxiliary Space: O(n)
	Algorithmic Paradigm: Divide and Conquer
	Applications :- 
	i) Merge Sort is useful for sorting linked lists in O(N Log N) time
	ii) External Sorting
	

e) Hash Table
		
f) Hash Map (https://www.youtube.com/watch?v=c3RVW3KGIIE)
	
	HASH Map
	-Hash Map works on key value pair concept or association between a key and it's value.
	a key is passed to hash function and it's equivalent hash is returned then the hash value is
	coverted to a index (as hashvalues are large and we practically don't use such big arrays) and
	then the value is referenced by that particular index.
	-Hash Map has a table for storing indexes and has 16 entries (0-15) by default when hash map
	is declared and once the table gets filled equal or above threshold limit i.e., 75% the size
	of Hash Map is doubled (so the increase is in form of 2^n) and this concept is called rehashing.
	- Hash Map contains nodes that are referenced by indexes and each node contains 4 data members
	  i) K (key) 		("Charles")
	 ii) H (Hash code) 	(465231654)
	iii) V (Value)		(valueObject or valueNumber)
	 iv) N (Node)		(reference to next node)
	 In case of collision i.e., when two elements will have same hashcode thus they will have same
	 index value then the new node will be added and it's value will be referenced by the last 
	 node already stored  on that index (the nodes are stored in Linked List) but in java 8 as the
	 size of linked list crosses 8 it will be converted into a BST(Binary Search Tree).
	-Hash Map is one of the Data Structure whose implementation is provided in java.util package
	-Hash Map implements Map Interface(part of  Collection framework of java.util)
	-No sequential order iteration
	-Hash Map is preffered over default implementation of hash table
	 Methods 
		put(key , value ) // for inserting
		get(Object key) // for fetching
		
	Map<Integer> test =new HashMap<Integer>();
	
	Parsing:-
	for(int i: test){
		system.out.println(i);
	}
	
g)  Hash Set & Tree Set	
	
	Hash Set:-
	1)Hash Set does not holds duplicate values thus Set is collection of unique objects or elements.
	2)Hash set implements Set Interface(part of  Collection framework of java.util) in java
	3)Just like List we can use Set to store the values  except duplicates.
	4)No Sequential Iteration
	5) Inital capacity 16 and load factor 0.75.
	
	Tree Set:-
	1)Contains unique elements.
	2) Sequential Iteration unlike Hash Set.
	
	Set<Integer> test= new HashSet<Integer>();
	Set<Integer> test2= new TreeSet<Integer>();
	
	
	Common Methods
	add (Object element)
	to fetch  run a for loop and check equlity with equals() method.
	
h) ArrayList
	-Implements List Interface(part of java.util Collections framework)
	-underlying DS dynamic or growable array.
	-Best for retrieval
	- inital default size 10
	- when gets completely filled the arraylist resizes to (1.5* currentSize)
	 Declaration with size n
	 ArrayList<Integer> arrli = new ArrayList<Integer>(n);
	 
	 Common Methods 
	 get(int index)
	 add(E element)
	 add(int index,E element)
	 remove(int index)
	 
	 
i) LinkedList 
	-Implements List Interface(part of java.util Collections framework)
	-underlying DS Double Linked List.
	-Best for adding or removing element in middle
	 LinkedList<String> object = new LinkedList<String>(); 
	 
	Common Methods
	add​(int index, E element)
	add​(E e)
	addAll​(Collection c)
	addFirst​(E e) 
	addLast​(E e)

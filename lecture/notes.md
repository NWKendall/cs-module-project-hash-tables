Slot
Index Chain (linked list)
----- -------------------------------
 0    -> ("qux", 10) -> None
 1    -> ("plugh", 20) -> ("foo", 999) -> None
 2    -> ("xyzzy", 50) -> ("baz", 999) -> ("bar", 30) -> None
 3    -> None
put("foo", 12)   # hashes to 1
put("bar", 30)   # hashes to 2
put("baz", 999 ) # hashes to 2--collision with "bar"!
put("qux", 10)   # hashes to 0
put("plugh", 20) # hashes to 1 (collision!)
put("xyzzy", 50) # hashes to 2 (collision!)
put("foo", 999)   # hashes to 1

Put:
* Find the slot for the key
* Search the linked list for the key
* If found, update it
* If not found, make a new HashTableEntry and add it to the list

Get:
* Find the slot for the key
* Search the linked list for the key
* If found, return the value
* If not found, return None

Delete:
* Find the slot for the key
* Search the linked list for the key
* If found, delete it from the linked list, then return the deleted value
* If not found, return None



Hash Table Load Factor
----------------------
0 |-> D  Load factor: 3 / 8 = 0.375
1 |->  
2 |-> A
3 |-> C
4 |->  
5 |->  
6 |->  
7 |->  
0 |-> D  Load factor: 1.0
1 |-> H
2 |-> A
3 |-> C
4 |-> G
5 |-> B
6 |-> E
7 |-> F
0 |-> D -> M            Load factor: 2.0
1 |-> H
2 |-> A -> I
3 |-> C -> J -> L -> N
4 |-> G
5 |-> B -> O
6 |-> E -> K -> P
7 |-> F
0 |-> D -> M -> Q          Load factor: 29 / 8 = 3.625
1 |-> H -> R -> X -> Y
2 |-> A -> I -> 0
3 |-> C -> J -> L -> N -> Z
4 |-> G -> S -> U
5 |-> B -> O -> 1 -> 2
6 |-> E -> K -> P -> W
7 |-> F -> T -> V

Load Factor
-----------
number of things stored in the hash table / number of slots in the array
When computing the load, keep track of the number of items in the hash table as
you go.
* When you put a new item in the hash table, increment the count
* When you delete an item from the hash table, decrement the count
When is the hash table overloaded?
* It's overloaded when load factor > 0.7
* It's underloaded when load factor < 0.2 (Stretch)
Resize the Hash Table
---------------------
Resize:
In a nutshell, take everything out of the old hash table array, and put it in a
new, resized array.
1. Allocate a new array of bigger size, typically double the previous size
   (or half the size if resizing down, down to some minimum)
2. Traverse the old hash table -- O(n) over the number of elements in the hash
   table
   For each of the elements:
      Figure it's slot in the bigger (or smaller), new array
      Put it there
Automatically do this when the hash table is overloaded, or underloaded
(stretch).

- python allows any mutable type of tdata to be used in a key
class Node:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        # how many indexes
        self.capacity = capacity
        # currently utilized slots
        self.size = 0
        # data structure (array length of capacity populated with default values)
        self.buckets = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        """
        Returns: The FNV-1 hash of a given string. 
        """
        # Constants
        # FNV_prime = 1099511628211
        # offset_basis = 14695981039346656037

        # FNV-1a Hash Function
        # hash = offset_basis + seed
        # for char in string:
        #     hash = hash * FNV_prime
        #     hash = hash ^ ord(char)
        # return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # https://gist.github.com/mengzhuo/180cd6be8ba9e2743753
        hash = 5381

        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
            self.put(key, value)
        # generate hash based on key
        else:
            slot = self.hash_index(key)

            # input value into buckets
            node = self.buckets[slot]

            # control for empty slot
            if node is None:
                self.buckets[slot] = Node(key, value)
                # increase size += 1
                self.size += 1
                return

            # setting anoth var to be equal to node
            prev = node
            # iterate through LL
            while node is not None:
                # overwrite node value if keys match
                if node.key is key:
                    node.value = value
                prev = node
                node = node.next
            # else add a new node linked to tail's next
            prev.next = Node(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # replace data at that key entry with default value (None)
        if self.get_load_factor() < 0.2:
            if self.capacity / 2 < 8:
                self.resize(8)
                self.delete(key)
            else:
                self.resize(int(round(self.capacity / 2, 0)))
                self.delete(key)
        else:
            # generate hash based on key
            slot = self.hash_index(key)
            node = self.buckets[slot]
            prev = None

            # Iterate to the requested node
            while node is not None and node.key is not key:
                prev = node
                node = node.next
                # control for none
            if node is None:
                # return none
                return None
            else:
                # key match occurred
                # decrement size
                self.size -= 1
                # store value to return
                result = node.value
                # Delete this element in linked list
                if prev is None:
                    self.buckets[slot] = node.next
                else:
                    # LinkedList delete by skipping over
                    prev.next = prev.next.next
                # Return the deleted result
                return result

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # generate hash value
        slot = self.hash_index(key)
        # store in variable
        node = self.buckets[slot]
        # iterate through LL
        while node is not None and node.key is not key:
            node = node.next
        # return none if no key match / 404
        if node is None:
            return None
        # if key does match, return the node value at that location
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # print("RESIZE", new_capacity)
        # if resizing, size with current bucket array needs to be reset
        self.size = 0
        # stores existing LLs in a var
        old_buckets = self.buckets
        # update capacity to new capacity
        self.capacity = new_capacity
        # rezized arr for LLs to be placed
        self.buckets = [None] * self.capacity
        # iterate through OLD array (as new arr contains None)
        for node_index in old_buckets:
            # store LL head in var for LL traversal
            cur = node_index
            while cur is not None:
                # for each node in LL, add to buckets (which has been readjusted)
                self.put(cur.key, cur.value)
                # traverse each node to repeat
                cur = cur.next


if __name__ == "__main__":
    ht = HashTable(800)
    print("num slots:", ht.get_num_slots())
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.delete("line_12")
    ht.delete("line_11")


    print("")
    print("num slots:", ht.get_num_slots())
    print("new size", ht.size)

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
    print("num slots:", ht.get_num_slots())
    print("Load Factor:", ht.get_load_factor())
    # print("num slots:", ht.resize(13))
    print("new size", ht.size)
    print("num slots:", ht.get_num_slots())
    print("new size", ht.size)
    print("Load Factor:", ht.get_load_factor())


#Initialize Queue, []
#storage = queue
#No need to reset Queue head or tail, does it on it's own
#Resets directory location to 0
#Tail and head can point to the same location. Queue is empty = Size = 0
#Head and tail can be greater than each other. Same pointers, allowed to cross.

#after running tests, 0 can't be current location. Noting the stylization of the tests,
# it sort of has to be behind in order to append, like schedules of most arrays.
# -1 seems to function, as if outside of the array.

# Head and Tail aren't used, but left as reference.

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.head = 0
        # self.tail = 0
        self.pointer = -1
        self.storage = []

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.pointer = (self.pointer + 1) % self.capacity
            self.storage[self.pointer] = item
        else:
            self.storage.append(item)

    def get(self):
        return self.storage

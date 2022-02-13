class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.slots = 10
        self.size = 0
        self.bucket = [None]*self.slots
        self.occupation_rate = 0.1

    def get_size(self):
        return self.size

    def double_size(self):
        print('double hash table size')
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        new_size = 0
        for x in self.bucket:
            while x:
                new_index = hash(x.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(x.key, x.value)
                    new_size += 1
                else:
                    head = new_bucket[new_index]
                    while head:
                        if head.key == x.key:
                            head.value = x.value
                            break
                        elif head.next is None:
                            head.next = HashEntry(x.key, x.value)
                            break
                        else:
                            head = head.next
                x = x.next
        self.size = new_size
        self.bucket = new_bucket
        self.slots = new_slots
        print('new slots size', self.slots)

    def remove(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        if not head:
            print('key does not exist, 1')
            return
        prev = head
        if prev.key == key:
            head = None
            self.bucket[index] = prev.next
        else:
            head = head.next
            flag = False
            while head:
                if head.key == key:
                    prev.next = head.next
                    head = None
                    flag = True
                    break
                else:
                    head = head.next
                    prev = prev.next
            if not flag:
                print('key does not exist, 2')
        if self.bucket[index] is None:
            self.size -= 1
            return


    def isEmpty(self):
        return self.size == 0

    def get_index(self, key):
        hash_value = hash(key)
        return hash_value % self.slots

    def insert(self, key, value):
        index = self.get_index(key)
        if not self.bucket[index]:
            self.bucket[index] = HashEntry(key, value)
            self.size += 1
            if float(self.size)/self.slots > self.occupation_rate:
                self.double_size()
        else:
            head = self.bucket[index]
            while head:
                if head.key == key:
                    head.value = value
                    break
                elif head.next == None:
                    head.next = HashEntry(key, value)
                    break
                else:
                    head = head.next

    def get_value(self, key):
        index = self.get_index(key)
        if not self.bucket[index]:
            return None
        head = self.bucket[index]
        while head:
            if head.key == key:
                return head.value
            else:
                head = head.next
        return None

def test():
    my_hash = HashTable()
    my_hash.insert(10.2, 10)
    my_hash.insert(10.3, 100)
    my_hash.insert(1.2, 5)
    my_hash.remove(10.2)
    my_hash.remove(999.9)
    print(my_hash.get_size())


test()

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        return new_node.get_data()

    def delete_friend(self, num):
        a, b = 0, 0
        current = self.head
        delfriend = False
        for _ in xrange(num):
            while current:
                a = current.get_data()
                b = current.get_next().get_data()
                if a > b:
                    self.delete(b)
                    delfriend = True
                    break
                current = current.get_next()
            if delfriend is False:
                current = self.head
                self.delete(current.get_data())


    def __str__(self):
        current = self.head
        d = []
        while current:
            d.append(str(current.get_data()))
            current = current.get_next()
        return ' '.join(reversed(d))

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



for _ in xrange(int(raw_input())):
    l = LinkedList()
    length, num = map(int, raw_input().split())
    for i in raw_input().split():
        l.insert(int(i))
    l.delete_friend(num)
    print l


'''for testcases in xrange(int(raw_input())):                                      
    friends_count, remove_count = map(int, raw_input().split())                 
    friends = map(int, raw_input().split())                                     
    temp = []                                                                   
    for friend in friends:                                                      
        while remove_count and temp and temp[-1] < friend:                      
            temp.pop()                                                          
            remove_count -= 1                                                   
        temp.append(friend)                                                     
    print ' '.join(map(str, temp))'''






















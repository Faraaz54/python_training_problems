from collections import deque
class Node():
    def __init__(self,label=None,data=None):
        self.label = label
        self.data = data
        self.children = dict()
        self.priority = 0

    def addChild(self,key,data=None):
        if not isinstance(key,Node):
            self.children[key] = Node(key,data)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        return self.children[key]


class Trie():
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]

    def add(self,word,weight):
        current_node = self.head
        word_finished = True
        i = 0
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1

        current_node.data = word
        current_node.priority = weight

    def has_word(self,word):
        current = self.head
        exists = True
        if word == '':
            return False
        if word is None:
            raise ValueError('has_word requires a not null string')

        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                exists = False
                break

        if exists:
            if current.data is None:
                exists = False

        return exists

    def start_with_prefix(self,prefix):
        if prefix is None:
            raise ValueError('Prefix should be a not null string')
        words = list()
        top = self.head
        for letter in prefix:
            if letter in top.children:
                top = top.children[letter]
            else:
                return words

        if top == self.head:
            queue = deque([node for key, node in top.children.iteritems()])
        else:
            queue = [top]

        while queue:
            current = queue.pop(0)
            if current.data != None:
                words.append(current.data)

            queue = [node for key, node in current.children.iteritems()] + queue

        return words

    def getData(self,word):
        if self.has_word(word) is False:
            return None
        current = self.head
        for letter in word:
            if letter in current.children:
                current = current.children[letter]

        return current.priority


if __name__ == '__main__':
    """ Example use """
    trie = Trie()
    store = dict()
    d_entries, queries = map(int,raw_input().split())
    for _ in xrange(d_entries):
        word,weight = raw_input().split()
        trie.add(word,int(weight))

    for __ in xrange(queries):
        query = raw_input()
        options = trie.start_with_prefix(query)
        if len(options) > 0:
            store[query] = max([trie.getData(w) for w in options])
        else:
            store[query] = -1
        if query in store.keys():
            print store[query]
















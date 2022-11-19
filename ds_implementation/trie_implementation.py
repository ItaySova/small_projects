from functools import wraps
import time


def method_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("started function: ", func.__qualname__)
        print("args:",*args)
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time() - start
        print("time: {}".format(str(end)))
        return ret

    return wrapper


def wrap_methods(clas):
    for key, val in vars(clas).items():
        if callable(val):
            setattr(clas, key, method_wrapper(val))
    return clas


# @wrap_methods
class Trie(object):
    class Node(object):
        def __init__(self, val=None):
            self.val = val
            self.children = {}
            self.children_values = set()
            self.isEndOfWord = False

        def get_child(self, val):  # return if exist - else false
            if self.children:
                if val in self.children_values:
                    return self.children[val]
            return False

        def set_eow(self):
            self.isEndOfWord = True

    def __init__(self):
        self.head = self.Node()

    # @method_wrapper
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current, length = self.head, len(word)
        for i in range(length):
            c = current.get_child(word[i])
            if not c:
                new_node = self.Node(word[i])
                current.children[word[i]] = new_node
                current.children_values.add(word[i])
            current = current.get_child(word[i])
            if i == length - 1:
                current.set_eow()

    # @method_wrapper
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current, length = self.head, len(word)
        for i in range(length):
            c = current.get_child(word[i])
            if c:
                # print(c.val)
                current = c
                if i == length - 1:
                    if current.isEndOfWord:
                        return True
            else:
                return False

    # @method_wrapper
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current, length = self.head, len(prefix)
        for i in range(length):
            c = current.get_child(prefix[i])
            if not c:
                print("breaking in startWith, value: {}".format(prefix))
                return False
            current = c
            if i == length - 1:
                return True

# @method_wrapper
def command_parser(trie, command, value):
    if command == 'insert':
        # print("command {} value {}".format(command, value))
        return trie.insert(value[0])
    if command == 'search':
        # print("command {} value {}".format(command, value))
        res = trie.search(value[0])
        return False if not res else res
    if command == 'startsWith':
        # print("command {} value {}".format(command, value))
        res = trie.startsWith(value[0])
        return False if not res else res
    return


def main():
    input_commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    input_values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    trie = Trie()
    print("start")
    numOfCommands = len(input_commands)
    final_output = []
    for i in range(1, numOfCommands):
        final_output.append(command_parser(trie, input_commands[i], input_values[i]))

    print(final_output)

if __name__ == "__main__":
    main()

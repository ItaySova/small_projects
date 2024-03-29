# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
# store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.
# The trie implementation is an exercise from the leet code website,
# and this version will be later optimized and updated

from functools import wraps
import time
from command_parser import command_parser


def method_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("started function: ", func.__qualname__)
        print("args:", *args)
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time() - start
        print("time: {}".format(str(end)))
        return ret

    return wrapper


class Trie(object):
    class Node(object):
        def __init__(self, val=None):
            self.val = val
            self.children = {}
            self.isEndOfWord = False

        def get_child(self, val):  # changed
            if val in self.children:
                return self.children[val]
            return False

        def set_eow(self):
            self.isEndOfWord = True

    def __init__(self):
        self.head = self.Node()

    @method_wrapper
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.head
        for letter in word:
            if letter not in current.children:
                current.children[letter] = self.Node(letter)
            current = current.children[letter]
        current.set_eow()

    @method_wrapper
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.head
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isEndOfWord

    @method_wrapper
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.head
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


def main():
    input_commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    input_values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    trie = Trie()
    numOfCommands = len(input_commands)
    final_output = []
    for i in range(1, numOfCommands):
        final_output.append(command_parser(trie, input_commands[i], input_values[i]))
    print(final_output)


if __name__ == "__main__":
    main()

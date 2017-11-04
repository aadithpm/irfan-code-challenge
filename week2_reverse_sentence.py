"""

Reverse a Sentence Without Reversing The Words:

Input: str | Example: "Python is awesome"
Output: str | "awesome is Python"

Time complexity: O(n)

Algorithm:

    Get an input string, split it on spaces. Use the python Deque (Double-ended Queue) structure. Create a deque with the words, and pop from the right to get words in the reverse order.

** coz why not ** One-liner using an Array:

    def reverse_sentence(sentence):
        return " ".join(sentence.split(" ")[::-1])

Other structures:

    I ran tests using timeit. The code below has the deque implementation. Here are the runtimes for implementations with deque, list and stack for 100 executions of the string "Python is awesome":

    Deque: 0.08665333997801283
    Stack: 0.12959458122654063
    List: 0.12060839880022475

"""

from collections import deque

sentence = input("sentence? ")

def impl_deque(sentence):
    words = deque(sentence.split(" "))
    for i in range(len(words) - 1):
        print(words.pop(), end = " ")
    print(words.pop())

impl_deque(sentence)
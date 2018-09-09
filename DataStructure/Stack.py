import unittest


class Stack:
    def __init__(self, _max):
        self.items = []
        self.max = _max

    def push(self, item):
        if len(self.items) < self.max:
            self.items.append(item)
        else:
            print("abort push in order to prevent stack overflow. max 5")

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print("stack is empty, abort pop to prevent stack underflow")

    def print_stack(self):
        print(self.items)


    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class StackTest(unittest.TestCase):
    def test(self):
        st = Stack(6)
        self.assertTrue(st.is_empty())
        self.assertEqual(st.size(), 0)
        st.push(1)
        st.push(2)
        st.print_stack()
        st.pop()
        st.print_stack()
        st.push(3)
        self.assertEqual(st.peek(), 3)
        self.assertFalse(st.is_empty())
        self.assertEqual(st.size(), 2)
        st.pop()
        st.pop()
        st.pop()
        st.push(3)
        st.push(3)
        st.push(3)
        st.push(3)
        st.push(3)
        st.push(3)


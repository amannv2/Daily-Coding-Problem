# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be
# smaller than the length of the list. The list is very long, so making more than one pass is prohibitively
# expensive. Do this in constant space and in one pass.
import random


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = Node(1, None)

    def insert(self, data):
        new = Node(data, self.head)
        self.head = new
        del new

    def display(self):
        current = self.head
        print('H', end='')
        while current:
            print(f' -> {current.data}', end='')
            current = current.next
        print('\n')


def remove(linked_list, pos):
    ref = linked_list.head
    prev = linked_list.head
    current = linked_list.head

    count = 0
    while current:
        count += 1
        if count > pos:
            # print(f'Ref: {ref.data}')
            prev = ref
            ref = ref.next
        current = current.next

    print(f'\nRemoving {pos}th last node.\nThe node to be deleted: {ref.data} && Prev Node: {prev.data}\n\n')
    prev.next = ref.next
    del ref


ll = LinkedList()
ll.insert(random.randrange(1, 19, 9))
ll.insert(random.randrange(1, 19, 8))
ll.insert(random.randrange(1, 19, 7))
ll.insert(random.randrange(1, 19, 6))
ll.insert(random.randrange(1, 19, 5))
ll.insert(random.randrange(1, 19, 4))
ll.insert(random.randrange(1, 19, 3))
ll.insert(random.randrange(1, 19, 2))
ll.insert(random.randrange(1, 19, 1))

ll.display()

to_remove = 4
remove(ll, to_remove)

ll.display()

"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""


class Node:
    # Constructor Implementation
    def __init__(self, task_id, start_time, end_time):
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.next = None


"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""


class LinkedList:
    # Constructor Implementation
    def __init__(self):
        self.head = None

    # This method will return the head of the linked list
    def get_list_head(self):
        return self.head

    # This method is responsible for printing the linked list nodes
    def print_linked_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.task_id, tmp.start_time, tmp.end_time)
            tmp = tmp.next

    # This method is responsible for inserting node in the linked list
    # in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node: Node, insert_at_starting=0):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        insert_at_starting += 1

    # This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self, head):
        if head is None:
            return
        else:
            self.print_in_reverse(head.next)
            print(head.task_id, head.start_time, head.end_time)

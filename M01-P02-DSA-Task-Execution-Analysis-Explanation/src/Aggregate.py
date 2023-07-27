from src.LinkedList import LinkedList, Node

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""


class Aggregate:

    # Initializing linked list object for various operations
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list
        self.next = None
        self.head = None

    # Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        task_list = LinkedList()
        while self.head in task_list is None:
            total_time = task_list[2] - task_list[1]
            maximum = max(total_time)
            print(task_list[maximum])

    # Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):
        task_list = LinkedList()
        while self.head is None in task_list:
            total_time = task_list[2] - task_list[1]
            minimum = min(total_time)
            print(task_list[minimum])

    # Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        task_list = LinkedList()
        total_time = task_list[2] - task_list[1]
        count = 0
        total = 0

        for i in range(0, len(task_list)):
            total = total + total_time[i]
            count += 1
            avg = total / 2
            print(avg)

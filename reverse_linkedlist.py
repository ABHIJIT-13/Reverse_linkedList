#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)
def reverse(head):
    curr=SinglyLinkedListNode(0)
    prev=SinglyLinkedListNode(0)
    nex=SinglyLinkedListNode(0)
    curr = head
    prev = None
    while( curr != None):
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    head = prev
    return head                
if __name__ == '__main__':
    

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    #data = int(input())

    #position = int(input())

    llist_head = reverse(llist.head)

    print_singly_linked_list(llist_head, ' ')
    

    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position-1):
                if current is None:
                    print("범위를 벗어난 삽입입니다.")
                    return
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def delete(self, position):
        if self.is_empty():
            print("싱글 링크드 리스트가 비어있습니다.")
            return
        
        if position == 0:
            deleted_data = self.head.data
            self.head =self.head.next
        else:
            current = self.head
            for _ in range(position-1):
                if current is None or current.next is None:
                    print("범위를 벗어났습니다.")
                    return
                current = current.next
            deleted_node = current.next
            deleted_data = deleted_node.data 
            current.next = current.next.next
        return deleted_data
    
    def search(self, data):
        current  = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1             
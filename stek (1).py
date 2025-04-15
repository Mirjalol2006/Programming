class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None 
  
        
class Stek:
    def __init__(self):
        self.head = None  
        self.count = 0

    def push(self, data):           # Yangi elementni stekka qo'shish
        node = Node(data) 
        node.Next = self.head  
        self.head = node  
        self.count += 1

    def is_empty(self):               # Stek bo'shligini tekshirish
        return self.head is None
    

    def pop(self):                   # Stekdan eng yuqori elementni olib tashlash
        if self.is_empty():
            return "stek bo'sh"
        cur = self.head
        self.head = self.head.Next  
        self.count -= 1
        return cur.Data

    def peek(self):                # Stekning eng yuqori elementini ko'rish
        if self.is_empty():
            return "stek bo'sh"
        return self.head.Data

    
    def print(self):                  # Stekdagi barcha elementlarni chiqarish
        if self.is_empty():       
            return "stek bo'sh"
        cur = self.head
        while cur is not None:
            print(cur.Data , end=" -> ")
            cur = cur.Next


stek = Stek()
stek.push(  8848) 
stek.push(  8611) 
stek.push(  5895)
stek.push(  4807)
stek.push(  5642) 

stek.print()


                    
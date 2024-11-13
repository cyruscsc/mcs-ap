from abc import ABC, abstractmethod

class QueueLike(ABC):
    def __init__(self):
        self.data = []

    def push(self, val: any) -> None:
        self.data.append(val)
    
    @abstractmethod
    def pop(self) -> None:
        return
    
    def view(self) -> None:
        print('Elements: ' + ', '.join(self.data))

class Queue(QueueLike):
    def pop(self) -> any:
        if len(self.data) < 1: return print('Underflow!')
        print('Popped: ' + self.data.pop(0))

class Stack(QueueLike):
    def pop(self) -> any:
        if len(self.data) < 1: return print('Underflow!')
        print('Popped: ' + self.data.pop())

def menu() -> None:
    d = None
    while d is None:
        choice = input('Enter "q" for queue or "s" for stack: ')
        match str(choice):
            case 'q': d = Queue()
            case 's': d = Stack()
            case _: print('Invalid input')
        print()
    while True:
        print('Select an action...\n0. push\n1. pop\n2. view\nx. exit')
        choice = input('Enter number of action: ')
        match str(choice).lower():
            case '0': d.push(input('Enter value to push: '))
            case '1': d.pop()
            case '2': d.view()
            case 'x': break
            case _: print('Invalid input')
        print()

if __name__ == '__main__':
    menu()
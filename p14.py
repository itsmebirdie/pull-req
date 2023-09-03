# python program to inplement a stack (stack of students' name) using list in Python
stack = []
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Display')
    print('4. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        name = input('Enter name: ')
        stack.append(name)
    elif ch == 2:
        if len(stack) == 0:
            print('Stack is empty')
        else:
            print('Popped element: ',stack.pop())
    elif ch == 3:
        if len(stack) == 0:
            print('Stack is empty')
        else:
            print('Stack: ',stack)
    elif ch == 4:
        break
    else:
        print('Invalid choice')
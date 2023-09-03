# python program to implement a queue (queue of students' name) using list in Python
queue = []
while True:
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Display')
    print('4. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        name = input('Enter name: ')
        queue.append(name)
    elif ch == 2:
        if len(queue) == 0:
            print('Queue is empty')
        else:
            print('Dequeued element: ',queue.pop(0))
    elif ch == 3:
        if len(queue) == 0:
            print('Queue is empty')
        else:
            print('Queue: ',queue)
    elif ch == 4:
        break
    else:
        print('Invalid choice')
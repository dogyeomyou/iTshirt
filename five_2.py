# five_2.py

from collections import deque

#큐(queue) 구현을 위한 Queue 라이브러리

queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

queue.append(5)
queue.append(2)
queue.append(3)
queue.apeend(7)
queue.popleft()
queue.append(1)
queue.apeend(4)
queue.popleft()

print(queue)#FIFO 출력
queue.reverse()
print(queue)# 나중에 들어온 순서부터 출력 LIFO



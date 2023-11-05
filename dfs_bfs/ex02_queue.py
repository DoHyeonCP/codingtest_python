from collections import deque

# 큐를 구현하기 위해 deque라이브러리 사용
queue = deque() # 선입 선출

# 삽입5-삽입2-삽입3-삽입7-삭제-삽입1-삽입4-삭제

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8,0,1]

# 모든 번위를 포함하는 리스트 선언
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')

# 원소간의 차이가 최대 1000000이하 일 때 효율적
# 공간 복잡도가 낭비될 수 도 있다.
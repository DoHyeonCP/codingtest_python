# 선택정렬: 가장 작은 수를 앞으로 보내는 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_i = i
    for j in range(i+1, len(array)):
        if array[min_i] > array[j]:
            min_i = j
    array[i], array[min_i] = array[min_i], array[i] # 스와프

print(array)
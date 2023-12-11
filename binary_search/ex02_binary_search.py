# 이진 탐색: 찾으려는 중간점 위치에 있는 데이터를 반복적으로 비교
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))


result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
    
# 이진 탐색은 1000만 단위가 넘어갈 경우 빛을 발한다.
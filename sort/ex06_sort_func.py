# sorted()는 퀵정렬보다 살짝 느릴 수 있지만 Nlon(N)의 시간복잡도를 보장한다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# sort()는 리스느 객체의 내장 함수, 내부원소가 바로 정렬 됨.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# key 매개변수를 입력으로 받을 수 있다. 함수가 들어옴
array = [('바나나',2), ('사과',5), ('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
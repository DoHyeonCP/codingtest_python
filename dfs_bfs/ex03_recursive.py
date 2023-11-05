

def recursive_function(i):
    print(f"{i}번째 재귀함수를 호출합니다.")
    if i == 100:
        return
    recursive_function(i+1)
    
    
recursive_function(1)
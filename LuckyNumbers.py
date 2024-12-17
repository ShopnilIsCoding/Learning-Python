def generate_lucky_numbers(limit):
    lucky_numbers = []
    
    def dfs(number):
        if number > limit:
            return
        if number > 0:
            lucky_numbers.append(number)
        dfs(number * 10 + 4)
        dfs(number * 10 + 7)
    
    dfs(0)
    return sorted(lucky_numbers)

def find_lucky_numbers_in_range(A, B):
    lucky_numbers = generate_lucky_numbers(B)
    result = [num for num in lucky_numbers if A <= num <= B]
    if result:
        print(" ".join(map(str, result)))
    else:
        print(-1)

# Input
A, B = map(int, input().split())

# Output
find_lucky_numbers_in_range(A, B)

def question1():
    with open('./puzzleKey.txt', 'r') as file:
        directions = file.read()
        answer = 0
        for char in directions:
            if char == '(':
                answer += 1
            elif char == ')':
                answer -= 1
        print('floor:', answer)

def question2():
    with open('./puzzleKey.txt', 'r') as file:
        directions = file.read()
        accumulator = 0
        counter = 0
        for char in directions:
            if char == '(':
                accumulator += 1
            elif char == ')':
                accumulator -= 1
            counter += 1
            if accumulator < 0:
                print('basement entered at:', counter)
                break

question2()
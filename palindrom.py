while True:
    word = input()
    h = len(word) // 2
    a = word[:h] == word[:len(word)-h-1:-1]
    print(a)

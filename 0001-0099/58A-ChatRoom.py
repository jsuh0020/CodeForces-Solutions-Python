def chatRoom():
    s = input()
    word = "hello"
    count = 0
    for i in range(len(s)):
        if s[i] == word[count]:
            count += 1
        if count == 5:
            return "YES"
    return "NO"


print(chatRoom())

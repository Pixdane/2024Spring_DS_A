# 58A. Chat room

def hello(word: str) -> str:
    HELLO = "hello"
    pos = 0
    for char in word:
        if pos < 5 and char == HELLO[pos]:
            pos += 1
        if pos == 5:
            return "YES"
    return "NO"

if __name__ == "__main__":
    inp = input()
    print(hello(inp))

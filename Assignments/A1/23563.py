#23563: 多项式时间复杂度

def str_parser(word: str):
    words = [tuple(map(lambda x: 1 if x == '' else int(x), i.split("n^"))) for i in word.split('+')]
    return [i[1] for i in words if i[0] != 0]

if __name__ == "__main__":
    inp = str_parser(input())
    print(f"n^{max(*inp, 0)}")

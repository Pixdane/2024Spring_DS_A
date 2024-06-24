#118A. String Task
if __name__ == "__main__":
    word = input()
    print('.', '.'.join(filter(lambda x: not x in "aoyeui", word.lower())), sep='')

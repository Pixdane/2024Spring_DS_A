#24591:中序表达式转后序表达式

class Expression:
    def __init__(self, is_op, *args):
        self.__is_op = is_op
        if self.__is_op:
            self.__op = args[0]
            self.__paras = (args[1], args[2])
        else:
            self.__value = args[0]

    def display(self):
        if self.__is_op:
            return f"{self.__paras[0].display()} {self.__paras[1].display()} {self.__op}"
        if isinstance(self.__value, Expression):
            return self.__value.display()
        return self.__value

def str_parser(string):
    res = []
    tmp = []
    for char in string:
        if char in {'+', '-', '*', '/', '(', ')'}:
            if tmp:
                res.append(''.join(tmp))
            res.append(char)
            tmp = []
        else:
            tmp.append(char.strip())
    if tmp:
        res.append(''.join(tmp))
    return res

def expression_parser(exp):
    length = len(exp)
    if length == 1:
        return Expression(False, exp[0])
    for index in range(length):
        if exp[index] == '(':
            count = 1
            for rindex in range(index + 1, length):
                if exp[rindex] == '(':
                    count += 1
                elif exp[rindex] == ')':
                    count -= 1
                    if count == 0:
                        return expression_parser([expression_parser(exp[index + 1:rindex])] + exp[rindex + 1:])
        if exp[index] in {'+', '-'}:
            return Expression(True, exp[index], expression_parser(exp[:index]), expression_parser(exp[index + 1:]))
        if exp[index] in {'*', '/'}:
            return Expression(True, exp[index], expression_parser(exp[:index]), expression_parser(exp[index + 1:]))

test = str_parser("1+1+1+1+1+2*3")
test = expression_parser(test)
print(test.display())

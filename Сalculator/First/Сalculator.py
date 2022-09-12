def correctness_check(user_input: str) -> bool:
    if 'exit' in user_input.lower():
        exit('Goodbye!')
    for k in user_input:
        if k in '+-/* ':
            user_input = user_input.replace(k, '')
    if user_input.isdigit():
        return True
    else:
        return False


def output(check: bool, input_: str):
    if check:
        try:
            return ['will be:', eval(input_)]
        except:
            return "SyntaxError! Please enter a valid value, leading zeros are not allowed in decimal integer literals," \
                   "\nthe number of signs of the operations '*' and '/' must not exceed two and yes, you cannot divide by zero!"
    else:
        return "ValueError! Please enter a valid value!"


def calculator_test(a: str):
    return output(correctness_check(a), a)


def calculator():
    while True:
        b = output(correctness_check((a := input('Enter the expression to be evaluated, for example "2+2"\n'
                                                 'to exit, type "exit"\n'))), a)
        if len(b) != 2:
            print(b)
        else:
            print(*b)


if __name__ == '__main__':
    calculator()

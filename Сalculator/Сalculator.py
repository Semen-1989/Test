
def correctness_check(user_input: str) -> bool:
    if user_input == 'exit' or 'EXIT':
        exit('Счастливо!')
    for k in user_input:
        if k in '+-\* ':
            user_input = user_input.replace(k, '')
    if user_input.isdigit():
        return True
    else:
        return False


def output(check: bool, input_: str):
    if check:
        try:
            return eval(input_)
        except:
            return "SyntaxError! Введите корректное значение, ведущие нули в десятичных целочисленных литералах не допускаются"
    else:
        return "Valueerror! Введите корректное значение!"


if __name__ == '__main__':
    while True:
        print(output(correctness_check((a := input('Введите выражение, которое нужно вычислить, например "2+2"\n'
                                                   'для выхода наберите "exit"\n'))), a))
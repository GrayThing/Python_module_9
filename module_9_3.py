first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(value[0]) - len(value[1]) if len(value[0]) > len(value[1]) else len(value[1]) - len(value[0])
                for value in zip(first, second) if len(value[0]) != len(value[1]))
second_result = (len(first[index]) == len(second[index]) for index in range(0, len(first)))

print(list(first_result))
print(list(second_result))

from random import choice

# The first task
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda symbol1, symbol2: symbol1 == symbol2, first, second)))
# End of the first task


# The second task
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data}\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# End of the second task
# The third task


class MysticBall:
    def __init__(self, *words):
        self.words = [*words]

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
# End of the third task

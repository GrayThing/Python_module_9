class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __check_step(self):
        if self.step > 0:
            return lambda pointer, stop: pointer > stop
        else:
            return lambda pointer, stop: pointer < stop

    def __iter__(self):
        self.checker = self.__check_step()
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.checker(self.pointer, self.stop):
            raise StopIteration
        if self.pointer == self.start + self.step:
            return self.start
        return self.pointer

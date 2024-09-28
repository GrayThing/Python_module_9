def is_prime(func):
    def wrapper(first, second, third):
        temp_result = func(first, second, third)
        divide_list = [number for number in range(1, temp_result + 1) if not temp_result % number]
        if temp_result == 1:
            print('Простое')
        elif temp_result == 0:
            pass
        elif temp_result != 1 and len(divide_list) == 2:
            print('Простое')
        else:
            print('Составное')
        return temp_result
    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)
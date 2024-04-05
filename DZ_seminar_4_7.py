# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import random
import time
import threading
import asyncio
import multiprocessing

CONST = 1000000
# Функция для вычисления суммы элементов массива
def calculate_sum(arr):
    return sum(arr)

# Генерируем массив случайных целых чисел от 1 до 100
arr = [random.randint(1, 100) for _ in range(CONST)]


# Асинхронность
async def calculate_sum_async(arr):
    return sum(arr)


start_time = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(calculate_sum_async(arr))
print(f"Асинхронность: Сумма элементов массива - {result}, "
      f"Время выполнения - {time.time() - start_time} секунд")

#Многопроессорность
result = multiprocessing.Value('i')

start_time = time.time()

arr_sum = sum(arr)
result.value = arr_sum

print(f"Многопроцессорность: Сумма элементов массива - {result.value}, "
      f"Время выполнения - {time.time() - start_time} секунд")

# Многопоточность
def thread_function():
    global result
    result = calculate_sum(arr)

start_time = time.time()
thread = threading.Thread(target=thread_function)
thread.start()
thread.join()
print(f"Многопоточность: Сумма элементов массива - {result}, "
      f"Время выполнения - {time.time() - start_time} секунд")

if __name__ == '__main__':
    pass
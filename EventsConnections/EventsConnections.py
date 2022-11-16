print('Введите путь до файла .txt формата:\nПервая строка - данные по первой категории событий через пробел')
print('Вторая строка то же самое, но для второй категории, число значений должно быть одинаковым')
print('Пример:\n-----------------\n20 -10 153 24 -10\n-10 30 42 -50 24\n-----------------')
file_path = input('Вводить сюда: ')
if file_path[0] in ('"', "'"):
    file_path = file_path[1:-1]
with open(file_path) as f:
    first = list(map(int, f.readline().split()))
    second = list(map(int, f.readline().split()))

def ranking(sample: list[int]) -> list[int]:
    ranks = []
    sorted_list = sorted(sample)
    for i in sample:
        rank = sorted_list.index(i) + 1
        ranks.append(rank + ranks.count(rank))
    return ranks

first_ranks = ranking(first)
second_ranks = ranking(second)
n = len(first)

s_d_i = sum((first_ranks[i] - second_ranks[i])**2 for i in range(n))
connections_value = 1 - (6*s_d_i  /  (n*(n**2 - 1)))

if 1 >= abs(connections_value) > 0.7:
    connection = 'сильная'
elif 0.7 >= abs(connections_value) > 0.5:
    connection = 'значительная'
elif 0.5 >= abs(connections_value) > 0.3:
    connection = 'умеренная'
elif 0.3 >= abs(connections_value) >= 0:
    connection = 'незначительная'
else:
    print('Произошла ошибка')
    exit()

print(f'Связь между категориями событий {connection}\nЧисловое значение примерно равно: {round(connections_value, 6)}')
input()
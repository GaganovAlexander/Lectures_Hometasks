ways_names = ['AC', 'AB', 'CD', 'BD', 'CE', 'DG', 'DH', 'GI', 'HI', 'EG', 'BF', 'FH']
print('Введите значения длин путей через пробел в порядке:')
print(' '.join(ways_names))
ways_lengths = list(map(int, input().split()))
ways = {} # Это будет словарь, где ключ - это название пути (АС означает путь из А в С) а значение - длина пути
for i in range(12):
    ways[ways_names[i]] = ways_lengths[i]

complited_points = {'A': 0} # Тут будут хранится точки, кратчайшие пути до которых из А уже известны, ну и соответственно длины путей до них

temp_lengths = [ways['AC'], ways['AB']] # Это те пути(длинны), с которыми мы сейчас работаем, в нём есть длины всех путей доступных нам ИЗ(не В) уже открытых точек
temp_ways = ['AC', 'AB'] # А это их названия как в ways
while len(complited_points) < 9: # Пробегаем всё пока не откроем все точки
    min_len_index = temp_lengths.index(min(temp_lengths))   # Сначала в списке длин с которым мы работаем находим мнимальную
    next_point = temp_ways[min_len_index][1]    # Следующая точка - это второй символ в названии пути из строчки выше

    # Раз путь до этой точки оказался минимальным из рабочих - то это означает, что её мы открыли => добовляем её в известные точки
    complited_points[next_point] = temp_lengths[min_len_index] 
    temp_ways.pop(min_len_index) # Как я и говорил, нам доступны все пути ИЗ доступных точек, так что путь В следующуб точку мы убираем
    temp_lengths.pop(min_len_index) # И длинну пути соответственно тоже

    # Теперь добавим в доступные пути новые
    for i in ways.keys():
        if next_point == i[0]: # Если путь в ways НАЧИНАЕТСЯ с новой доступной точки - то добовляем этот путь в доступные
            temp_ways.append(i)
            temp_lengths.append(ways[i] + complited_points[next_point])
# После всего прохода for мы таким образом откроем все точки

# Выводим ответ
print(f'Кратчайшие пути из А в точки графа:\n{complited_points}')
print(f'''Ответ(кратчайший путь из А в I) = {complited_points['I']}''')

input()

import json


def main():
    with open('/work/Сохранение.txt', 'r') as textfile:
        save = textfile.readline() # Вытаскиваем сохранение из файла

    with open('/work/Текстовый_квест.json') as file:
        plot = json.load(file) # Загружаем сюжет в переменную
        if save != '':
            for i in save:
                plot = plot[i] # Загружаем последнее сохранение
        while plot['2'] != "Выйти": # Проверка на последнюю стадию сюжета
            print(plot["0"])
            print()
            ans = input() # Пользователь вводит вариант ответа
            while ans != '2' and ans != '1': # проверка на правильность ввода
                print('Пожалуйста, введите цифру варианта вашего ответа.')
                ans = input() # Повторный ввод
            with open('/work/Сохранение.txt', 'a') as textfile:
                textfile.write(ans) # Сохранение данных
            plot = plot[ans]
        print(plot['0'])
        ans = input()
        with open('/work/Сохранение.txt', 'w') as textfile:
            textfile.write('') # Так как сюжет кончился, удаляем данные из сохранения
        if ans == "2":
            print()
            return # Завершение программы по просьбе пользователя
        else:
            main() # Начало нового сюжета
main()

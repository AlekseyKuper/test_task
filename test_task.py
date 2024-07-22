import random

def main():
    print(
        " Данное консольное приложение предназначено для управления библиотекой книг.\n Приложение позволяет добавлять, удалять, искать, менять статус и отображать книги.\n Введите цифру для взаимодействия с приложением.\n")
    while (True):
        try:
            selection = int(input(
                "1.Отображение всех книг\t\t2.Добавление книги\t\t3. Поиск книги\t\t 4. Удаление книги\t\t5. Изменение статуса книги\t\t6.Выход\nВыберите действие: "))
            match selection:
                case 1:
                    read_data()
                case 2:
                    wtite_data()
                case 3:
                    search_data()
                case 4:
                    delete_data()
                case 5:
                    change_data()
                case 6:
                    break
        except:
            print("Файл не создан или некорректный ввод\n")
    print("Программа завершена")




def read_data():
    try:
        with open("library.txt", "r") as file:
            file = file.readlines()
            file = [line.strip() for line in file]
            page = 1
            score_page = 10
            score_element = 0
            print("___ОТОБРАЖЕНИЕ ВСЕХ КНИГ___")
            print("...")
            print('Запись:', page)
            print("...")
            for list in file:
                print(list)
                score_element += 1
                if score_element == score_page:
                    score_page += 10
                    page += 1
                    print("...")
                    print('Запись: ' + str(page))
                    print("...")
            print('___')

    except:
            print("Файл не создан. Необходимо сделать запись")


def wtite_data():
    with open("library.txt", "a") as file:
        print("___ДОБАВЛЕНИЕ КНИГИ___")
        print("...")
        print("Введите данные для записи...")
        id = str(random.randint(1,999))
        title = input("Название:")
        author = input("Автор:")
        year = str(input("Дата издания:"))
        status = "В наличии"
        join_data = ('ID:', id, 'Название:', title, 'Автор:', author, "Год публикации:", year, "Статус:", status)
        join_data = [join_data + "\n" for join_data in join_data]
        file.writelines(join_data)
        print('ЗАПИСЬ ДОБАВЛЕНА...')
        print('___')



def delete_data():
    with open("library.txt", "r") as for_delete:
        print("___УДАЛЕНИЕ КНИГ___")
        print("...")
        print("Введите данные для удаления книги...")
        for_delete = for_delete.readlines()
        for_delete = [line.strip() for line in for_delete]
        input_index = input("Введите ID:")
        index_id = for_delete.index(input_index)
        index_id-=1
        index_status = index_id + 10
        del for_delete[index_id:index_status]
        with open("library.txt", "w") as file:
            for_delete = [for_delete + "\n" for for_delete in for_delete]
            file.writelines(for_delete)
        print("ЗАПИСЬ УДАЛЕНА...")
        print('___')

def search_data():
    with open("library.txt", "r") as file:
        print("___ПОИСК КНИГ___")
        print("...")
        file = file.readlines()
        file = [line.strip() for line in file]
        search_input = input('Введите данные для поиска(например: название книги, автора, дата публикации, по статусу публикации "В наличии" или "Выдана";\n Обратите внимание в верхнем или нижнем регистре вы пишете, от этого будет зависеть запрос):\n')
        print("РЕЗУЛЬТАТ ЗАПРОСА:")
        slit_end = 10
        slit_start = 0
        score_element = 0
        for element in file:
            score_element += 1

        end_element = score_element + 10

        while end_element != slit_end:
            search_list = []
            for list in file[slit_start:slit_end]:
                search_list.append(list)
            if search_input in search_list:
                print("...")
                print('Совпадение:')
                print("...")
                for list in search_list:
                    print(list)
                slit_start += 10
                slit_end += 10

            else:
                print("...")
                print('Нет совпадений...')
                print("...")
                slit_start += 10
                slit_end += 10
        print('___')

def change_data():
    with open("library.txt", "r") as for_status:
        print("___ИЗМЕНЕНИЕ СТАТУСА КНИГ___")
        print("...")
        print("Введите данные для изменения статуса...")
        for_status = for_status.readlines()
        for_status = [line.strip() for line in for_status]
        input_index = input("Введите ID:")
        index_id = for_status.index(input_index)
        index_status = index_id + 8
        id_book = for_status[index_id]
        status_book = for_status[index_status]
        print(f"ID книги: {id_book}. Статус: {status_book}.")
        status_true = 'В наличии'
        status_false = 'Выдана'
        input_status = int(input('Введите 1 для изменения статуса книги на "В наличии" или 2 на статус "Выдана":'))
        if input_status == 1:
            for_status[index_status] = status_true
        elif input_status == 2:
            for_status[index_status] = status_false
        else:
            print("Некоректный ввод")
        with open("library.txt", "w") as file:
            for_status = [for_status + "\n" for for_status in for_status]
            file.writelines(for_status)
        print("СТАТУС ИЗМЕНЕН...")
        print('___')
main()
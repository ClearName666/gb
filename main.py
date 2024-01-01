# # задача 31
# def fib(num, n1=0, n2=1):
#     if num == 0:
#         return n2
#     return fib(num-1, n2, n1+n2)
#
# print(fib(7))
#
# # задача 33
# def f(x):
#     if x > 3:
#         return 1
#     return x
# list_ = [1,3,3,3,4]
# list_ = list(map(f, list_))
# print(list_)
#
# # задача 35
# def simpleNum(num):
#     for i in range(2, 10):
#         if i != num and num % i == 0:
#             return "Нет"
#     return "Да"
# print(simpleNum(5))
#
# # задача 37
# def revers_(n, *args):
#     if n == 0:
#         return
#     n -= 1
#     print(args[n])
#     revers_(n, *args)
#
# revers_(4, 5, 6, 3, 2)

# задание 35
path_file = "data.txt"
Search_data_txt = ["фамилия", "имя", "отчество", "номер телефона"]
data = []
def GetData(_path_file):
    data_ = []
    with open(_path_file, 'r', encoding='utf-8') as file:
        for line in file:
            data_.append(line)
    return data_
def PrintData(data_):
    for d in data_:
        print(d)

def InputData(data_, _path_file):
    try:
        with open(_path_file, 'a', encoding='utf-8') as file:
            file.write(data_ + "\n")
        print("данные записаны")
    except Exception as error:
        print(f"запись данных не удалась ошибка: {error}")
def SearchData(mod, dataSearch, _path_file):
    print(f"поиск по {Search_data_txt[mod]}")
    data_ = []
    ret_data = []
    with open(_path_file, 'r', encoding='utf-8') as file:
        for line in file:
            data_.append(line)
    for d in data_:
        one_d = d.split(', ')
        if one_d[mod].lower() == dataSearch.lower():
            print(f"найдена запись: {d}")
            ret_data.append(d)
    if len(ret_data) == 0:
        print("данные не найдены")
    return ret_data


def Menu():
    mod = -1
    while mod > 4 or mod < 0:
        mod = int(input(
            "Выберете действие:\n"
            "1 вывести данные из файла\n"
            "2 произвести поиск по данным\n"
            "3 записать данные\n"
            "4 скопировать строку в другой файл data1.txt\n"
            "введите команду: "
        ))
    return mod

def MenuSearch():
    search_text = ""
    mod = -1
    while mod > 3 or mod < 0:
        search_text = input(
            "Выберете действие и через пробел напишите поисковой запрос:\n"
            "0 поиск по фамилии\n"
            "1 поиск по имени\n"
            "2 поиск по отчеству\n"
            "3 поиск по номеру телефона\n"
            "введите команду: "
        )
        try:
            mod = int(search_text[0])
        except Exception as error:
            print(f"ошибка ввода поискового запроса: {error}")
    return search_text

def MenuRecordData():
    text_add_data = input("введите данные для записи в порядке \"фамилия, имя, отчество, номер_телефона\" через \nвведите данные: ")
    if len(text_add_data.split(", ")) == 4:
        return text_add_data
    else:
        print("данные введены не корректно")
        return ""


def CopyFile(line):
    with open("data.txt", "r", encoding="utf-8") as file:
        try:
            lines = file.readlines()
            str_ = lines[line - 1]
            return str_
        except Exception as error:
            print(f"Ошибка: {error}")
            return ""


def MenuLineСhoice():
    line = -1
    while line < 0:
        try:
            line = int(input("Введите строку которую надо скопировать в другой файл: "))
        except Exception as error:
            print(f"Ошибка {error} повторите команду")
    return line

def ControlMenu():
    mod = Menu()
    match mod:
        case 1:
            data = GetData(path_file)
            PrintData(data)
        case 2:
            search_text = MenuSearch()
            d_search = search_text.split()
            try:
                SearchData(int(d_search[0]), d_search[1], path_file)
            except Exception as error:
                print(f"ошибка ввода поискового запроса: {error}")
        case 3:
            data_Rec = MenuRecordData()
            if data_Rec:
                InputData(data_Rec, path_file)
        case 4:
            line = MenuLineСhoice()
            if line > 0:
                str_ = CopyFile(line)
                with open("data1.txt", "a", encoding="utf-8") as file:
                    file.write(str_)
                print(f"Записалась строка: \"{str_}\"")






while True:
    ControlMenu()



# data = GetData(path_file)
# InputData(data, path_file)
# data = GetData(path_file)

# SearchData(0, "Смирнов", path_file)
# PrintData(data)


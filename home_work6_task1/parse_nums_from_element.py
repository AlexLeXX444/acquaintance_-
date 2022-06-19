# получает на вход элемент в виде строки,


# возвращает числовое значение коэффициэнта.
# если числовое значение отсутствует - возвращает элемент в исходном виде.
def parse_nums (element):
    index = element.find("*x")
    string_result = ''
    for i in range(0,index):
        string_result += element[i]
    if len(string_result) == 0:
        if index < 0:
            return element
    else:
        return int(string_result)

# возвращает строковое значение x в степени n.
# если передано числовое значение - возвращает пустую строку.
def parse_no_nums (element):
    index = element.find("*x")
    string_result = ''
    for i in range(index, len(element)):
        string_result += element[i]
    if index < 0:
        return ''
    else:
        return string_result
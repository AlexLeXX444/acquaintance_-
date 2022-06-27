# алгоритм дешифровки

def un_zip_data(data):
    data_cach = data.split('/')
    data_unzipped = ''
    while("" in data_cach) :
        data_cach.remove("")

    for i in range (len(data_cach)):
        number = data_cach[i]
        index = len(number) - 1
        counter = ''
        answer_str = ''
        for j in range (len(number) - 1):
            counter += number[j]
        float(counter)
        for k in range (int(counter)):
            answer_str += str(number[index])
        data_unzipped += answer_str

    return data_unzipped
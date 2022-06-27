# алгоритм сжатия

def zip_data(data_str):
    answer_string = ''
    i = 0
    while (i <= len(data_str)-1):
        counter = 1
        character = data_str[i]
        j = i
        while (j < len(data_str)-1): 
            if (data_str[j] == data_str[j + 1]): 
                counter += 1
                j += 1
            else: 
                break
        answer_string += f'{counter}{character}/'    
        i = j + 1
    return answer_string
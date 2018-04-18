data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peak_dict = {}
    for index, value in enumerate(data):
        if index < 2 or index == len(data)-1:
            continue
        else:
            # try:
                if data[index - 1] < value > data[index + 1]:
                    peak_dict[index] = value
            # except IndexError:
            #     pass
    return peak_dict


def valleys(data):
    valley_dict = {}
    for index, value in enumerate(data):
        if index < 2 or index == len(data):
            continue
        else:
            if data[index - 1] > value < data[index + 1]:
                valley_dict[index] = value
    return valley_dict

def peaks_and_valleys(data):
    POI = {}
    peak_dict = peaks(data)
    for key in peak_dict.items():
        POI[key] = 'P'
    valley_dict = valleys(data)
    for key in valley_dict.items():
        POI[key] = 'V'
    return POI

def lower_peak(an_index):
    peak_dict = peaks(data)
    left_peak_value = 0
    for key, value in peak_dict.items():
        if an_index > key and left_peak_value < value:
            left_peak_value = value
    return left_peak_value




def draw_data(data):
    width = len(data)
    height = max(data)

    line = [' '*6]
    for i in range(height):
        for j in range(width):
            if max(data) - i <= data[j]:
                line.append('X')
            elif lower_peak(j) > data[j] and i >= max(data) - lower_peak(j):
                line.append('O')
            else:
                line.append(' ')
        line = '  '.join(line)
        print(line[:])
        line = [' '*6]
    print('data = {}'.format(data))

def main():
    draw_data(data)

if __name__ == '__main__':
    main()




import csv, json

data_list = []

def receive_data():
    # filename = input('Enter the name of the file with data: ')

    try:
        with open(f'{filename}.csv', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row)
                data_list.append(row)
    except FileNotFoundError:
        print(f'File {filename} was not found.')
    print(data_list)

    print('**************************************')

    user_id = int(input("Wprowadz id: "))
    for dicts in data_list:
        number = int(dicts.get('id'))
        print(number)
        if number == user_id:
            dicts.clear()
            print(data_list)

def return_to_json():
    json_str = json.dumps({"id": 1234})
    print(json_str)


if __name__ == '__main__':
    return_to_json()




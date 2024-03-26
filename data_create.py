def name_data():
    name = input('Введите ваше имя: ')
    return name


def surname_data():
    surname = input('Введите вашу фамилию: ')
    return surname


def phone_data():
    phone = input('Введите ваш номер телефона: ')
    return phone


def address_data():
    address = input('Введите ваш адрес: ')
    return address

def update(id='', new_name='', new_surname='', new_number='', new_address=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_surname != ''):
                    row[2] = new_surname.title()

                if(new_number != ''):
                    row[3] = new_number

                if(new_address != ''):
                    row[3] = new_address.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)

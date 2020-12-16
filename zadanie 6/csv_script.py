import csv
import os

option = '0'
while True:
    choice = input(
        '[1] - display CSV content\n'
        '[2] - add record\n'
        '[3] - remove record\n'
        '[4] - exit program\n'
    )

    if choice == '1':
        file = open('bikes.csv', 'r', newline='')
        data = csv.reader(file)
        for row in data:
            print("ID: ", row[0])
            print("Name: ", row[1])
            print("Brand: ", row[2], '\n')
        file.close()

    if choice == '2':
        file = open('bikes.csv', 'r', newline='')
        data = csv.reader(file)
        row_count = sum(1 for row in data)
        file.close()
        row_id = row_count + 1
        name = input("Name: ")
        brand = input("Brand: ")
        line = '\n' + str(row_id) + ',' + str(name) + ',' + str(brand)
        with open(r'bikes.csv', 'a') as f:
            f.writelines(line)

    if choice == '3':
        file_r = open('bikes.csv', 'r', newline='')
        data = csv.reader(file_r)
        id_row = str(input("Which record you want to delete? Enter id."))
        status = False
        file_w = open('bikes_tmp.csv', 'w', newline='')
        writer = csv.writer(file_w)
        for row in data:
            if row[0] != id_row:
                print("!" + row[0] )
                writer.write(row)
            else:
                status = True
        file_r.close()
        file_w.close()
        if status:
            print("Row was deleted")
            os.remove("bikes.csv")
            os.rename("bikes_tmp.csv", "bikes.csv")
        else:
            print("No record with entered ID")

    if choice == '4':
        break

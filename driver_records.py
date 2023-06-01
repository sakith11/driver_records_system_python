import csv
import random
import datetime
print("Driver Records ")
print()
print("type key for console key words")
print()
# creating driverrecords.csv and racedetails.csv if they are not found in the directory
while True:
    try:
        file = open("driverrecords1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            pass
        file.close()
        break
    except FileNotFoundError:
        row1 = ["driver", "age", "team", "car", "points"]
        file = open("driverrecords1.csv", "w+", newline='')
        writer = csv.writer(file)
        writer.writerow(row1)
        file.close()
        break
while True:
    try:
        file = open("racedetails1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            pass
        file.close()
        break
    except FileNotFoundError:
        file = open("racedetails1.csv", "w+", newline='')
        writer = csv.writer(file)
        row2 = ["n", "n", "Monte Carlo", "Sweden", "Croatia", "Portugal", "Italy", "Kenya", "Estonia", "Finland",
                "Belgium", "Greece", "New Zealand", "Spain", "Japan"]
        row3 = ["d", "d", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        row4 = ["w", "w", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        row5 = ["c", "c", "not completed", "not completed", "not completed", "not completed", "not completed",
                "not completed", "not completed", "not completed", "not completed",
                "not completed", "not completed", "not completed", "not completed"]
        writer.writerow(row2)
        writer.writerow(row3)
        writer.writerow(row4)
        writer.writerow(row5)
        file.close()
        break
# custom Exception class for error handling
class InputError(Exception):
    input_large = "the input must be less or equal to 25 characters"
    beyond_range = "the input is beyond the expected range"
    y_n = "the input must be either y or n"
    wrong_date = "enter a valid date "
    wrong_date_format = " the correct format is yyyy-mm-dd"

def add_record():
    global d_age
    global d_name
    global d_team
    global d_car
    global c
    incorrect = False
    empty = True
    c = 0
    while True:
        try:
            d_name = input("driver's name -")
            if len(d_name) <= 25 and d_name !='':
                break
            else:
                raise InputError
        except InputError as e:
            print(e.input_large)
    while True:
        try:
            d_age = int(input("driver's age -"))
            if d_age> 99 or d_age =='':
                raise ValueError
            break
        except ValueError:
            print("wrong input")
    while True:
        try:
            d_team = input("driver's team -")
            # if character of d_name,d_team,d_car is >25
            # when creating tables in vct and vrl become problematic
            if len(d_team) <= 25 and d_team != '':
                break
            else:
                raise InputError
        except InputError as e:
            print(e.input_large)

    while True:
        try:
            d_car = input("driver's car -")
            if len(d_car) <= 25 and d_car != '':
                break
            else:
                raise InputError
        except InputError as e:
            print(e.input_large)
    while True:
        try:
            d_points = int(input("current points -"))
            if d_points =='':
                d_points=0
            break
        except ValueError:
            print("wrong input")

    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == d_name:
            c += 1
            # d_name and d_car act as a composite key
            if row[0] == d_name and row[3] == d_car:
                incorrect = True
    if incorrect:
        # two records with the same name and car cannot remain
        while True:
            try:
                user_input15 = input("a similar record exists | n - change the name | c - change the car | e -exit")
                if user_input15 == "n" or user_input15 == "c" or user_input15 == "e":
                    pass
                else:
                    raise InputError
                break
            except InputError:
                print("input should be n/c/e")
        if user_input15 == "e":
            main_menu("null")
        elif user_input15 == "n":

            while True:
                try:
                    d_name_c = d_name
                    d_name = input("driver's name -")
                    if d_name == d_name_c or d_name =='':
                        raise InputError
                    else:
                        pass
                    if len(d_name) <= 25:
                        pass
                    else:
                        raise InputError
                    break
                    c = 0
                except InputError as e:
                    if len(d_name) > 25:
                        print(e.input_large)
                    else:
                        print("please change the name")
        elif user_input15 == "c":
            while True:
                d_car_c = d_car
                try:
                    d_car = input("driver's car -")
                    if d_car == d_car_c or d_car =='':
                        raise InputError
                    else:
                        pass
                    if len(d_car) <= 25:
                        pass
                    else:
                        raise InputError
                    break
                except InputError as e:
                    if len(d_car) > 25:
                        print(e.input_large)
                    else:
                        print("please change the car")
    if c == 0:
        # appending the new record to both files
        slct = input("do you want to add another record(y/n)")
        while slct != "y" and slct != "n":
            print("please enter a valid response")
            slct = input("do you want to add another record(y/n)")
        drv = [d_name, d_age, d_team, d_car, d_points]
        drv1 = [d_name, d_car]
        file = open("driverrecords1.csv", "a", newline='')
        writer = csv.writer(file)
        writer.writerow(drv)
        file.close()
        file2 = open("racedetails1.csv", "r")
        reader = csv.reader(file2)
        for row in reader:
            if row[0] == "n":
                for i in range(2, len(row)):
                    drv1.insert(i, "-")  #when simulating a race an error is thrown if empty columns are left empty
        file2.close()
        file1 = open("racedetails1.csv", "a", newline='')
        writer1 = csv.writer(file1)
        writer1.writerow(drv1)
        file1.close()
        if slct == "y":
            add_record()
        elif slct == "n":
            main_menu("null")

    elif c > 0:
        user_input4 = input("there are " + str(
            c) + " person(s) with the same name enter y to continue d to alter the name and n to exit ")
        if user_input4 == "y":
            drv = [d_name, d_age, d_team, d_car, d_points]
            drv1 = [d_name, d_car]
            file = open("driverrecords1.csv", "a", newline='')
            writer = csv.writer(file)
            writer.writerow(drv)
            file.close()
            file2 = open("racedetails1.csv", "r")
            reader = csv.reader(file2)
            for row in reader:
                if row[0] == "n":
                    for i in range(2, len(row)):
                        drv1.insert(i, "-")
            file2.close()
            file1 = open("racedetails1.csv", "a", newline='')
            writer1 = csv.writer(file1)
            writer1.writerow(drv1)
            file1.close()
        elif user_input4 == "d":
            d_name = input("please enter the new name")
            drv = [d_name, d_age, d_team, d_car, d_points]
            drv1 = [d_name, d_car]
            file = open("driverrecords1.csv", "a", newline='')
            writer = csv.writer(file)
            writer.writerow(drv)
            file.close()
            file2 = open("racedetails1.csv", "r")
            reader = csv.reader(file2)
            for row in reader:
                if row[0] == "n":
                    for i in range(2, len(row)):
                        drv1.insert(i, "-")
            file2.close()
            file1 = open("racedetails1.csv", "a", newline='')
            writer1 = csv.writer(file1)
            writer1.writerow(drv1)
            file1.close()
            file1 = open("racedetails1.csv", "a", newline='')
            writer1 = csv.writer(file1)
            writer1.writerow(drv1)
            file1.close()
        elif user_input4 == "n":
            main_menu("null")
        while True:
            try:
                slct = input("do you want to add another record?(y/n)")
                if slct == "y" or slct == "n":
                    break
                else:
                    raise InputError
            except InputError:
                print(InputError.y_n)
        if slct == "y":
            add_record()
        elif slct == "n":
            main_menu("null")
def udd_record():
    duplicated_rows = []
    row_count = 0
    duplicated_records = 0
    updated_row = []
    updated_row_race = []
    name_car = [0, 1]# stores name and car to update racedetails.csv
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    length = 0
    for row in reader:#checks if driverrecords file is empty
        if row[0] =="name":
            pass
        else:
            length += len(row)
    file.close()
    if length == 0:
        print("there are no records to be updated")
        main_menu("null")
    while True:
        try:
            d_name = input("please enter a driver name to update - ")
            if d_name == '':
                raise InputError
            break
        except InputError:
            print("enter a valid name")
    d_name_c = d_name#stores a copy of the original name
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    record_found = False
    for row in reader:
        row_count += 1
        if row[0] == d_name:
            duplicated_rows.append(row_count)
            duplicated_records += 1#number of records with the same name
            record_found = True
            print(str(duplicated_records) + str(row))
    file.close()
    if record_found == True and duplicated_records == 1:#if only one records exist with the same name
        user_input2 = input(
            "enter the relavent number| 1- driver name | 2- driver age | 3- driver team | 4- driver car | 5- driver points | 0- update")
        file = open("driverrecords1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            if row[0] == d_name:
                while user_input2 !="0":
                    if user_input2 == "1":
                        while True:
                            try:
                                d_name = input("driver's name -")
                                if len(d_name) <= 25 and d_name!='':
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.input_large)
                            name_car.remove(name_car[0])
                            name_car.insert(0, d_name)

                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                            row[0] = d_name

                    elif user_input2 == "2":
                        while True:
                            try:
                                d_age = input("enter the driver's age")
                                if int(d_age) <= 100 and d_age!='':
                                    break
                                else:
                                    raise InputError
                                break
                            except ValueError:
                                print("enter a valid age")
                            except InputError as e:
                                print(e.input_large)
                        row[1] =d_age
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                    elif user_input2 == "3":
                        while True:
                            try:
                                d_team = input("driver's team -")
                                if len(d_team) <= 25 and d_team !='':
                                    pass
                                else:
                                    raise InputError
                                break
                            except InputError as e:
                                print(e.input_large)
                        row[2]= d_team
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                            row[2] = d_team
                    elif user_input2 == "4":
                        while True:
                            try:
                                d_car = input("driver's car-")
                                if len(d_car) <= 25 and d_car!= '':
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.input_large)
                        row[3] = d_car
                        name_car.remove(name_car[1])
                        name_car.insert(1, d_car)
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                    elif user_input2 == "5":
                        while True:
                            try:
                                d_points = int(input("driver points -"))
                                if d_points =='':
                                    raise ValueError
                            except ValueError:
                                print("please enter a valid number of points")
                            row[4] = d_points
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                    else:
                        print("wrong input please try again")
                        user_input2 = input(
                            "enter the relavent number| 1- driver name | 2- driver age | 3- driver team | 4- driver car | 5- driver points | 0 - update")
                d_car_c = row[3]
                file1 = open("driverrecords1.csv", "r")
                reader1 = csv.reader(file1)
                duplicated_records =0
                for row1 in reader1:
                    if row1[0] == d_name and row1[3] == d_car_c:
                        duplicated_records += 1
                file1.close()
                if duplicated_records > 1:
                    while True:
                        try:
                            user_input15 = input(
                                "a similar record exists | n - change the name | c - change the car | e -exit")
                            if user_input15 == "n" or user_input15 == "c" or user_input15 == "e":
                                pass
                            else:
                                raise InputError
                            break
                        except InputError:
                            print("input should be n/c/e")
                    if user_input15 == "e":
                        main_menu("null")
                    elif user_input15 == "n":
                        while True:
                            try:
                                d_name_c = d_name
                                d_name = input("driver's name -")
                                if d_name == d_name_c or d_name =='':
                                    raise InputError
                                else:
                                    pass
                                if len(d_name) <= 25:
                                    pass
                                else:
                                    raise InputError
                                row[0] = d_name
                                name_car[0] = d_name
                                break
                            except InputError as e:
                                if len(d_name) > 25:
                                    print(e.input_large)
                                else:
                                    print("please change the name")

                    elif user_input15 == "c":
                        while True:
                            try:
                                d_car_c = d_car
                                d_car = input("driver's car -")
                                if d_car == d_car_c or d_car =='':
                                    raise InputError
                                else:
                                    pass

                                if len(d_car) <= 25:
                                    pass
                                else:
                                    raise InputError
                                row[3] = d_car
                                name_car[1] = d_car
                                break
                            except InputError as e:
                                if len(d_car) > 25:
                                    print(e.input_large)
                                else:
                                    print("please change the car")
            updated_row.append(row)
        file.close()
        file = open("driverrecords1.csv", "w+", newline='')
        writer = csv.writer(file)
        writer.writerows(updated_row)
        file.close()
        if name_car[0] != 0 or name_car[1] != 1:
            file1 = open("racedetails1.csv", "r")
            reader = csv.reader(file1)
            for row in reader:
                if row[0] == d_name_c and name_car[0] != 0 and name_car[1] != 1:#updating racedetails.csv/ doesn't need to check for same name and car both files are mirrored
                    row[0] = d_name
                    row[1] = d_car
                elif row[0] == d_name_c and name_car[0] == 0:
                    row[1] = d_car
                elif row[0] == d_name_c and name_car[1] == 1:
                    row[0] = d_name
                updated_row_race.append(row)
            file1.close()
            file1 = open("racedetails1.csv", "w+", newline='')
            writer = csv.writer(file1)
            writer.writerows(updated_row_race)
            file1.close()

    elif not record_found:
        print("record not found")
        user_input5 = input("do you want to try again(y/n) ")
        if user_input5 == "y":
            main_menu("udd")
        elif user_input5 == "n":
            main_menu("null")
    elif record_found == True and duplicated_records > 1:
        turn = 1
        user_input3 = int(input("multiple drivers found please enter the number of the record to update"))
        user_input2 = input(
            "enter the relavent number| 1- driver name | 2- driver age | 3- driver team | 4- driver car | 5- driver points | 0- update")
        in_row = duplicated_rows[user_input3 - 1]# gets wich duplicated record needs to be updated
        file = open("driverrecords1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            row_count += 1
            if row[0] == d_name and row_count == in_row:
                d_car_c = row[3]
                d_name_c = d_name
                while user_input2 != "0":
                    if user_input2 == "1":
                        while True:
                            try:
                                d_name = input("driver's name -")
                                if len(d_name) <= 25 and d_name !='':
                                    break
                                else:
                                    raise InputError

                            except InputError as e:
                                print(e.input_large)
                        name_car.remove(name_car[0])
                        name_car.insert(1, d_name_c)
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("please enter a valid input")
                        row[0] = d_name

                    elif user_input2 == "2":
                        while True:
                            try:
                                d_age = input("enter the driver's age")
                                if int(d_age) <= 100 and d_age!='':
                                    pass
                                else:
                                    raise InputError
                                break
                            except ValueError:
                                print("enter a valid age")
                            except InputError as e:
                                print(e.input_large)
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                        row[1] = d_age
                    elif user_input2 == "3":
                        while True:
                            try:
                                d_team = input("driver's team -")
                                if len(d_team) <= 25 and d_team !='':
                                    pass
                                else:
                                    raise InputError
                                break
                            except InputError as e:
                                print(e.input_large)
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                        row[2] = d_team
                    elif user_input2 == "4":
                        while True:
                            try:
                                d_car = input("driver's car-")
                                if len(d_car) <= 25 and d_car !='':
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.input_large)
                        name_car.remove(name_car[1])
                        name_car.insert(1, )
                        row[3] = d_car
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                    elif user_input2 == "5":
                        while True:
                            try:
                                d_points = int(input("driver points -"))
                                if d_points =='':
                                    raise ValueError
                            except ValueError:
                                print("please enter a valid number of points")
                        row[4] = d_points
                        while True:
                            try:
                                user_input2 = input("enter 0 to update or another number to continue")
                                if 0 <= int(user_input2) <= 5:
                                    break
                                else:
                                    raise InputError
                            except InputError as e:
                                print(e.beyond_range)
                            except ValueError:
                                print("enter a valid input")
                    else:
                        print("wrong input please try again")
                        user_input2 = input(
                            "enter the relavent number| 1- driver name | 2- driver age | 3- driver team | 4- driver car | 5- driver points | 0- update")

                d_car=row[3]
                file1 = open("driverrecords1.csv", "r")
                reader1 = csv.reader(file1)
                duplicated_records =0
                for row1 in reader1:
                    if row1[0] == d_name and row1[3] == d_car:
                        duplicated_records += 1
                file1.close()
                if duplicated_records > 1:
                    while True:
                        try:
                            user_input15 = input(
                                "a similar record exists | n - change the name | c - change the car | e -exit")
                            if user_input15 == "n" or user_input15 == "c" or user_input15 == "e":
                                pass
                            else:
                                raise InputError
                            break
                        except InputError:
                            print("input should be n/c/e")
                    if user_input15 == "e":
                        main_menu("null")
                    elif user_input15 == "n":
                        while True:
                            try:
                                d_name_c = d_name
                                d_name = input("driver's name -")
                                if d_name == d_name_c or d_name =='':
                                    raise InputError
                                else:
                                    pass

                                if len(d_name) <= 25:
                                    pass
                                else:
                                    raise InputError
                                row[0] = d_name
                                name_car[1] = d_car
                                break
                            except InputError as e:
                                if len(d_name) > 25:
                                    print(e.input_large)
                                else:
                                    print("please change the name")

                    elif user_input15 == "c":
                        while True:
                            try:
                                d_car_c = d_car
                                d_car = input("driver's car -")
                                if d_car == d_car_c or d_car =='':
                                    raise InputError
                                else:
                                    pass

                                if len(d_car) <= 25:
                                    pass
                                else:
                                    raise InputError
                                row[3] = d_car
                                name_car[1] = d_car
                                break
                            except InputError as e:
                                if len(d_car) > 25:
                                    print(e.input_large)
                                else:
                                    print("please change the car")
                # updated_row.append(row)
            elif row[0] == d_name:
                turn += 1
            updated_row.append(row)
    file.close()
    file = open("driverrecords1.csv", "w+", newline='')
    writer = csv.writer(file)
    writer.writerows(updated_row)
    file.close()
    if name_car[0] != 0 or name_car[1] != 1:
        file1 = open("racedetails1.csv", "r")
        reader1 = csv.reader(file1)
        for row in reader1:
            if row[0] == d_name_c and row[1] == d_car_c:
                if name_car[0] == 0 and name_car[1] != 1:
                    row[1] = d_car
                elif name_car[0] != 0 and name_car[1] == 1:
                    row[0] = d_name
                elif name_car[0] != 0 and name_car[1] != 1:
                    row[0] = d_name
                    row[1] = d_car
            updated_row_race.append(row)
        file1.close()
        file1 = open("racedetails1.csv", "w+", newline='')
        writer1 = csv.writer(file1)
        writer1.writerows(updated_row_race)
        file1.close()
    while True:
        try:
            user_input17 = input("do you want to update another record(y/n)?")
            if user_input17!= "y" and user_input17 != "n":
                raise InputError
            if user_input17 == "y":
                udd_record()
            elif user_input17 == "n":
                main_menu("null")
            break
        except InputError:
            print(InputError.y_n)

def ddd_record():
    while True:
        try:
            d_name = input("please enter the driver's name to be deleted-")
            if d_name == '':
                raise InputError
            break
        except InputError:
            print("enter a valid name")
    deleted_records = []
    deleted_records_race = []
    found1 = False
    row_count1 = 0
    dup_rows = 0
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    duplicated_row_num = []
    for row in reader:  # checks if the name is repeated
        row_count1 += 1
        if row[0] == d_name:
            dup_rows += 1
            duplicated_row_num.append(row_count1)
            found1 = True
            print(str(dup_rows) + str(row))
    file.close()
    if found1 == True and dup_rows == 1:  # if there is no repetition
        file = open("driverrecords1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            if row[0] == d_name:
                pass
            else:
                deleted_records.append(row)
        file.close()
        file1 = open("racedetails1.csv", "r")
        reader1 = csv.reader(file1)
        for row in reader1:
            if row[0] == d_name:
                pass
            else:
                deleted_records_race.append(row)
    elif found1 == True and dup_rows > 1:
        row_num = 0
        while True:
            try:
                user_input8 = input("there are multiple records please choose a record")
                if 0<int(user_input8)<=dup_rows:
                    break
                else:
                    raise InputError
            except InputError:
                print(InputError.beyond_range)
        file = open("driverrecords1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            row_num += 1
            if row_num == duplicated_row_num[int(user_input8) - 1]:
                pass
            else:
                deleted_records.append(row)
        row_num_race = 0
        file1 = open("racedetails1.csv", "r")
        reader1 = csv.reader(file1)
        for row in reader1:
            row_num_race+=1
            if row_num_race == duplicated_row_num[int(user_input8) - 1]+3:
                pass
            else:
                deleted_records_race.append(row)
        file1.close()
    elif found1 == False:

        while True:
            try:
                user_input9 = input("No record found do you want to search again(y/n)")
                if user_input9 == "y":
                    ddd_record()
                else:
                    main_menu("null")
            except ValueError or user_input9 != "y" or user_input9 != "n":
                print("wrong input ")
    while True:
        try:
            user_input23 = input("confirm (y/n)?")
            if user_input23 == "y" or user_input23 == "n":
                break
            else:
                raise InputError
        except InputError:
            print(InputError.y_n)
    if user_input23 == "n":
        main_menu("null")
    elif user_input23 == "y":
        file = open("driverrecords1.csv", "w+", newline='')
        writer = csv.writer(file)
        writer.writerows(deleted_records)
        file.close()
        file1 = open("racedetails1.csv", "w+", newline='')
        writer = csv.writer(file1)
        writer.writerows(deleted_records_race)
        file1.close()
    while True:
        try:
            user_input7 = input("do you want to delete another record(y/n)? ")
            if user_input7 == "y":
                ddd_record()
            elif user_input7 == "n":
                main_menu("null")
        except ValueError or user_input7 != "y" or user_input7 != "n":
            print("wrong input")

def vct():
    points = []
    name = []
    team = []
    car = []
    npoints = []
    nname = []
    nteam = []
    ncar = []
    position =0
    same_points = 0
    pos = []
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "driver":
            continue
        points.append(int(row[4]))
        name.append(row[0])
        team.append(row[2])
        car.append(row[3])
    file.close()
    while len(points) != 0:
        for letter in points:
            if letter == max(points):
                npoints.append(letter)
                i = points.index(letter)
                nname.append(name[i])  # appends the driver name whose points are max
                nteam.append(team[i])
                ncar.append(car[i])
                del points[i]  # deletes the driver details of the driver whose points are max
                del name[i]
                del team[i]
                del car[i]
    for i in range(0,len(npoints)):
        if i ==0:
            position+=1
            pos.append(position)
        else:
            if npoints[i] != npoints[i-1]:
                position+=1
                pos.append(position)
            else:
                same_points+=1
                if i != len(npoints)-1:
                    if npoints[i]!= npoints[i+1]:
                        pos.append(position)
                        position+=same_points-1
                        same_points =0
                    elif npoints[i] == npoints[i+1]:
                        pos.append(position)
                elif i == len(npoints)-1:
                    pos.append(position)
    print("position |points  | driver's name             | team       | car")
    print("================================================================")
    for i in range(0,len(nname)):
        l_pos = 9 - len(str(pos[i]))
        l_p = 8-len(str(npoints[i]))  # determines the number of spaces to keep the table uniform
        l_n = 25 - len(nname[i])
        l_t = 10 - len(nteam[i])
        print(str(pos[i])+" "*l_pos+"|"+str(npoints[i])+" "*l_p+"| "+nname[i]+" "*l_n+" | "+nteam[i]+" "*l_t+" | "+ncar[i])


def srr():
    racedetails = []
    increase = 0
    decrease = 0
    completed = False

    while True:
        try:

            print("Enter the race to simulate ")
            user_input10 = int(
                input(" 1 - Monte Carlo  2 - Sweden  3 - Croatia  4 - Portugal \n 5 - Italy  6 - Kenya "
                      "7 - Estonia  8 - Finland \n 9 - Belgium  10 - Greece  11 - New Zealand  12 - Spain "
                      "\n 13 -  Japan \n -"))
            if 1 <= user_input10 <= 13:
                pass
            else:
                raise InputError
            break
        except (InputError, ValueError):
            print("wrong input Please re-enter")
    file = open("racedetails1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "c":
            if row[user_input10 + 1] == "completed":
                completed = True
    file.close()
    if completed == True:
        while True:
            try:
                user_input13 = input(
                    "the race has already been completed do you wish to select another race(y) or go to the main menu(n)")
                if user_input13 != "y" and user_input13 != "n":
                    raise InputError
                elif user_input13 == "y":
                    srr()
                elif user_input13 == "n":
                    main_menu("null")
            except InputError:
                print(InputError.y_n)

    elif completed == False:
        while True:
            try:
                user_input11 = input("enter the date")
                if user_input11[4] != "-" or user_input11[7] != "-":
                    raise InputError
                date = datetime.datetime(int(user_input11[0] + user_input11[1] + user_input11[2] + user_input11[3]),
                                         int(user_input11[5] + user_input11[6]), int(user_input11[8] + user_input11[9]))
                break

            except (ValueError, InputError, IndexError):
                print("wrong syntax please enter the date again")

        while True:
            try:
                user_input12 = int(input("enter the weather condition \n 1- sunny |"
                                         " 2- light rain | 3- heavy rain |"
                                         " 4 - light snow | 5- heavy snow \n -"))
                if 1 <= user_input12 <= 5:
                    break
                else:
                    raise InputError

            except (InputError, ValueError):
                print("wrong input please re-enter")
    race = user_input10
    condition = user_input12  # the value will change according to weather
    if condition == 1:
        increase = 0.5
        decrease = 0.5
    elif condition == 2 or condition == 4:
        increase = 0.4
        decrease = 0.5
    elif condition == 3 or condition == 5:
        increase = 0.4
        decrease = 0.6
    total_points = 0
    probability = []
    driver = []
    car = []
    nprobability = []
    ncar = []
    ndriver = []
    points = []
    npoints = []
    points_in_race = []
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "driver":
            continue
        else:
            total_points += float(row[4])
    file.close()
    if total_points == 0:
        total_points += 1
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] =="driver":
            continue
        else:
            driver.append(row[0])
            car.append(row[3])
            points.append(row[4])
            prob = int(row[4]) / total_points
            probability.append(prob)
    file.close()
    p = random.randint(0, len(probability) - 1)
    m = random.randint(0, len(probability) - 1)
    probability[p] += increase
    if probability[m] > decrease:
        probability[m] -= decrease
    while len(probability) != 0:
        for letter in probability:
            if letter == max(probability):
                nprobability.append(letter)
                i = probability.index(letter)
                ndriver.append(driver[i])
                ncar.append(car[i])
                npoints.append(points[i])
                probability.remove(letter)
                driver.remove(driver[i])
                car.remove(car[i])
                points.remove(points[i])
    simiulated_race = []
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "driver":
            pass
        elif row[0] == ndriver[0] and row[3] == ncar[0]:
            p = int(row[4])
            p += 10
            row[4] = str(p)
        elif row[0] == ndriver[1] and row[3] == ncar[1]:
            p = int(row[4])
            p += 7
            row[4] = str(p)
        elif row[0] == ndriver[2] and row[3] == ncar[2]:
            p = int(row[4])
            p += 5
            row[4] = str(p)
        else:
            p = 0
        simiulated_race.append(row)
    file.close()
    for driver in ndriver:
        if ndriver.index(driver) == 0:
            points_in_race.append(10)
        elif ndriver.index(driver) == 1:
            points_in_race.append(7)
        elif ndriver.index(driver) == 2:
            points_in_race.append(5)
        else:
            points_in_race.append(0)
    file = open("driverrecords1.csv", "w+", newline='')
    writer = csv.writer(file)
    writer.writerows(simiulated_race)
    file.close()
    # update racedetails1.csv
    file1 = open("racedetails1.csv", "r")
    reader1 = csv.reader(file1)
    weather =''
    for row in reader1:
        if row[0] == "n":
            pass
        elif row[0] == "d":
            row[race + 1] = date
        elif row[0] == "w":
            if condition == 1:
                row[race + 1] = "sunny"
                weather ="sunny"
            elif condition == 2:
                row[race + 1] = "light rain"
                weather ="light rain"
            elif condition == 3:
                row[race + 1] = "heavy rain"
                weather ="heavy rain "
            elif condition == 4:
                row[race + 1] = "light snow"
                weather = "light snow"
            elif condition == 5:
                row[race + 1] = "heavy snow"
                weather = "heavy snow"
        elif row[0] == "c":
            row[race + 1] = "completed"
        else:
            for driver in ndriver:
                if row[0] == driver and row[1] == ncar[ndriver.index(driver)]:
                    l = str(ndriver.index(driver) + 1)
                    b = str(points_in_race[ndriver.index(driver)])
                    d = race + 1
                    place_string = l + "|" + b #  position|points
                    row[d] = place_string
                    break
        racedetails.append(row)
    file.close()
    file = open("racedetails1.csv", "w+", newline='')
    writer = csv.writer(file)
    writer.writerows(racedetails)
    file.close()
    ven =[]
    file = open("racedetails1.csv","r")
    reader = csv.reader(file)
    for row in reader:
        if row[0]=="n":
            ven.append(row[user_input10+1])
    file.close()
    print("========================results of the race========================")
    print("Venue   - " + ven[0])
    print("Date    - " + user_input11)
    print("Weather - " + weather)
    print("position | driver                  |car                      |points")
    print("====================================================================")
    for i in range(0,len(npoints)):
        l_po =9-len(str(i+1))
        l_d = 25 - len(ndriver[i])
        l_c = 25 - len(ncar[i])
        position = i+1
        print(str(position)+" "*l_po+"|"+ndriver[i]+" "*l_d+"|"+ncar[i]+" "*l_c+"|"+str(points_in_race[i]))


def vrl():
    race = []
    date = []
    ndate1 = []
    ndate2 = []
    nrace = []
    nwheather = []
    wheather = []
    winner = []
    nwinner = []
    while True:
        try:
            user_input14 = int(input("arrange from most recent -1 | arrange from oldest -2"))

            if user_input14 == 1 or user_input14 == 2:
                pass
            else:
                raise InputError
            break
        except (ValueError, InputError):
            print("wrong syntax please re-enter")
    while True:
        try:
            user_input15 = input("show only completed races?(y/n) -")
            if user_input15 == "y" or user_input15 == "n":
                pass
            else:
                raise InputError
            break
        except InputError:
            print("wrong input please try again")
    file = open("racedetails1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "n":
            length = len(row)
            for i in range(2, len(row)):
                if row[i] == '_' and user_input15 == "n":
                    race.append("0")
                elif row[i] == '_' and user_input15 == "y":
                    pass
                else:
                    race.append(row[i])
        elif row[0] == "d":
            for i in range(2, len(row)):
                if row[i] == '_' and user_input15 == "n":
                    date.append("0")
                elif row[i] == '_' and user_input15 == "y":
                    pass
                else:
                    date.append(row[i])
        elif row[0] == "w":
            for i in range(2, len(row)):
                if row[i] == '_' and user_input15 == "n":
                    wheather.append("-")
                elif row[i] == '_' and user_input15 == "y":
                    pass
                else:
                    wheather.append(row[i])
    file.close()
    h = length
    for k in range(2, h):
        file = open("racedetails1.csv", "r")
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'n' or row[0] == 'd' or row[0] == 'w' or row[0] == "c":
                continue
            else:
                string = row[k]
                if string == '-' and user_input15 == "n":
                    winner.append("-")
                    break
                elif string == '-' and user_input15 == "y":
                    break
                elif string[0] == "1":
                    winner.append(row[0])
                    break
        file.close()
    for d in date:
        if d == "0":
            ndate1.append("0")
        else:
            ndate1.append(str(d[0] + d[1] + d[2] + d[3] + "-" + d[5] + d[6] + "-" + d[8] + d[9]))
    if user_input14 == 1:
        while len(ndate1) != 0:
            for d1 in ndate1:
                if d1 == max(ndate1):
                    ndate2.append(d1)
                    ind = ndate1.index(d1)
                    nrace.append(race[ind])
                    nwheather.append(wheather[ind])
                    nwinner.append(winner[ind])
                    del race[ind]
                    del wheather[ind]
                    del winner[ind]
                    del ndate1[ind]
    if user_input14 == 2:
        for d3 in ndate1:
            if d3 == '0':
                ndate1[ndate1.index(d3)] = '99999999'
        while len(ndate1) != 0:
            for d2 in ndate1:
                if d2 == min(ndate1):
                    ndate2.append(d2)
                    ind = ndate1.index(d2)
                    nrace.append(race[ind])
                    nwheather.append(wheather[ind])
                    nwinner.append(winner[ind])
                    del race[ind]
                    del wheather[ind]
                    del winner[ind]
                    del ndate1[ind]
        for d4 in ndate2:
            if d4 == '99999999':
                ndate2[ndate2.index(d4)] = '0'
    print("Date        | Race           | Wheather    | Winner")
    print("===================================================")
    for i in range(0,len(ndate2)):
        l_d = 12 - len(ndate2[i])
        l_r =15 - len(nrace[i])
        l_w = 12 - len(nwheather[i])
        print(ndate2[i] + " "*l_d + "| " + nrace[i] +" "*l_r + "| " + nwheather[i] + " "*l_w + "| "+ nwinner[i])

def stf():
    driver_records = []
    race_details = []
    file = open("driverrecords1.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        driver_records.append(row)
    file.close()
    file1 = open("racedetails1.csv", "r")
    reader1 = csv.reader(file1)
    for row1 in reader1:
        race_details.append(row1)
    file.close()

    try:
        dr_name = input("enter the name for driver records file")
        if dr_name[-4]+dr_name[-3]+dr_name[-2]+dr_name[-1] == ''".txt":
            pass
        else:
            dr_name = dr_name+".txt"
    except IndexError:
        dr_name = dr_name+".txt"
    while True:
        try:
            file = open(dr_name,"r")
            file.readlines()
            file.close()
            raise InputError
        except FileNotFoundError:
            break
        except InputError:
            print("A file with the same name exists change the file name")
            dr_name = input("enter the name for driver records file")
            try:
                if dr_name[-4] + dr_name[-3] + dr_name[-2] + dr_name[-1] == ''".txt":
                    pass
                else:
                    dr_name = dr_name + ".txt"
            except IndexError:
                dr_name = dr_name + ".txt"
    try:
        rd_name = input("enter the name for race details file")
        if rd_name[-4]+rd_name[-3]+rd_name[-2]+rd_name[-1] ==".txt":
            pass
        else:
            rd_name = rd_name+".txt"
    except IndexError:
        rd_name = rd_name+".txt"
    while True:
        try:
            file = open(rd_name,"r")
            file.readlines()
            file.close()
            raise InputError
        except FileNotFoundError:
            break
        except InputError:
            print("A file with the same name exists change the file name")
            try:
                rd_name = input("enter the name for race details file")
                if rd_name[-4] + rd_name[-3] + rd_name[-2] + rd_name[-1] == ".txt":
                    pass
                else:
                    rd_name = rd_name + ".txt"
            except IndexError:
                rd_name = rd_name + ".txt"

    file3 = open(dr_name, "w")
    for r in driver_records:
        for i in range(0,len(r)):
            l_n = 25 - len(r[0])
            l_a = 4 - len(r[1])
            l_t = 25 - len(r[2])
            l_c = 25 - len(r[3])
        file3.writelines(r[0]+" "*l_n+"| "+r[1]+" "*l_a+" |"+r[2]+" "*l_t+"| "+r[3]+" "*l_c+"| "+r[4]+" \n")
    file3.close()
    file4 =open(rd_name,"w")
    for j in race_details:
        for k in range(0,len(j)):
            l = 25- len(j[k])
            file4.writelines(j[k]+" "*l)
        file4.write(" \n")
    file4.close()
def rff():
    class FileContentError(Exception):
        pass
    driver = []
    race = []
    race1 = []
    race2 = []
    driver1 = []
    driver2 =[]
    dr_file = input("enter the name for driver records file")
    try:
        if dr_file[-4] + dr_file[-3] + dr_file[-2] + dr_file[-1] == ".txt":
            pass
        else:
            dr_file = dr_file + ".txt"
    except IndexError:
        dr_file = dr_file + ".txt"
    while True:
        try:
            file = open(dr_file,"r")
            file.readlines()
            file.close()
            break
        except FileNotFoundError:
            user_input24 = input("No such file was found re-enter the file name or esc to exit")
            if user_input24 =="esc":
                main_menu("null")
            else:
                try:
                    if dr_file[-4] + dr_file[-3] + dr_file[-2] + dr_file[-1] == ".txt":
                        pass
                    else:
                        dr_file = dr_file + ".txt"
                except IndexError:
                    dr_file = dr_file + ".txt"


    try:
        rd_file = input("enter the name for race details file")
        if rd_file[-4] + rd_file[-3] + rd_file[-2] + rd_file[-1] == ".txt":
            pass
        else:
            rd_file = rd_file + ".txt"
    except IndexError:
        rd_file = rd_file + ".txt"
    while True:
        try:
            file= open(rd_file,"r")
            file.readlines()
            file.close()
            break
        except FileNotFoundError:
            user_input24 = input("No such file was found re-enter the file name or esc to exit")
            if user_input24 == "esc":
                main_menu("null")
            else:
                try:
                    rd_file = input("enter the name for race details file")
                    if rd_file[-4] + rd_file[-3] + rd_file[-2] + rd_file[-1] == ".txt":
                        pass
                    else:
                        rd_file = rd_file + ".txt"
                except IndexError:
                    rd_file = rd_file + ".txt"


    try:
        file1 = open(dr_file, "r")
        driver = file1.readlines()
        file1.close()
        for object in driver:
            content = int(object[27]+object[28])
            if object[88] =="0":
                pass
            elif object[88]!='0':
                content = int(object[87]+object[88])
    except FileContentError:
        print("file indexing is incorrect")
        main_menu("null")
    except ValueError:
        print("file content is incorrect")
        main_menu("null")
    try:
        file2 = open(rd_file,"r")
        race = file2.readlines()
        file2.close()
        count =0
        length =0
        t_length =0
        for r_object in race:
            length = len(r_object)
            t_length+=length
            count+=1
            if count ==1 and r_object[0] !="n":
                raise  FileContentError
            elif count == 1 and r_object[25] != "n":
                raise  FileContentError
            elif count == 2 and r_object[0] != "d":
                raise FileContentError
            elif count == 2 and r_object[25] != "d":
                raise FileContentError
            elif count == 3 and r_object[0] != "w":
                raise FileContentError
            elif count == 3 and r_object[25] != "w":
                raise FileContentError
            elif count == 4 and r_object[0] != "c":
                raise FileContentError
            elif count == 4 and r_object[25] != "c":
                raise FileContentError
        if t_length%length != 0:
            raise FileContentError
    except FileContentError:
        print("file indexing and content is incorrect")
        main_menu("null")
    for obj in race:
        race1.clear()
        for i in range(0, 352, 25):
            k = i + 25
            obj1 = obj[i:k].rstrip()
            race1.append(obj1)
        race2.append(race1.copy())
    file = open("racedetails1.csv", "w+", newline='')
    writer = csv.writer(file)
    writer.writerows(race2)
    file.close()
    for obj2 in driver:
        driver1.clear()
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for i in range(0, 91):
            if 0 <= i <= 25 and count1 == 0:
                obj3 = obj2[0:25].rstrip()
                driver1.append(obj3)
                count1 += 1
            elif 27 <= i <= 32 and count2 == 0:
                obj3 = obj2[27:32].rstrip()
                driver1.append(obj3)
                count2 += 1
            elif 34 <= i <= 58 and count3 == 0:
                obj3 = obj2[33:58].rstrip()
                driver1.append(obj3)
                count3 += 1
            elif 60 <= i <= 85 and count4 == 0:
                obj3 = obj2[60:85].rstrip()
                driver1.append(obj3)
                count4 += 1
            elif 87 <= i <= 90 and count5 == 0:
                obj3 = obj2[87:90].rstrip()
                driver1.append(obj3)
                count5 += 1
        driver2.append(driver1.copy())
    file1 = open("driverrecords1.csv","w+",newline='')
    writer1 = csv.writer(file1)
    writer1.writerows(driver2)
    file1.close()


def main_menu(console_input):
    while console_input != "esc":
        if console_input == "null":
            del console_input
            print("===================================================")
            console_input = input("->")
        elif console_input == "key":
            print("ADD for adding driver details")
            print("DDD for deleting")
            print("UDD for updating driver details")
            print("VCT for viewing the rally cross standings table")
            print("Type SRR for simulating a random race")
            print("VRL for viewing race table sorted according to the date")
            print("STF to save the current data to a text file")
            print("RFF to load data from the saved text file")
            print("ESC to exit the program")
            main_menu("null")
        elif console_input == "add":
            add_record()
            main_menu("null")
        elif console_input =="udd":
            udd_record()
            main_menu("null")
        elif console_input == "ddd":
            ddd_record()
            main_menu("null")
        elif console_input == "vct":
            vct()
            main_menu("null")
        elif console_input == "srr":
            srr()
            main_menu("null")
        elif console_input == "vrl":
            vrl()
            main_menu("null")
        elif console_input == "stf":
            stf()
            main_menu("null")
        elif console_input =="rff":
            rff()
            main_menu("null")
        else:
            print("wrong input")
            console_input =input("->")


main_menu("null")



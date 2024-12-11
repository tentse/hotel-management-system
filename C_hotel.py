
# MODULE IMPORTING
import random
import datetime
import mysql.connector
import string
import calendar

#------------------------------------------------------------------------------------------------

# LIST
customer_no = []
room_number = []
ratings = []

# VARIABLE
num_of_room_booked = 0     # keeping track of the number of room book to maintain not overflow

# Mysql connnector object to store the information of individual customer details
mysql_connector = None
cursor = None

#------------------------------------------------------------------------------------------------

# Database creation funtion
def establishing_database_tables():
    global mysql_connector
    global cursor
    mysql_connector = mysql.connector.connect(host='localhost', user='root', password='ten-tsering', database='Cee_Hotel')
    cursor = mysql_connector.cursor()
    first_q = 'drop table if exists customerdetails'
    second_q = 'drop table if exists ratings'
    cursor.execute(first_q)
    cursor.execute(second_q)
    table_q = 'create table customerdetails(CUSTOMER_NO int, CUSTOMER_NAME varchar(20), ROOM_NO int, PHONE_NO varchar(10), DATE_TIME_OF_CHECKIN varchar(50), EMAIL varchar(50))'
    cursor.execute(table_q)
    rating_q = 'create table ratings(CUSTOMER_NO int, CUSTOMER_NAME varchar(30), RATING int)'
    cursor.execute(rating_q)
    mysql_connector.commit()

# Dropping existing table and Creating new table for Cee_Hotel database
establishing_database_tables()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTIONS

# Home Page function
def Home_page():
    print(
        '\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600********\U0001f600')
    print(
        '\U0001f600                                                                                                             \U0001f600')
    print(
        '\U0001f600                                                                                                             \U0001f600')
    print(
        '\U0001f600                                WELCOME TO Cee TAJ HOTEL                                                     \U0001f600')
    print(
        '\U0001f600                                                                                                             \U0001f600')
    print(
        '\U0001f600                                                                                                             \U0001f600')
    print(
        '\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600*********\U0001f600********\U0001f600\n')
    print('Please Select one of the operation from given option below \U0001F447')
    print('\t\t\t 1. For booking room')
    print('\t\t\t 2. For fetching personal information')
    print('\t\t\t 3. For Check-Out ')
    print('\t\t\t 4. Check Customer Rating')
    print('\t\t\t 5. Check the calender\n')

    while True:
        choice = input('\t Enter the choice \U0001F449 ')
        if choice.isalpha() or choice == '' or ' ' in choice:
            print('---------------------------------------------------')
            print('\t\tPlease enter a valid choice')
            print('---------------------------------------------------')
            continue
        if int(choice) not in range(1, 6):
            print('---------------------------------------------------')
            print('\t\tPlease enter a valid choice number :( ')
            print('---------------------------------------------------')
        else:
            if int(choice) == 1:
                booking()
            elif int(choice) == 2:
                Info()
            elif int(choice) == 3:
                Checkout()
            elif int(choice) == 4:
                total_rating()
            elif int(choice) == 5:
                print(calendar.calendar(2021))
            break

# Booking page function
def booking():
    global num_of_room_booked
    if num_of_room_booked != 3:
        print(
            '----------------------------------------------------------------------------------------------------------',
            '\n')
        print('\tDEAR CUSTOMER KINDLY NOTE THAT YOU ARE IN THE BOOKING SECTION')
        while True:
            print()
            customername = str(input("\tKindly Enter Your Name \U0001F449 "))
            customername = string.capwords(customername)
            phone_number = str(input('\tKindly Enter Your phone number \U0001F449 '))
            if len(phone_number) != 10 or not (phone_number.isdigit()):
                print('---------------------------------------------------------------------------------------------------------')
                print('Please ', customername,
                      ' enter your phone number correctly once again we are redirecting you to fill the form again :( ')
                print(
                    "\t\t\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614")
                continue
            address = str(input('\tKindly Enter Your Home Address like(Bylakuppe, Dharamshala) \U0001F449 '))
            email_address = str(input('\tKindly Enter your email address \U0001F449 '))
            if ' ' in email_address or '@' not in email_address or '.com' not in email_address:
                print('---------------------------------------------------------------------------------------------------------')
                print('\tPlease ', customername,
                      ' enter a valid email address. We are redirecting you to fill the form again :( ')
                print(
                    "\t\t\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614\t\t\U0001F614")
                continue
            if customername != '':
                cust_no = random.randrange(1,11)
                while True:
                    if cust_no in customer_no:
                        cust_no = random.randrange(1,11)
                    else:
                        break
                room_no = random.randrange(100, 111)
                while True:
                    if room_no in room_number:
                        room_no = random.randrange(100, 111)
                    else:
                        break
                customer_no.append(cust_no)  # appending the customer number to the customer number list
                room_number.append(room_no)  # appending the room number to the room_number list
                date = str(datetime.datetime.now())  # generating the current date and time to store in database
                mysql_query = "insert into CustomerDetails values('{0}','{1}',{2},'{3}','{4}','{5}')".format(cust_no,customername,room_no,phone_number,date,email_address)
                cursor.execute(mysql_query)
                mysql_connector.commit()
                print('--------------------------------------------------------------------------------------------------')
                print('\tYour Recorded has been succesfully entered \U0001F44D \n')
                print('\tDear "', customername, '", Please note your customer_number for fetching your details later !')
                print('\tYour customer_number is ', cust_no)
                print(
                    '--------------------------------------------------------------------------------------------------')
                num_of_room_booked += 1
                break
            else:
                print('\tPlease Enter the form again somthing went wrong and kindly enter the value carefully :( ')

    else:
        print(
            "\n\t\t\t\t\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614"'\n')
        print('\t\tDear customer all room are full sorry for the inconvience :( ')
        print('\t\tKindly wait until room get empty :( ')
        print('\t\tSSSSSOOOOOOORRRRRRYYYYY !!!!!!\n')
        print("\t\t\t\t\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614""\U0001F614")

# Info page function
def Info():
    print('---------------------------------------------------------------------------------------------------------')
    print('\tKindly note that you are in the Fetching information section \n')
    input_cust_no = input('\t\t\tEnter your customer number \U0001F449 ')
    if input_cust_no == '' or not(input_cust_no.isdigit()):
        print('\tDear customer please enter a valid customer number')
    elif int(input_cust_no) in customer_no:
        info = "select*from customerdetails where customer_no={}".format(input_cust_no)
        cursor.execute(info)
        print('------------------------------------------------------------------------------------------------------')
        data = cursor.fetchone()
        print('\t\tYour data of customer_number ', input_cust_no, ' is as follow \U0001F447\n')
        print('\t\tCUSTOMER NO          : ', data[0], '\n\t\tCUSTOMER NAME        : ', data[1],
              '\n\t\tROOM NO              : ', data[2], '\n\t\tPHONE NO             : ', data[3],
              '\n\t\tDATE TIME OF CHECKIN : ', data[4], '\n\t\tEMAIL                : ', data[5])
        print('------------------------------------------------------------------------------------------------------')
    else:
        print('X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \n')
        print('\t\t\tINVALID CUSTOMER NUMBER\n')
        print('X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X ')

# Checkout page function
def Checkout():
    global num_of_room_booked
    print('----------------------------------------------------------------------------------------------------------')
    print('\tDear customer kindly note that you are in the ROOM CHECKOUT session :- \n')
    cus_no = input('Kindly enter your customer_number as provided at the begining \U0001F449 ')
    if cus_no == '' or cus_no.isalpha() or ' ' in cus_no:
        print('\n\t\tPlease enter a valid customer number as provided at the very first :( ')
    elif int(cus_no) in customer_no:
        print('Your Info as follows : ')
        q = 'select * from customerdetails where customer_no = {}'.format(cus_no)
        cursor.execute(q)
        data = cursor.fetchone()
        q1 = 'select customer_name from customerdetails where customer_no = {}'.format(cus_no)
        cursor.execute(q1)
        name = cursor.fetchone()
        name = name[0]
        print('\t\tYour data of customer_number ', cus_no, ' is as follow :-')
        print('\t\tCUSTOMER NO          : ', data[0], '\n\t\tCUSTOMER NAME        : ', data[1],
              '\n\t\tROOM NO              : ', data[2], '\n\t\tPHONE NO             : ', data[3],
              '\n\t\tDATE TIME OF CHECKIN : ', data[4], '\n\t\tEMAIL                : ', data[5])
        conformation = input("\tDear Customer Do you really want to check out ? (y/n)  -> ")
        if conformation.lower() != 'n':
            q2 = 'delete from customerdetails where customer_no = {}'.format(cus_no)
            cursor.execute(q2)
            mysql_connector.commit()
            num_of_room_booked -= 1
            room_num = customer_no.index(int(cus_no))
            customer_no.remove(int(cus_no))
            room_number.pop(room_num)
            print(name)
            print('\tDear customer You have been successfully check out from Hotel Cee :) ')
            print('\tHope you have enjoy the grand Hotel_Cee PLease do visit again ')
            rating = int(input('\tDear customer please give us rating out of 10 -> '))
            q3 = "insert into ratings values({0},'{1}',{2})".format(cus_no, name, rating)
            ratings.append(rating)
            cursor.execute(q3)
            mysql_connector.commit()
            print('\tThank You And Have A Nice Day :) ')

    else:
        print('X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \n')
        print('\t\t\tCUSTOMER NUMBER ', cus_no, ' NOT FOUND IN THE DATABASE\n')
        print('X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X ')

# Total rating funtion
def total_rating():
    if not(ratings == []):
        q = 'select sum(rating) from ratings'
        cursor.execute(q)
        total_rating = cursor.fetchone()
        num = total_rating[0]
        q1 = 'select count(*) from ratings'
        cursor.execute(q1)
        avg_rage = cursor.fetchone()
        avg = avg_rage[0]
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('\t\tThe total rating of the Hotel is \U0001F449 ', num, ' out of ', avg*10)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    else:
        print(
            'X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X \n')
        print('\t\t\tRating is empty :( \n')
        print(
            'X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X ')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#MAIN PART OF THE PROGRAM
# FUNCTION CALL
choice = 'y'
while choice.lower() == 'y':
    Home_page()
    choice = input('\nDo you wish to run the program agian ? (y/n) \U0001F449 ')
    print()
    if choice.lower() == 'n':
        print('Are you sure you want to exit the program (y/n) \U0001F449 ', end='')
        choice = input()
        print()
        if choice.lower() == 'y':
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('\t\tDEAR USER THIS MESSAGE IS FROM THE FOUNDER OF CEE_HOTEL PROGRAM')
            print('\t\t"Hope You have enjoy my project which is on hotel management system, just a brief program to tell you how actually the big application or software works"')
            print('\t\t"THANK YOU FOR TESTING MY PROJECT"')
            print("\t\t\t\U0001f600",'HAVE A NICE DAY AND A SWEET DAY ',"\U0001f600")
            print('---------------------------------------------------------------------------------------------------------------------------------------')
            break
        else:
            choice = 'y'
    elif choice == '' or choice!='y' and choice!='n':
        print('\tPlease enter a valid choice :( \n')
        choice = input('Do you wish to run the program again ? (y/n) \U0001F449 ')


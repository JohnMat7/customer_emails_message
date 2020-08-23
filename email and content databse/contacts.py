import re


def details():
    while True:
        email = input("Please enter your email id    :")
        if check_email(email) == True:
            break
    while True:
        phone_num = input("Please enter your phone  number    :")
        if check_number(phone_num) == True:
            break

    subject = input("Please enter your subject    :")
    message = input("Message    :")
    # to add data to the file
    data_customer(email, phone_num, subject, message)


def check_email(email):
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(pattern, email):
        return True
    else:
        print("***********Hey please enter valid email*****************")
        return False


def check_number(phone_num):
    if len(phone_num) == 10:
        return True
    else:
        print("***********Hey please enter valid number****************")
        return False


def data_customer(email, phone_num, subject, message):
    data = open('database.txt', 'a+')
    data.write(
        f'\nEmail : {email}\nPhone number : {phone_num}\nSubject : {subject}\nMessage : {message}\n')
    data.write('\n************NEW VISITOR**************\n')
    data.close()
    return


if __name__ == "__main__":
    details()
    print("Thanks for entering details , i will be in touch very soon ")

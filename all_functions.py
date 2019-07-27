from book import BookClass
from faculty import FacultyClass
from student import StudentClass
import datetime
import pickle


def load_student():
    with open("student_data.pkl",'rb') as f:
        StudentClass.student_list = pickle.load(f)


def dump_student():
    with open("student_data.pkl", 'wb') as f:
        pickle.dump(StudentClass.student_list,f)


def load_faculty():
    with open("faculty_data.pkl", 'rb') as f:
        FacultyClass.faculty_list = pickle.load(f)


def dump_faculty():
    with open("faculty_data.pkl", 'wb') as f:
        pickle.dump(FacultyClass.faculty_list,f)


def load_book():
    with open("book_data.pkl", 'rb') as f:
        BookClass.book_list=pickle.load(f)


def dump_book():
    with open("book_data.pkl", 'wb') as f:
        pickle.dump(BookClass.book_list,f)


def check_s(roll):
    n = len(StudentClass.student_list)
    for i in range(n):
        if str(StudentClass.student_list[i].std_roll) == roll:
            print("Already exits")
            return False
    return True


def check_f(faculty_d):
    for x in FacultyClass.faculty_list:
        if x.faculty_id==faculty_d:
            print("Already Exists")
            return False
    return True


def check_b(isbn):
    for obj in BookClass.book_list:
        if obj.isbn == isbn:
            print('Book with same ISBN exists, cannot add this book')
            return False
    else:
        return True


def add_student():
    name = input("Enter your name::")
    while True:
        year = int(input("Enter the year of addmission::"))
        if year > datetime.date.today().year:
            print("Invalid Year!! Try Again")
        else:
            break
    branch = input("Enter Your Branch::")
    while True:
        admn_id_no = input("Enter the admission id::")
        if len(admn_id_no) != 4:
            print("Invalid!!,Try Again")
        else:
            break
    std_roll = str(year) + "0187" + str(branch) + str(admn_id_no)
    load_student()
    if check_s(std_roll):
        s=StudentClass(name, year, branch, admn_id_no, std_roll)
        StudentClass.student_list.append(s)
        dump_student()


def add_faculty():
    name = input('Enter Your Name:: ')
    faculty_id=input('Enter Your ID:: ')
    while True:
        if len(faculty_id) != 5:
            print('Invalid!!,Try again')
            faculty_id = input('Enter Your ID:: ')
        else:
            faculty_id = int(faculty_id)
            break
    load_faculty()
    if check_f(faculty_id):
        f=FacultyClass(name, faculty_id)
        FacultyClass.faculty_list.append(f)
        dump_faculty()


def add_book():
    load_book()
    title = input('Enter Book Title:: ')
    author = input('Enter Author Name:: ')
    isbn = input('Enter ISBN number:: ')
    while True:
        if len(isbn) != 13:
            print('Invalid ISBN, Try again')
            isbn = input('Enter ISBN number:: ')
        else:
            isbn = int(isbn)
        break
    no_of_copies = int(input('Enter number of copies : '))
    if check_b(isbn):
        book_obj = BookClass(title, author, isbn, no_of_copies)
        BookClass.book_list.append(book_obj)
        dump_book()


def check_for_roll(roll):
    for i in range(len(StudentClass.student_list)):
        if str(StudentClass.student_list[i].std_roll) == roll:
            print('Student found !')
            return True, i
    else:
        print('Student not found !')
    return False, ''


def book_limit(i):
    if len(StudentClass.student_list[i].books) < 3:
        return True
    print('book cannot be issued to you, max limit is 3')
    return False


def check_isbn(isbn):
    for i in range(len(BookClass.book_list)):
        if BookClass.book_list[i].isbn == isbn:
            print('Book Found')
            return True, i
    return False, ''


def check_number_of_copies(book_obj):
    if book_obj.num_of_copies > 0:
        return True
    else:
        return False


def check_already_issued(i, book_obj):
    for s in StudentClass.student_list[i].books:
        if s.isbn == book_obj.isbn:
            print("You have same copy, Can't issue another copy")
            return False
    return True


def issue_book_to_student():
    roll = input('Enter Student roll No :: ')
    load_book()
    load_student()
    check_roll, i = check_for_roll(roll)
    if check_roll:
        if book_limit(i):
            isbn = input('Enter ISBN number:: ')
            while True:
                if len(isbn) != 13:
                    print('Invalid ISBN, Try again')
                    isbn = input('Enter ISBN number:: ')

                else:
                    isbn = int(isbn)
                    break
            b_isbn, book_index = check_isbn(isbn)
            if b_isbn:
                if check_number_of_copies(BookClass.book_list[book_index]):
                    if check_already_issued(i, BookClass.book_list[book_index]):
                        b_object = BookClass.book_list[book_index]
                        StudentClass.student_list[i].books.append(b_object)
                        BookClass.book_list[book_index].num_of_copies -= 1
                        print('Book Issued')
                else:
                    print('Book not available')
            else:
                print('Book not valid, Please try again')
            dump_book()
            dump_student()

def faculty_id_check(id):
    for i in range(len(FacultyClass.faculty_list)):
        if FacultyClass.faculty_list[i].faculty_id == int(id):
            print('Faculty data found')
            return True, i
    else:
        print('Faculty data not available')
    return False, ''

def check_isbn_f(isbn, n):
    for i in range(len(BookClass.book_list)):
        if BookClass.book_list[i].isbn == isbn and BookClass.book_list[i].num_of_copies >= n:
            print('Book data found')
            return True, i
    return False, ''

def issue_book_to_faculty():
    load_faculty()
    load_book()
    f_id = input('Enter Employee Id:: ')
    check_f_id, i = faculty_id_check(f_id)
    if check_f_id:
        isbn = int(input('Enter isbn:: '))
        n = int(input('Enter no of copies : '))
        c_isbn, b_index = check_isbn_f(isbn, n)
        if c_isbn:
            b = [BookClass.book_list[b_index], n]
            FacultyClass.faculty_list[i].books.append(b)
            BookClass.book_list[b_index].num_of_copies -= n
            print('Book issued successfully')
        else:
            print('Cannot issue book')
    else:
        print(f'Employee not present. Cannot issue book.')
    dump_book()
    dump_faculty()

def check_book_student(isbn, i):
    for b in range(len(StudentClass.student_list[i].books)):
        if StudentClass.student_list[i].books[b].isbn == isbn:
            return True, b
    return False, ''

def return_by_student():
    load_student()
    load_book()
    roll = input('Enter student roll no:: ')
    c_roll, i = check_for_roll(roll)
    if c_roll:
        isbn = int(input('Enter book isbn::'))
        c_isbn, b_index = check_book_student(isbn, i)
        if c_isbn:
            b = StudentClass.student_list[i].books.pop(b_index)
            dump_student()
            b_i, book_index2 = check_isbn(isbn)
            if b_i:
                BookClass.book_list[book_index2].num_of_copies += 1
            else:
                b.num_of_copies += 1
                BookClass.book_list.append(b)
            dump_book()
            print('Return successfull')
        else:
            print("wrong book information ")
def return_by_faculty():
    load_faculty()
    load_book()
    faculty_id = input('Enter faculty id:: ')
    x_faculty_id, i = faculty_id_check(faculty_id)
    if x_faculty_id:
        isbn = int(input('Enter book isbn number::'))
        a_isbn, b_index = check_isbn_f(isbn, i)
        if a_isbn:
            b = FacultyClass.faculty_list[i].books.pop(b_index)
            dump_faculty()
            b_i, book_i = check_isbn(b[0].isbn)
            if b_i == True:
                BookClass.book_list[book_i].num_of_copies += b[1]
            else:
                b[0].num_of_copies += b[1]
                BookClass.book_list.append(b[0])
            print('Book returned')
        else:
            print('invalid book')
        dump_book()

def book_search():
    load_book()
    print("Book Search ::\n1.isbn\n2.author name\n3.book title")
    n=int(input("Enter Your choice::"))
    sea=input("Enter book to search::")
    if n==1:
        for x in BookClass.book_list:
            if x.isbn==int(sea):
                print("Your Book is here!!")
                x.display()
                break
        else:
            print("Book Not found")
    elif n==2:
        for x in BookClass.book_list:
            if x.author==sea:
                print("Your Book is here!!")
                x.display()
                break
        else:
            print("Book Not Found")
    elif n == 3:
        for x in BookClass.book_list:
            if x.title==sea:
                print("Your Book is here!!")
                x.display()
                break
        else:
            print("Book Not Found")
    else:
        print("Invalid coice")


def print_student():
    print("**************************************************")
    load_student()
    for x in StudentClass.student_list:
        x.display()
    print("**************************************************")


def print_faculty():
    print("**************************************************")
    load_faculty()
    for x in FacultyClass.faculty_list:
        x.display()
    print("**************************************************")


def print_book():
    print("**************************************************")
    load_book()
    for x in BookClass.book_list:
        x.display()
    print("**************************************************")

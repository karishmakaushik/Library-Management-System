from all_functions import*
import sys
while True:
    print("**************************************************")
    print('************Library Managemnet System**************')
    print("**************************************************")
    print('1.Add a Student member to library \n2.Add Faculty member to library\n3.Add Book to library\n'
          '4.Issue book to student\n5.Issue book to faculty \n6.Return book by Student \n7.Return book by Faculty\n'
          '8.Search for a Book in library\n9.Print Student records\n10.Print Faculty record\n11.Print Book record\n12.Exit')
    ch=int(input("Enter Your Choice::"))
    if ch == 1:
        add_student()
    elif ch == 2:
        add_faculty()
    elif ch == 3:
        add_book()
    elif ch == 4:
        issue_book_to_student()
    elif ch == 5:
        issue_book_to_faculty()
    elif ch == 6:
        return_by_student()
    elif ch== 7:
        return_by_faculty()
    elif ch == 8:
        book_search()
    elif ch == 9:
        print_student()
    elif ch == 10:
        print_faculty()
    elif ch == 11:
        print_book()
    elif ch == 12:
        sys.exit("Exit")
    print("**************************************************")
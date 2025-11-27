from library import Library

lib = Library()

print("\n=== WELCOME TO SIMPLE LIBRARY SYSTEM ===\n")

while True:
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        t = input("Enter title: ")
        a = input("Enter author: ")
        i = input("Enter ISBN: ")
        lib.add_book(t, a, i)
        print("Book Added.\n")

    elif choice == "2":
        n = input("Enter member name: ")
        mid = input("Enter member ID: ")
        lib.register_member(n, mid)
        print("Member Registered.\n")

    elif choice == "3":
        mid = input("Member ID: ")
        isbn = input("Book ISBN: ")
        if lib.lend_book(mid, isbn):
            print("Book Borrowed.\n")
        else:
            print("Borrow Failed.\n")

    elif choice == "4":
        mid = input("Member ID: ")
        isbn = input("Book ISBN: ")
        if lib.take_return(mid, isbn):
            print("Book Returned.\n")
        else:
            print("Return Failed.\n")

    elif choice == "5":
        print(lib.analytics())
        print()

    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.\n")



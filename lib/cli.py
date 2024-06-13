# lib/cli.py

from colorama import Fore, Style

from helpers import (
    exit_program,
    list_tenants,
    find_tenant_by_name,
    find_tenant_by_id,
    create_tenant,
    update_tenant,
    delete_tenant,
    list_apartments,
    find_apartment_by_address,
    find_apartment_by_id,
    delete_apartment,
    create_apartment,
    update_apartment,
    list_leases,
    find_lease_by_id,
    find_leases_by_apartment_id,
    find_leases_by_tenant_id,
    create_lease,
    update_lease,
    delete_lease
)


def main():
    user_name = input(Fore.GREEN+ "Please input your name to continue \n")
    print(f"Welcome, {user_name} to Thika Flats Management System(TFMS) \nLooking forward to making your life easier. \nYou can call this the best AirBnB in town!" + Style.RESET_ALL)
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == '1':
            list_tenants()
        elif choice == '2':
            find_tenant_by_name()
        elif choice == '3':
            find_tenant_by_id()
        elif choice == '4':
            create_tenant()
        elif choice == '5':
            update_tenant()
        elif choice == '6':
            delete_tenant()
        elif choice == '7':
            list_apartments()
        elif choice == '8':
            find_apartment_by_address()
        elif choice == '9':
            find_apartment_by_id()
        elif choice == '10':
            create_apartment()
        elif choice == '11':
            update_apartment()
        elif choice == '12':
            delete_apartment()
        elif choice == '13':
            list_leases()
        elif choice == '14':
            find_lease_by_id()
        elif choice == '15':
            find_leases_by_apartment_id()
        elif choice == '16':
            find_leases_by_tenant_id()
        elif choice == '17':
            create_lease()
        elif choice == '18':
            update_lease()
        elif choice == '19':
            delete_lease()
        else:
            print("Invalid choice. Please try again.")


def menu():
    print(Fore.CYAN +"\nThika Flats Management System(TFMS)")
    print("1. List Tenants")
    print("2. Find Tenant by Name")
    print("3. Find Tenant by ID")
    print("4. Create Tenant")
    print("5. Update Tenant")
    print("6. Delete Tenant")
    print("7. List Apartments")
    print("8. Find Apartment by Address")
    print("9. Find Apartment by ID")
    print("10. Create Apartment")
    print("11. Update Apartment")
    print("12. Delete Apartment")
    print("13. List Leases")
    print("14. Find Lease by ID")
    print("15. Find leases by apartment id")
    print("16. Find leases by tenant id")
    print("17. Create Lease")
    print("18. Update Lease")
    print("19. Delete Lease")
    print("0. Exit" + Style.RESET_ALL )


if __name__ == "__main__":
    main()

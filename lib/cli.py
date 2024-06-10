# lib/cli.py

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
    create_lease,
    update_lease,
    delete_lease
)


def main():
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
            create_lease()
        elif choice == '16':
            update_lease()
        elif choice == '17':
            delete_lease()
        else:
            print("Invalid choice. Please try again.")


def menu():
    print("\nWelcome to Thika Flats Management System(TFMS)")
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
    print("15. Create Lease")
    print("16. Update Lease")
    print("17. Delete Lease")
    print("0. Exit")


if __name__ == "__main__":
    main()

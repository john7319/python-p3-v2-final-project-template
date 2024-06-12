# lib/helpers.py
from colorama import init, Fore, Style, Back
from models.house import Apartment
from models.rent import Lease
from models.tenant import Tenant

init()

def list_tenants():
    tenants = Tenant.get_all()
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Listing Tenants..." +Style.RESET_ALL)
    print(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Here are the tenants that are at your apartment:"+ Style.RESET_ALL)
    for tenant in tenants:
        print(Fore.GREEN + f"Tenant name is {tenant.name} and the contact is {tenant.contact_info}" + Style.RESET_ALL)

def find_tenant_by_name():
    print( Back.BLACK+ Fore.CYAN + Style.BRIGHT +"Finding Tenant by name..." +Style.RESET_ALL)
    name = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's name: " +Style.RESET_ALL)
    tenant = Tenant.find_by_name(name)
    print(Fore.YELLOW + f'{tenant}' + Style.RESET_ALL) if tenant else print(Fore.YELLOW +f'Tenant {name} not found'+ Style.RESET_ALL)

def find_tenant_by_id():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Finding Tenant by Id..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's id: " +Style.RESET_ALL)
    tenant = Tenant.find_by_id(id_)
    print(Fore.YELLOW + f'{tenant}'+ Style.RESET_ALL) if tenant else print(Fore.YELLOW + f'Tenant {id_} not found'+ Style.RESET_ALL)

def create_tenant():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Creating a tenant..." +Style.RESET_ALL)
    name = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's name: " +Style.RESET_ALL)
    contact_info = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's contact info: " +Style.RESET_ALL)
    try:
        tenant = Tenant.create(name, contact_info)
        print(Fore.YELLOW + f'Success: {tenant}'+ Style.RESET_ALL)
    except Exception as exc:
        print(Fore.YELLOW + "Error creating tenant: ", exc + Style.RESET_ALL)

def update_tenant():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Updating a tenant..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's id: ")
    if tenant := Tenant.find_by_id(id_):
        try:
            name = input("Enter the tenant's new name: ")
            tenant.name = name
            contact_info = input("Enter the tenant's new contact info: " +Style.RESET_ALL)
            tenant.contact_info = contact_info
            tenant.update()
            print(Fore.YELLOW + f'Success: {tenant}' + Style.RESET_ALL)
        except Exception as exc:
            print(Fore.YELLOW + "Error updating tenant: ", exc + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'Tenant {id_} not found' + Style.RESET_ALL)

def delete_tenant():
    print(Back.BLACK+ Fore.RED + Style.BRIGHT +"Deleting a tenant..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's id: " +Style.RESET_ALL)
    if tenant := Tenant.find_by_id(id_):
        tenant.delete()
        print(Fore.YELLOW + f'Tenant {id_} deleted'+ Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'Tenant {id_} not found'+ Style.RESET_ALL)

# Apartment CLI functions
def list_apartments():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Listing apartments..." +Style.RESET_ALL)
    apartments = Apartment.get_all()
    for apartment in apartments:
        print(Fore.YELLOW + f'{apartment}')

def find_apartment_by_address():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Finding apartment by address..." +Style.RESET_ALL)
    address = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the apartment's address: " +Style.RESET_ALL)
    apartment = Apartment.find_by_address(address)
    print(Fore.YELLOW + f'{apartment}' + Style.RESET_ALL) if apartment else print(Fore.YELLOW + f'Apartment {address} not found'+ Style.RESET_ALL)

def find_apartment_by_id():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Finding apartment by Id..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the apartment's id: " +Style.RESET_ALL)
    apartment = Apartment.find_by_id(id_)
    print(Fore.YELLOW + f'{apartment}' + Style.RESET_ALL) if apartment else print(Fore.YELLOW + f'Apartment {id_} not found' + Style.RESET_ALL)

def create_apartment():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Creating apartment..." +Style.RESET_ALL)
    address = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the apartment's address: ")
    rent = float(input("Enter the apartment's rent: "))
    availability = int(input("Is the apartment available. (Type 1 for available and 0 for occupied)?" +Style.RESET_ALL))
    availability1 = True if availability == 1 else False
    try:
        apartment = Apartment.create(address, rent, availability1)
        print(Fore.YELLOW + f'Success: {apartment}' + Style.RESET_ALL)
    except Exception as exc:
        print(Fore.YELLOW + "Error creating apartment: ", exc + Style.RESET_ALL)

def update_apartment():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Updating apartment..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the apartment's id: ")
    if apartment := Apartment.find_by_id(id_):
        try:
            address = input("Enter the apartment's new address: ")
            apartment.address = address
            rent = float(input("Enter the apartment's new rent: "))
            apartment.rent = rent
            availability = int(input("Is the apartment available (Type 1 for available and 0 for occupied)? " + Style.RESET_ALL))
            if availability == 1:
                apartment.availability = True
            else:
                apartment.availability = False
            apartment.update()
            print(Fore.YELLOW + f'Success: {apartment}' + Style.RESET_ALL)
        except Exception as exc:
            print(Fore.YELLOW + "Error updating apartment: ", f'{exc}' + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'Apartment {id_} not found' + Style.RESET_ALL)

def delete_apartment():
    print(Back.BLACK+ Fore.RED + Style.BRIGHT +"Deleting apartment..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the apartment's id: " +Style.RESET_ALL)
    if apartment := Apartment.find_by_id(id_):
        apartment.delete()
        print(Fore.YELLOW + f'Apartment {id_} deleted' + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'Apartment {id_} not found' + Style.RESET_ALL)

# Lease CLI functions
def list_leases():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Listing leases provided..." +Style.RESET_ALL)
    leases = Lease.get_all()
    for lease in leases:
        print(Fore.YELLOW + f"Lease ID: {lease[0]}, Tenant: {lease[1]}, Apartment: {lease[2]}, Start Date: {lease[3]}, End Date: {lease[4]}"+ Style.RESET_ALL)

def find_lease_by_id():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Finding a lease by Id..." +Style.RESET_ALL)
    tenant_id = input("Enter the tenant's id: ")
    leases = Lease.find_by_tenant_id(tenant_id)
    if leases:
        for lease in leases:
            apartment = Apartment.find_by_id(lease.apartment_id)
            print(f"Lease ID: {lease.id}, Tenant: {lease.tenant_id}, Apartment: {apartment.address}, Start Date: {lease.start_date}, End Date: {lease.end_date}")
    else:
        print(f'No leases found for tenant {tenant_id}')
    
def find_leases_by_tenant_id():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Finding a lease by tenant Id..." +Style.RESET_ALL)
    tenant_id = input("Enter the tenant's id: ")
    leases = Lease.find_by_tenant_id(tenant_id)
    if leases:
        for lease in leases:
            apartment = Apartment.find_by_id(lease.apartment_id)
            print(f"Lease ID: {lease.id}, Tenant: {lease.tenant_id}, Apartment: {apartment.address}, Start Date: {lease.start_date}, End Date: {lease.end_date}")
    else:
        print(f'No leases found for tenant {tenant_id}')
        
def find_leases_by_apartment_id():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Finding a lease apartment Id..." +Style.RESET_ALL)
    apartment_id = input("Enter the apartment's id: ")
    leases = Lease.find_by_apartment_id(apartment_id)
    if leases:
        for lease in leases:
            tenant = Tenant.find_by_id(lease.tenant_id)
            print(f"Lease ID: {lease.id}, Tenant: {tenant.name}, Apartment: {lease.apartment_id}, Start Date: {lease.start_date}, End Date: {lease.end_date}")
    else:
        print(f'No leases found for apartment {apartment_id}')

def create_lease():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Creating a new Lease..." +Style.RESET_ALL)
    tenant_id = int(input(Back.BLACK+ Fore.WHITE + Style.BRIGHT +"Enter the tenant's id: "))
    apartment_id = int(input("Enter the apartment's id: "))
    start_date = input("Enter the lease start date (YYYY-MM-DD): ")
    end_date = input("Enter the lease end date (YYYY-MM-DD): " +Style.RESET_ALL)
    try:
        lease = Lease.create(tenant_id, apartment_id, start_date, end_date)
        print(Fore.YELLOW + f'Success: {lease}' + Style.RESET_ALL)
    except Exception as exc:
        print(Fore.YELLOW + "Error creating lease: ", exc + Style.RESET_ALL)

def update_lease():
    print(Back.BLACK+ Fore.BLUE + Style.BRIGHT +"Updating a Lease..." +Style.RESET_ALL)
    id_ = input("Enter the lease's id: ")
    if lease := Lease.find_by_id(id_):
        try:
            tenant_id = input("Enter the tenant's id: ")
            lease.tenant_id = tenant_id
            apartment_id = input("Enter the apartment's id: ")
            lease.apartment_id = apartment_id
            start_date = input("Enter the lease start date (YYYY-MM-DD): ")
            lease.start_date = start_date
            end_date = input("Enter the lease end date (YYYY-MM-DD): ")
            lease.end_date = end_date
            lease.update()
            print(f'Success: {lease}')
        except Exception as exc:
            print("Error updating lease: ", exc)
    else:
        print(f'Lease {id_} not found')
def delete_lease():
    print(Back.BLACK+ Fore.RED + Style.BRIGHT +"Deleting a lease..." +Style.RESET_ALL)
    id_ = input(Back.BLACK+ Fore.WHITE + Style.BRIGHT + "Enter the lease's id: " + Style.RESET_ALL)
    if lease := Lease.find_by_id(id_):
        lease.delete()
        print(Fore.YELLOW + f'Lease {id_} deleted' + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f'Lease {id_} not found' + Style.RESET_ALL)
def exit_program():
    print(Fore.RED +"Good Bye, I hope I served you as you wished. \nLooking forward to working with you again")
    exit()

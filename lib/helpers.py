# lib/helpers.py
from models.house import Apartment
from models.rent import Lease
from models.tenant import Tenant

def list_tenants():
    tenants = Tenant.get_all()
    for tenant in tenants:
        print("Here are the tenants that are at your apartment:")
        print(f"Tenant name is {tenant.name} and the contact is {tenant.contact_info}")

def find_tenant_by_name():
    name = input("Enter the tenant's name: ")
    tenant = Tenant.find_by_name(name)
    print(tenant) if tenant else print(f'Tenant {name} not found')

def find_tenant_by_id():
    id_ = input("Enter the tenant's id: ")
    tenant = Tenant.find_by_id(id_)
    print(tenant) if tenant else print(f'Tenant {id_} not found')

def create_tenant():
    name = input("Enter the tenant's name: ")
    contact_info = input("Enter the tenant's contact info: ")
    try:
        tenant = Tenant.create(name, contact_info)
        print(f'Success: {tenant}')
    except Exception as exc:
        print("Error creating tenant: ", exc)

def update_tenant():
    id_ = input("Enter the tenant's id: ")
    if tenant := Tenant.find_by_id(id_):
        try:
            name = input("Enter the tenant's new name: ")
            tenant.name = name
            contact_info = input("Enter the tenant's new contact info: ")
            tenant.contact_info = contact_info
            tenant.update()
            print(f'Success: {tenant}')
        except Exception as exc:
            print("Error updating tenant: ", exc)
    else:
        print(f'Tenant {id_} not found')

def delete_tenant():
    id_ = input("Enter the tenant's id: ")
    if tenant := Tenant.find_by_id(id_):
        tenant.delete()
        print(f'Tenant {id_} deleted')
    else:
        print(f'Tenant {id_} not found')

# Apartment CLI functions
def list_apartments():
    apartments = Apartment.get_all()
    for apartment in apartments:
        print(apartment)

def find_apartment_by_address():
    address = input("Enter the apartment's address: ")
    apartment = Apartment.find_by_address(address)
    print(apartment) if apartment else print(f'Apartment {address} not found')

def find_apartment_by_id():
    id_ = input("Enter the apartment's id: ")
    apartment = Apartment.find_by_id(id_)
    print(apartment) if apartment else print(f'Apartment {id_} not found')

def create_apartment():
    address = input("Enter the apartment's address: ")
    rent = float(input("Enter the apartment's rent: "))
    availability = input("Is the apartment available (yes/no)? ").lower() == 'yes'
    try:
        apartment = Apartment.create(address, rent, availability)
        print(f'Success: {apartment}')
    except Exception as exc:
        print("Error creating apartment: ", exc)

def update_apartment():
    id_ = input("Enter the apartment's id: ")
    if apartment := Apartment.find_by_id(id_):
        try:
            address = input("Enter the apartment's new address: ")
            apartment.address = address
            rent = float(input("Enter the apartment's new rent: "))
            apartment.rent = rent
            availability = input("Is the apartment available (yes/no)? ").lower() == 'yes'
            apartment.availability = availability
            apartment.update()
            print(f'Success: {apartment}')
        except Exception as exc:
            print("Error updating apartment: ", exc)
    else:
        print(f'Apartment {id_} not found')

def delete_apartment():
    id_ = input("Enter the apartment's id: ")
    if apartment := Apartment.find_by_id(id_):
        apartment.delete()
        print(f'Apartment {id_} deleted')
    else:
        print(f'Apartment {id_} not found')

# Lease CLI functions
def list_leases():
    leases = Lease.get_all()
    for lease in leases:
        print(lease)

def find_lease_by_id():
    id_ = input("Enter the lease's id: ")
    lease = Lease.find_by_id(id_)
    print(lease) if lease else print(f'Lease {id_} not found')

def create_lease():
    tenant_id = int(input("Enter the tenant's id: "))
    apartment_id = int(input("Enter the apartment's id: "))
    start_date = input("Enter the lease start date (YYYY-MM-DD): ")
    end_date = input("Enter the lease end date (YYYY-MM-DD): ")
    try:
        lease = Lease.create(tenant_id, apartment_id, start_date, end_date)
        print(f'Success: {lease}')
    except Exception as exc:
        print("Error creating lease: ", exc)

def update_lease():
    id_ = input("Enter the lease's id: ")
    if lease := Lease.find_by_id(id_):
        try:
            tenant_id = int(input("Enter the new tenant id: "))
            lease.tenant_id = tenant_id
            apartment_id = int(input("Enter the new apartment id: "))
            lease.apartment_id = apartment_id
            start_date = input("Enter the new start date (YYYY-MM-DD): ")
            lease.start_date = start_date
            end_date = input("Enter the new end date (YYYY-MM-DD): ")
            lease.end_date = end_date
            lease.update()
            print(f'Success: {lease}')
        except Exception as exc:
            print("Error updating lease: ", exc)
    else:
        print(f'Lease {id_} not found')

def delete_lease():
    id_ = input("Enter the lease's id: ")
    if lease := Lease.find_by_id(id_):
        lease.delete()
        print(f'Lease {id_} deleted')
    else:
        print(f'Lease {id_} not found')
def exit_program():
    print("Goodbye!")
    exit()

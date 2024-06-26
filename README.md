# Apartment Management System CLI

## Overview

This project is a command-line interface (CLI) tool for managing Thika Flats system. It allows users to perform CRUD (Create, Read, Update, Delete) operations on tenants, apartments, and leases. The data is stored in a SQLite database.

## Features

- **Tenant Management**
  - **You will be abe to:**
  - List all tenants
  - Find tenant by name
  - Find tenant by ID
  - Create a new tenant
  - Update an existing tenant
  - Delete a tenant

- **Apartment Management**
  - **You will be abe to:**
  - List all apartments
  - Find apartment by address
  - Find apartment by ID
  - Create a new apartment
  - Update an existing apartment
  - Delete an apartment

- **Lease Management**
  - **You will be abe to:**
  - List all leases
  - Find lease by ID
  - Create a new lease
  - Update an existing lease
  - Delete a lease

## Requirements

- Python 3.x
- SQLite3

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/john7319/python-p3-v2-final-project-template
    cd python-p3-v2-final-project-template/lib
    ```

2. **Install dependencies:**

    pipenv --python <python_source_path>
    pipenv install
    pipenv shell(to enter the environment)

3. **Set up the database:**
    Run the CLI and it will be automatically implemented
    

## Usage

1. **Run the CLI:**

    ```sh
    python cli.py
    ```

2. **Main Menu:**

    The main menu will be displayed with options to manage tenants, apartments, and leases.

    ```
    Welcome to Thika Flats Management System(TFMS)
    1. List Tenants
    2. Find Tenant by Name
    3. Find Tenant by ID
    4. Create Tenant
    5. Update Tenant
    6. Delete Tenant
    7. List Apartments
    8. Find Apartment by Address
    9. Find Apartment by ID
    10. Create Apartment
    11. Update Apartment
    12. Delete Apartment
    13. List Leases
    14. Find Lease by ID
    15. Find leases by apartment id
    16. Find leases by tenant id
    17. Create Lease
    18. Update Lease
    19. Delete Lease
    0. Exit
    ```

3. **Choose an Option:**

    Enter the number corresponding to the desired operation and follow the prompts to perform the operation.

## Project Structure

- `models/`
  - `tenant.py`: Tenant model
  - `house.py`: Apartment model
  - `rent.py`: Lease model
-apartment.db: Sql database
-debug.py: To debug any errors
-`cli.py`: Comand line interface
-`helpers.py`: Connection code
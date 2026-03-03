# Hospital Management System

Terminal-based Hospital Management System in Python — CRUD patient records stored in encrypted binary files, schedule appointments across 5 departments, and generate itemized billing invoices from the command line.

## Features

- **Patient Records**: Add, view, modify, and delete patient profiles (name, gender, DOB, phone, address)
- **Appointments**: Schedule appointments across 5 departments, each with 2 assigned doctors
- **Billing**: Generate itemized invoices based on appointment history and export receipts to a `.txt` file
- **Auto Age Calculation**: Patient age is computed dynamically from date of birth at runtime
- **Formatted Console UI**: Center-aligned menus and tables using `PrettyTable`

## Requirements

- Python 3.x
- [PrettyTable](https://pypi.org/project/prettytable/)

```bash
pip install prettytable
```

## Data Files

The program creates and manages the following files automatically:

| File               | Purpose                                      |
|--------------------|----------------------------------------------|
| `hospital.dat`     | Stores full patient records (pickle format)  |
| `patients.dat`     | Tracks appointment and billing codes         |
| `print_receipt.txt`| Exported billing receipt for a patient       |

⚠️ Do not manually edit `.dat` files, they are binary pickle files.

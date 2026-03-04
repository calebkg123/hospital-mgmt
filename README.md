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
python -m pip install -U prettytable
```

## File Structure

The program creates and manages the following files automatically:

| File               | Purpose                                      |
|--------------------|----------------------------------------------|
| `hospital.dat`     | Stores full patient records (pickle format)  |
| `patients.dat`     | Tracks appointment and billing codes         |
| `print_receipt.txt`| Exported billing receipt for a patient       |

⚠️ Do not manually edit `.dat` files, they are binary pickle files.

\
**`hospital.dat`**: each record is a dictionary in the format `{ pid: [nm, gen, dob, ph, addr, reg] }`

| Field      |Datatype| Description                          |
|------------|--------|--------------------------------------|
| `pid`      | `int`  | Patient ID                           |
| `nm`       | `str`  | Name of patient                      |
| `gen`      | `str`  | Gender of patient                    |
| `dob`      | `str`  | Date of birth of patient (dd-mm-yyyy)|
| `ph`       | `int`  | Phone number of patient              |
| `addr`     | `str`  | Address of patient                   |
| `reg`      | `str`  | Current date / Date of registration  |

\
**`patients.dat`**: each record is a dictionary in the format `{ pid: [<code1>, <code2>, ...] }`

## Appointment Codes

Appointments are stored as short 3-character codes for billing.

The first character represents the department.
| Code | Department |
|------|------------|
|`C xx`|Cardiology |
|`E xx`|ENT |
|`G xx`|General Surgery|
|`N xx`|Neurology|
|`P xx`|Physiotherapy|

The second character represents the doctor.
| Code  | Doctor        |
|-------------|----------------|
| `x 1x`        | Doctor 1  |
| `x 2x`        | Doctor 2 |

The third character represents the type of visit.
| Code  | Visit Type        |
|-------------|-------------------|
| `x x1`        | Initial Checkup   |
| `x x2`        | Follow-up Checkup |
| `x x3`        | Post-Surgery      |
| `x x4`        | Emergency         |

\
`0` represents the file opening fee, and is present for every patient.

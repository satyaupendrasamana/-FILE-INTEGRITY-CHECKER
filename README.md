# -FILE-INTEGRITY-CHECKER

*COMPANY -- CODETECH IT SOULUTIONS

*NAME -- SATYA UPENDRA SAMANA

*INTERN ID. -- CT04WX86

*DOMAIN -- CYBERSECURITY & ETHICAL HACKING

*DURATION -- 4WEEKS

*MENTOR -- NEELA SANTOSH



# File Integrity Checker

## Description
The **File Integrity Checker** is a Python-based tool designed to scan, save, and verify the integrity of files in a specified folder. It helps detect any modifications, new additions, or deletions of files by comparing their hash values.

## Features
* Scans all files in a folder and generates SHA-256 hash values.  
* Saves the file hashes in a `hashes.txt` file for future reference.  
* Verifies file integrity by comparing current file hashes with saved values.  
* Detects modified, new, and deleted files.  

## Requirements
* Python 3.x

## Installation
1. Clone this repository:
```
git clone <repository_url>
```
2. Navigate to the folder:
```
cd Task_1_File_Integrity_Checker
```
3. Install dependencies (if required):
```
pip install hashlib
```

## Usage Instructions
1. Run the Python file:
```
python file_integrity_checker.py
```
2. Select an option:
* **[1] Scan & Save Hashes**: Scans files and generates a `hashes.txt`.  
* **[2] Verify Integrity**: Verifies current files against the stored hashes.  

3. Enter the folder path when prompted (e.g., `C:\Users\shash\internships\Task_1_File_Integrity_Checker\test_folder`).

## Folder Structure
```
Task_1_File_Integrity_Checker
 ┣ test_folder
 ┃ ┣ sample1.txt
 ┃ ┣ sample2.txt
 ┃ ┗ sample3.txt
 ┣ file_integrity_checker.py
 ┣ hashes.txt
 ┗ README.md
```

## Sample Output
### Successful Scan & Save
```
Scanning files and saving hashes...
sample1.txt ➜ 1234abcd5678...
sample2.txt ➜ 9876efgh4321...
Hashes saved in: hashes.txt
```

### File Integrity Check - Modified Files Detected
```
Verifying file integrity...
Modified Files:
➔ sample1.txt
New Files Detected:
➔ new_file.txt
Deleted Files Detected:
➔ sample2.txt
```

## Credits
This project was developed as part of my **Cyber Security & Ethical Hacking Internship** at **CODTECH IT SOLUTIONS PVT. LTD.** under the guidance of my mentors.  
  And using online for help in the stuations


  ##OUPUT IMAGES
  
*256-hash vlue output

![Image](https://github.com/user-attachments/assets/97cd8367-2e14-4208-a75a-a2dcaa9dd9c4)

*Hash value store at hash.txt

![Image](https://github.com/user-attachments/assets/05cf6824-087a-4e08-8409-f4972b7a223e)

*file modified output

![Image](https://github.com/user-attachments/assets/5f2edbbd-6507-4b40-885d-e1ec09cb5035)

*file format/ task format

![Image](https://github.com/user-attachments/assets/821fb06a-52e2-409d-8466-5898a40274d0)

  
  
  


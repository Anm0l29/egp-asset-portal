import csv
import sys

def find_user_email(target_emp_id):
    csv_file = "users_list.csv"
    
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check if the Employee ID matches
                if row['Emp_ID'].strip() == target_emp_id:
                    print(f"SUCCESS: Found user {row['Full_Name']}")
                    print(f"TARGET_EMAIL={row['Email_ID'].strip()}")
                    return
            
            print(f"ERROR: Employee ID {target_emp_id} not found in database.")
            sys.exit(1)
            
    except FileNotFoundError:
        print(f"ERROR: {csv_file} file is missing in the workspace!")
        sys.exit(1)

if __name__ == "__main__":
    # Simulate scanning the portal for ID: ag51137
    target_id = "ag51137"
    find_user_email(target_id)
import csv
import os

# read file name from user
filename = input("Enter File Name: ")
gcode = input("Enter Group Code: ")

try:
    invalid = 0
    filename_short = filename.split('.')[0]
    with open(filename) as csv_file:
        # create a csv_reader
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        total_data = []

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                pass
            else:
                mobile = row[1].replace(" ", "").replace("+", '')
                name = row[1].replace(" ", "").replace(
                    "+", '') if len(row[0].replace(" ", "")) == 0 else row[0].replace(" ", "")
                if (len(mobile) < 9):
                    invalid += 1
                    pass

                elif (len(mobile) == 9):
                    mobile = '233' + mobile
                    total_data.append({'Name': name, 'Mobile': mobile,
                                       'Email': row[2], 'Group code': gcode.upper(), 'Tags': 'Tags'})
                elif (len(mobile) == 10 and mobile.startswith('0')):
                    mobile = '233'+mobile[-9:]
                    total_data.append({'Name': name, 'Mobile': mobile,
                                       'Email': row[2], 'Group code': gcode.upper(), 'Tags': 'Tags'})
                elif (mobile.startswith('233')):
                    mobile = '233' + mobile[-9:]
                    total_data.append({'Name': name, 'Mobile': mobile,
                                       'Email': row[2], 'Group code': gcode.upper(), 'Tags': 'Tags'})
                else:
                    invalid += 1
                    pass
                line_count += 1
        csv_file.close()
    # writing a new formatted file

    with open(f'{filename_short}_filtered.csv', mode='w', newline='') as filtered_file:
        fieldnames = ['Name', 'Mobile', 'Email', 'Group code', 'Tags']
        writer = csv.DictWriter(filtered_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(total_data)

        filtered_file.close()

    print(f'Data successfully written to {filename_short}_filtered.csv \n')
    print('===============================================================')
    print(f'You have {invalid} invalid numbers in your data')
    print('===============================================================')

except FileNotFoundError:
    print("File Not Found in current directory. Make sure file is in the same directory as the script Or Check Your spelling and try again.")
    exit()

import csv
import glob #globモジュールを宣言

for file in glob.glob("sample_*.txt"):
    file_data = open(file, "r")
    i = 0
    subject = name = address = text = received_time = 0
    for line in file_data:
        if i == 0:
            subject = line.removeprefix('Subject: ')
        elif i == 1:
            name = line.removeprefix('From: ')
        elif i ==2:
            received_time = line.removeprefix('Date: ')
        elif i == 3:
            continue
        elif i == 4:
            address = line.removeprefix('Reply-to: ')
        else:
            text += line
    with open('data_1', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([subject, name, address, text, received_time])

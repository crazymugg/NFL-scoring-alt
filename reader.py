import csv
from datetime import timedelta


with open('first.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        if len(row) == 6:
            quater = row[0]
            time = row[1]
        elif len(row) == 5:
            time = row[0]

        print(f'{quater}: {time}')
        time_minutes, time_seconds = time.split(':')
        converted_quater = timedelta(minutes=(60-(15*int(quater))))
        converted_time = timedelta(minutes=int(time_minutes), seconds=int(time_seconds))
        total_time = converted_quater + converted_time
        print(total_time)
        sec = total_time.seconds
        print(sec)        
        # minutes, seconds = row[1].split(':')
        # converted_quarter = timedelta(minutes=60-int(row[0]))
        # converted_time = timedelta(minutes=int(minutes), seconds=int(seconds))
        # time = converted_quarter + converted_time
        # scorea = row[-2]
        # scoreb = row[-1]


# from datetime import timedelta

# t1 = timedelta(hours=7, minutes=36)
# t2 = timedelta(hours=11, minutes=32)
# t3 = timedelta(hours=13, minutes=7)
# t4 = timedelta(hours=21, minutes=0)

# arrival = t2 - t1
# lunch = (t3 - t2 - timedelta(hours=1))
# departure = t4 - t3

# print(arrival, lunch, departure)
import csv

with open('faculty.csv', 'r') as book1:
    with open('emails.csv', 'r') as book2:
        reader1 = csv.reader(book1, delimiter=',')
        reader2 = csv.reader(book2, delimiter=',')

        both = []
        fields = reader1.next()
        reader2.next()
        for row1, row2 in zip(reader1, reader2):
            row2.append(row1[-1])
            both.append(row2)

        with open('emails2.csv', 'w') as output:
            writer = csv.writer(output, delimiter=',')
            writer.writerow(fields)
            writer.writerows(both)

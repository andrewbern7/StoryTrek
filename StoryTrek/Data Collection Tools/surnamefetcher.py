import csv

# Open the CSV file
with open('Names_2010Census.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    names = []
    for row in reader:
        name = row[0]  # Assuming the name is in the first column
        names.append(name)
        if len(names) >= 10000:
            break

# Write the names to a text file
with open('../data/surnames.txt', 'w') as txtfile:
    txtfile.write('\n'.join(names))

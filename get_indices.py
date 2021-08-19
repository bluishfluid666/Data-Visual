import csv

def get_indices(header_row, header):
    result = [i for i, j  in enumerate(header_row) if j==header]
    return int(result[-1])

def get_name(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        #title = next(header_row)[get_indices(header_row, 'NAME')]
        #return title
        
        #These are the wackest lines I can come up with atm:
        title = []
        for row in reader:
            name = row[get_indices(header_row, 'NAME')]
            title.append(name)
        return list(set(title))[0]
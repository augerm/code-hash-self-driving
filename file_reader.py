import os


def read_file(file, header_cols, row_cols):

    with open(file, 'r') as i:
        lines = i.readlines()

    header = {}
    rows = []
    for line in lines:
        line = line.replace('\n', '')
        lineArr = line.split(' ')
        if not header:
            for i in range(len(header_cols)):
                try:
                    header[header_cols[i]] = int(lineArr[i])
                except:
                    header[header_cols[i]] = lineArr[i]
        else:
            row = {}
            for i in range(len(row_cols)):
                try:
                    row[row_cols[i]] = int(lineArr[i])
                except:
                    row[row_cols[i]] = lineArr[i]
            rows.append(row)

    return {'header': header, 'rows': rows}



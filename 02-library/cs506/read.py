def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    csv_file = open(csv_file_path, 'r')
    lines = csv_file.readlines()
    for i in range(len(lines)):
        sub_list = lines[i].split(',')
        for j in range(len(sub_list)):
            # Deal with extra sets of quotation marks around strings
            if '"' in sub_list[j]:
                sub_list[j] = sub_list[j][1:-1]
            # Deal with the newline characters in the CSV
            if '\n' in sub_list[j]:
                sub_list[j] = sub_list[j][:-1]
            # Remove leading or trailing spaces
            sub_list[j] = sub_list[j].strip()
            print(sub_list)
            # Deal with numbers that are currently expressed as strings (first integers, then floats)
            if sub_list[j].isnumeric():
                    sub_list[j] = int(sub_list[j])
            elif "." in sub_list[j]:
                sub_list[j] = float(sub_list[j])
        lines[i] = sub_list
    return lines

print(read_csv("/Users/Alex/Desktop/test.csv"))
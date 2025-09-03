def read_and_write():
    reader = open('ds.csv', 'r')
    writer = open('ds.tsv', 'w')

    for line in reader.readlines():
        remove_quotes_line = remove_quotes(line)
        writer.write(remove_quotes_line)

    reader.close()
    writer.close()


def remove_quotes(line):
    result = []
    quote_count = 0

    for i in range(len(line)):
        if line[i] == '"':
            quote_count = 1
            result.append(line[i])
        elif line[i] == ',' and quote_count == 1:
            result.append('\t')
        else:
            result.append(line[i])
            
    return ''.join(result)
 

if __name__ == '__main__':
    read_and_write()
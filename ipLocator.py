import sys
import csv

# convert ip to integer
def ipToNum(ip):
    array = ip.split('.')
    num = 0
    for octal in array:
        num = num * 256 + int(octal)
    return num

# main
with open(sys.argv[1],'r') as database, open(sys.argv[2],'r') as ranges, open(sys.argv[3], 'w') as wr:
    
    # open all files passed by args
    reader1 = csv.reader(database)
    reader2 = csv.reader(ranges)
    results = csv.writer(wr, quoting=csv.QUOTE_NONNUMERIC)
    # output header
    results.writerow(('Ip','Country'))
    
    # store the files in memory if they are not too large
    data1 = []
    data2 = []
    for row in reader1:
        data1.append(row[0])
    for row in reader2:
        data2.append(row)

    #check the range of the ips    
    for i in data1:
        for j in data2:
            formatIp = ipToNum(i)
            if (formatIp >= int(j[0]) and
                formatIp <= int(j[1])):
                # write the ip in the output file
                results.writerow((i.rstrip(), j[3]))
                break # when ip matches, exits loop

database.close()
ranges.close()
wr.close()
import sys

# convert ip to integer
def ipToNum(ip):
    array = ip.split('.')
    num = 0
    for octal in array:
        num = num * 256 + int(octal)
    return num

def countryLookUp(formatIP, ranges):
    for r in ranges:
        if formatIP <= r[1]:
            if formatIP >= r[0]:
                return r[2]

# main
file1 = sys.argv[1]
file2 = sys.argv[2]
fileout = sys.argv[3]
    
ips = []
with open (file1, 'r') as db:
    for line in db:
        # delete invalid chars
        ips.append(line.replace('"', '').replace("\n",""))
rng = []
with open (file2, 'r') as ranges:
    for line in ranges:
        l =  line.replace('"',"")
        l = l.split(",")
        country = l[3]
        rng.append((int(l[0]),int(l[1]),country))        
results = []
for ip in ips:
    formatIP = ipToNum(ip)
    country = countryLookUp (formatIP,rng)
    results.append((ip, country))
 
with open (fileout, 'w') as fout:
    for r in results:
        fout.write(str(r[0])+","+str(r[1]))
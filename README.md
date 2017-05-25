# Locate the country of several IPs
IP Bulk to lookup for their respecting country using CSV files.
Special thanks to Bayu

## Usage
Using two existing CSV files passed as arguments with the same format as samples (toCompare.csv and countries.csv) will return results of the matching ips in a output file, corresponding to the third argument of the command.

Command example:
```
python ipLocator.py toCompare.csv countries.csv output.csv
```
## Links
- [Country ranges dataset](http://lite.ip2location.com/ip-address-ranges-by-country)

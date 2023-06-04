import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
print('Retrieving', url)

total = 0
count = 0

openURL = urllib.request.urlopen(url)
data = openURL.read()  # Take all data
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
list_of_data = tree.findall('comments/comment')

for item in list_of_data:
    count = count + 1
    value = item.find('count').text
    total = total + float(value)

print('Count:', count)
print('Sum:', total)

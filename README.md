# Extracting-data-from-XML
 The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
 
 Actual data: http://py4e-data.dr-chuck.net/comments_1806431.xml (Sum ends with 85)
 count all values in count tag <count></count>
 
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

<h3>Sample Execution</h3>

$ python3 solution.py<br>
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml<br>
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml<br><br>
Retrieved 4189 characters<br>
Count: 50<br>
Sum: 2485.0

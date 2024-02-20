import requests
from bs4 import BeautifulSoup
import os
import subprocess
import re
host = "hubemupc0180"

# Step 1: Send a GET request to the URL
url = "http://jediemserver.boi.rd.hpicorp.net/emulator/WorkingPages/AddEditEmulator.aspx?host={host}"
response = requests.get(url)

# Step 2: Parse the HTML response
# Your HTML line
html_line = '<input name="ctl00$ContentPlaceHolder1$txtFrmProdIP" type="text" value="15.77.164.180" readonly="readonly" id="ctl00_ContentPlaceHolder1_txtFrmProdIP">'
# Parse the HTML line with BeautifulSoup
soup = BeautifulSoup(html_line, 'html.parser')
# Find the input tag and get the value of the 'value' attribute, which is the IP address
ip_address = soup.find('input')['value']

# Step 4: Run the main.py script with the IP address as an argument
print(f"The IP address is: {ip_address}")


# Create the ping command as a string
command = f"ping {ip_address}"

# Use subprocess to execute the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
stdout, stderr = process.communicate()

# Decode the output
output = stdout.decode()
print(output)

# Use regex to find the packet loss percentage
loss_match = re.search(r'(\d+)% loss', output)
if loss_match:
    loss_percentage = int(loss_match.group(1))
    print(f"Packet loss percentage: {loss_percentage}%")
else:
    print("Could not find packet loss percentage")



# Check the packet loss percentage and print the result
if loss_percentage > 0:
    print("NOT PINGED")
else:
    print("PINGED")

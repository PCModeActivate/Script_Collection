import requests

url = requests.get("https://www.worldometers.info/world-population/population-by-country/")
html = url.text

input = open('Input.txt', 'r') 
inputFile = input.readlines() 
output = open('Output.txt', 'w')

for line in inputFile:
    country_index = line.find(',')
    requested_country = line[:country_index]
    vaccination_percentage = line[country_index+1:]
    vaccination_percentage = float(vaccination_percentage.strip())

    pop_string = ""
    pop_string_no_comma = ""
    pop_number = -1
    index = html.find(requested_country)+41+len(requested_country)

    while html[index] != '<':
        pop_string += html[index]
        index += 1

    for char in pop_string:
        if char != ',':
            pop_string_no_comma += char
    
    pop_number = int(pop_string_no_comma)
    output.write(requested_country+", "+str(int(pop_number*vaccination_percentage/100))+"\n")
input.close()
output.close()

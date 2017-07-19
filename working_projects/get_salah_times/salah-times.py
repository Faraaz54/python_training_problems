import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.salahtimes.com/india/hyderabad'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'html.parser')
table = soup.find('tbody')

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        list_of_cells.append(cell.get_text())
    list_of_rows.append(list_of_cells)

outfile = open('salah-times.csv','wb')
writer = csv.writer(outfile)
writer.writerows(list_of_rows)







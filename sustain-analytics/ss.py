from bs4 import BeautifulSoup
import csv

with open('ESG Data Publication App.html', 'r') as file:
    html = file.read()
print(html)
soup = BeautifulSoup(html, 'html.parser')

company_rows = soup.find_all('div', class_='company-row')

data = [
    ["Company Name", "Stock Ticker", "ESG Risk", "ESG Rating"]
]

for company in company_rows:
    name = company.find('a').text
    stock_ticker = company.find('small').text
    risk = company.find('div', class_="col-lg-6 col-md-10").text
    esg_rating = company.find('div', class_="col-2").text

    data.append([name, stock_ticker, risk, esg_rating])

filename = "esg_data.csv"

mode = 'w'

with open(filename, mode, newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


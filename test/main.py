from carid.carid2 import Vehicle
from openpyxl import Workbook

with Vehicle() as bot:
    bot.land_first_page()
    result = bot.select_year()
    wb = Workbook()
    page = wb.active
    page.title = "Carid.com"
    headers = ['Type','Year','Make','Model']
    page.append(headers)
    for row in result:
        row.insert(0,"Automobile")
        page.append(row)
    wb.save('results/Final_results_of_scraping_Carid.xlsx')




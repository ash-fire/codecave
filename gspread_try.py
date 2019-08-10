import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project 57578-9d661947467e.json', scope)


gc = gspread.authorize(credentials)

wks = gc.open("py.try").sheet1
pop = 1
pops = 2
wks.update_acell('B2', pop)
wks.update_acell('A2', pops)
wks.update_acell('B3', "=B2 + A2")
cell_list = wks.acell('')
print(cell_list)

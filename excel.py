import pandas as pd 

x = pd.read_excel('/Users/prarthanadesai/Library/Mobile Documents/com~apple~Numbers/Documents/Excel_Read.numbers')

data = x.to_json(orient='records', indent=4)
file_path = 'data.json'
with open(file_path, 'w') as json_file:
    json_file.write(data)
print("Data has been saved!")


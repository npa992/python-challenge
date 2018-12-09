import pandas as pd
file_path = ('Resources/budget_data.csv')
data_file = pd.read_csv(file_path)

profit_loss = data_file['Profit/Losses']
date = data_file['Date']

average_change = (profit_loss.tail(1)-profit_loss[0])/(len(profit_loss)-1)
delta = [profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]

max_change=max(delta)
min_change=min(delta)
max_date=date[delta.index(max_change)+1]
min_date=date[delta.index(min_change)+1]

file=open('output.txt','w')
file.write(f'The total number of months in the data is {len(date)}')
file.write('\n')
file.write(f'The average change was $ {int(average_change)}')
file.write('\n')
file.write(f'The maximum increase in profits was ${max_change} and occurred in {max_date}')
file.write('\n')
file.write(f'The maximum decrease was ${min_change} and occurred in {min_date}')

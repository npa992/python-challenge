import pandas as pd
file_path = ('Resources/election_data.csv')
election_data=pd.read_csv(file_path)

results = election_data['Candidate'].value_counts()
candidate = election_data['Candidate'].value_counts().index
results_percentages = (election_data['Candidate'].value_counts(1)*100)
total_votes=election_data['Candidate'].count()

final_result = pd.DataFrame({'Candidate':candidate,'Results':results,'Results %':results_percentages})
final_result.to_csv('results.csv',index=False)
index_winner=list(final_result['Results']).index(final_result['Results'].max())
winner=final_result['Candidate'].index[index_winner]
winner_votes=final_result['Results'].max()

file=open('results.txt','w')
file.write('The results are as follows:')
file.write('\n')
file.write(f'Total Votes:{total_votes}')
file.write('\n')
file.write(f'{candidate[0]}:{results[0]}, {round(results_percentages[0],2)}%')
file.write('\n')
file.write(f'{candidate[1]}:{results[1]}, {round(results_percentages[1],2)}%')
file.write('\n')
file.write(f'{candidate[2]}:{results[1]}, {round(results_percentages[2],2)}%')
file.write('\n')
file.write(f'{candidate[3]}:{results[1]}, {round(results_percentages[3],2)}%')
file.write('\n')
file.write(f'The winner was:{winner} with {winner_votes}votes')
file.close()



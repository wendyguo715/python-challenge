import os
import csv

#Pull csv file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    vote_count = 0
    candidate_list = []
    for row in csvreader:
        vote_count = vote_count + 1
        candidate_list.append(str(row[2]))

unique_candidate = list(set(candidate_list))
unique_candidate_sort = sorted(unique_candidate)
correy_count = candidate_list.count(unique_candidate_sort[0])
otoo_count = candidate_list.count(unique_candidate_sort[3])
khan_count = candidate_list.count(unique_candidate_sort[1])
li_count = candidate_list.count(unique_candidate_sort[2])
correy_percentage = correy_count/vote_count
otoo_percentage = otoo_count/vote_count
khan_percentage = (khan_count/vote_count)
li_percentage = li_count/vote_count
count_list = [correy_count,otoo_count,khan_count,li_count]
name_list = ["Correy","O'Tooley","Khan","Li"]
max_value = max(count_list)
winner_index = count_list.index(max_value)


print("Election Results")
print(f"Total Votes: {vote_count}")
print(f'Khan: {khan_percentage:.3%} ({khan_count})')
print(f'Correy: {correy_percentage:.3%} ({correy_count})')
print(f'Li: {li_percentage:.3%} ({li_count})')
print(f"O'Tooley: {otoo_percentage:.3%} ({otoo_count})")
print(f'Winner: {name_list[winner_index]}')

output_path = os.path.join("output2.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow("Election Results")
    csvwriter.writerow(["Total Votes",vote_count])
    csvwriter.writerow(["Khan",str(round(khan_percentage*100,3))+'%',khan_count])
    csvwriter.writerow(["Correy",str(round(correy_percentage*100,3))+'%',correy_count])
    csvwriter.writerow(["Li",str(round(li_percentage*100,3))+'%',li_count])
    csvwriter.writerow(["O'Tooley",str(round(otoo_percentage*100,3))+'%',otoo_count])
    csvwriter.writerow(["Winner",name_list[winner_index]])
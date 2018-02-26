import re

#reading the whole file as a string.
data_path = 'raw_dataset.txt'
with open(data_path, 'r') as f:
	data = f.readlines()

#spliting based on tags - 
tag_list = str(data).split('"],"') #split across "],"
num_of_tags = len(tag_list)
print("There are " + str(num_of_tags) + "distinct tags.\n")
temp = tag_list[num_of_tags - 1]
temp = temp[:-5]
tag_list[num_of_tags - 1] = temp
temp = tag_list[0]
temp = temp[4:]
tag_list[0] = temp
#Now each entry in the tag list consists of the tag followed by the qusetions in which that tag occured.

#Separating tag from the list of questions
tup = []
for i in tag_list:
	temp = i.split('":["') #split across ":["
	#print(len(temp))
	tup.append((temp[0], temp[1].split('","'))) #split across "," 
#Now each tuple in the list 'tup' contains two fields. First is the tag name and second is a list of questions from that tag.

#Removing html tags and other special characters from the question.
def clean_text(raw_text):
  clean_html = re.compile('<.*?>')
  cleaned_html = re.sub(clean_html, '', raw_text)
  cleaned_html = re.sub('\\\\n', '', cleaned_html)
  cleaned_html = re.sub('\\\\t', '', cleaned_html)
  cleantext = re.sub(r'\W+',' ', cleaned_html)
  return cleantext
out = 'Question, Tag\n' #Header for output file
for tag in tup:
	print("Working on " + str(tag[0]))
	for question in tag[1]:
		question = clean_text(question)
		out = out + str(question) + ',' + str(tag[0]) + '\n'

with open('cleaned_dataset.csv', "w") as f:
	f.write(out)
print('Done!')
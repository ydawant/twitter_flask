import datetime

good_file = open('good_words.txt', 'r')
bad_file = open('bad_words.txt', 'r')
good_list = [x.strip('\n') for x in good_file.readlines()]
bad_list = [x.strip('\n') for x in bad_file.readlines()]

def influence_score_calc(text):
	total = 0
	for word in text.split():
		if word in good_list:
			total +=1
		elif word in bad_list:
			total -=1
	return total

def convert_datetime(datetime_string):
	 return datetime.datetime.strptime(datetime_string,'%a %b %d %H:%M:%S +0000 %Y')
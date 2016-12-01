import urllib

folder = r"C:\Users\natal\Documents\Web Dev Nanodegree\0_Programming_Foundations\MiniProjects"
movie = "\movie_quotes.txt"
profane = "\list_of_bad_words.txt"
wdyl = "http://www.wdyl.com/profanity?q="

def read_text(path):
	quotes = open(path)
	contents = quotes.read()
	quotes.close()
	return contents
def check_profanity(text_to_check):
	#connection = urllib.urlopen(wdyl+text_to_check)
	#print connection.read()
	#connection.close()
	# code is out of date for how wdyl works
	contents = read_text(folder+profane)
	for word in text_to_check.split():
		if word in contents and len(word)>3:
			print word,"is a bad word"
			return True
	return False
check_profanity(read_text(folder+movie))
check_profanity("oh shit I forgot")
check_profanity("oh shoot I forgot")
check_profanity("he's a fucking beast")
check_profanity('fuck')
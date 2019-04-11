import pandas as pd
from textblob import TextBlob
from collections import Counter
import string
import enchant
import re
import csv
import glob, os
df = pd.read_csv("test.csv")
string1 = df.reviewText
for i in range(len(string1)):
	print(i)
	try:
		final=list();
		sentence =string1.iloc[i]
		length=len(sentence)
		wordlist=list(sentence.split())
		characterlist=list(sentence)
		blob = TextBlob(sentence)
		adjective=list();
		adjectivecomparitive=list();
		adjectivesuperlative=list();
		noun=list();
		conjuction=list();
		preposition=list();
		pronoun=list();
		adverb=list();
		verb=list();
		verbbase=list();
		verbpast=list();
		verbpresentpart=list();
		verbpastpart=list();
		verbsinnon=list();
		verbsin=list();
		pronounpossesive=list();
		pronounpersonal=list();
		nounpropsingular=list();
		nounpropplural=list();
		posending=list();
		pronounwh=list();
		cardinalnumber=list();
		for word, pos in blob.tags:
			if pos in ['JJ','JJR','JJS']:
				adjective.append(word)
				if(pos=='JJR'):
					adjectivecomparitive.append(word)
				elif(pos=='JJS'):
					adjectivesuperlative.append(word)
			if pos in ['NN','NNS','NNP','NNPS']:
				noun.append(word)
				if(pos=='NNP'):
					nounpropsingular.append(word)
				elif(pos=='NNPS'):
					nounpropplural.append(word)
			if pos in ['CC']:
				conjuction.append(word)
			if pos in ['IN']:
				preposition.append(word)
			if pos in ['PRP','PRP$','WP','WP$']:
				pronoun.append(word)
				if(pos=='PRP'):
					pronounpersonal.append(word)
				elif(pos=='PRP$'):
					pronounpossesive.append(word)
				elif(pos=='WP' or pos=='WP$'):
					pronounwh.append(word)
			if pos in ['RB','RBP','RBS','WRB']:
				adverb.append(word)
			if pos in ['VB','VBD','VBG','VBN','VBP','VBZ']:
				verb.append(word)
				if(pos=='VB'):
					verbbase.append(word)
				elif(pos=='VBD'):
					verbpast.append(word)
				elif(pos=='VBG'):
					verbpresentpart.append(word)
				elif(pos=='VBN'):
					verbpastpart.append(word)
				elif(pos=='VBP'):
					verbsinnon.append(word)
				elif(pos=='VBZ'):
					verbsin.append(word)
			if(pos=='POS'):
				posending.append(word)
			if(pos=='CD'):
				cardinalnumber.append(word)


		# processing caracters
		nofexclmation=0
		nofquestion=0
		nofdigits=0
		nofcapital=0
		nofpunctuation=0
		gramaticwords=0



		lowercase=list(string.ascii_lowercase)
		uppercase=list(string.ascii_uppercase)
		digits=list(string.digits)
		punctuation=list(string.punctuation)
		for x in characterlist:
			if(x=='!'):
				nofexclmation+=1
			elif(x=='?'):
				nofquestion+=1
			elif(x in digits):
				nofdigits+=1
			elif(x in uppercase):
				nofcapital+=1
			elif(x in punctuation):
				nofpunctuation+=1

		#processing words
		nofcapitalword=0
		nofdigitwords=0
		for x in wordlist:
			if(x.isupper()==True):
				nofcapitalword+=1
			elif(x.isdigit()==True):
				nofdigitwords+=1
		url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', sentence)
		nofurl=len(url)
		d = enchant.Dict("en_US")
		for x in wordlist:
			v=d.check(x)
			if(v==True):
				gramaticwords+=1
		polar=TextBlob(sentence).sentiment.polarity
		emoticons = 1
		nofemoticones= len(re.findall('\w+|[\U0001f600-\U0001f650]', sentence))

		final.append(nofexclmation)
		final.append(nofquestion)
		if(nofexclmation>0):
			final.append('Yes')
		else:
			final.append('No')
		if(nofquestion>0):
			final.append('Yes')
		else:
			final.append('No')
		if(nofurl>0):
			final.append('Yes')
		else:
			final.append('No')
		if(nofemoticones>0):
			final.append('Yes')
		else:
			final.append('No')
		final.append(polar)
		final.append(nofdigitwords)
		final.append(nofcapitalword)
		final.append(nofcapital)
		final.append(nofpunctuation)
		final.append(gramaticwords/len(wordlist))
		final.append(len(sentence))
		final.append(len(adjective))
		final.append(len(adjectivecomparitive))
		final.append(len(adjectivesuperlative))
		final.append(len(verbbase))
		final.append(len(verbpast))
		final.append(len(verbpresentpart))
		final.append(len(verbpastpart))
		final.append(len(verbsin))
		final.append(len(verbsinnon))
		final.append(len(adverb))
		final.append(len(pronounpersonal))
		final.append(len(pronounpossesive))
		final.append(len(nounpropsingular))
		final.append(len(nounpropplural))
		final.append(len(cardinalnumber))
		final.append(len(posending))
		final.append(len(pronounwh))
		final.append(len(verb))
		final.append(len(noun))
		final.append(len(pronoun))

		with open("dataanalysis.csv", "a") as fp:
			wr = csv.writer(fp, dialect='excel')
			wr.writerow(final)
	except:
		with open("dataanalysis.csv", "a") as fp:
			wr = csv.writer(fp, dialect='excel')
			wr.writerow(['ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR'])
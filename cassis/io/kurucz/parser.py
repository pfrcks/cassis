## Created by Amol Agrawal 8:35 PM, 6th March, 2015

def parse_first():
	from pyparsing import Word,OneOrMore,CharsNotIn,delimitedList	

	####Parsing First Line####
	whitespaces = ' \t\n\r'
	word = CharsNotIn(whitespaces)
	single_space = Word(whitespaces, exact=1)
	pars_label = OneOrMore(delimitedList(word, delim=single_space, combine=True))
	###########################


	fd = open('gf1401.gam')
	dct = dict()
	for i, lines in enumerate(fd):
		if i==0:
			dct[i] = pars_label.parseString(lines)
		else:
			break
	print dct[0]

def read_six_cols():

	import pandas as pd
	import numpy as np
	from sqlalchemy import create_engine

	colspaces = [(0,9),(10,12),(13,24),(26,29),(30,42),(43,48)]
	dataFrame = pd.read_fwf('gf1401.gam',colspecs=colspaces,skiprows=37,nrows=1764)
	dataFrame.columns=['elem','index','E','J','label','glande']
	dataFrame['glande']=dataFrame['glande'].map(lambda x: '%1.3f' % x)
	engine = create_engine('sqlite:///../../alchemy/parser.sqlite')## Open the database stored in alchemy folder
	conn = engine.raw_connection()
	dataFrame.to_sql(name='levels', con=conn, if_exists='append', index=False) ## Add dataframe to the table
	conn.close()

if __name__ == "__main__":
	parse_first()
	read_six_cols()

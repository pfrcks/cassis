import sqlalchemy
from sqlalchemy import create_engine
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
Base = declarative_base()

class  level(Base):##creating the levels table
	__tablename__ = 'levels'

	id = Column(Integer, primary_key=True)
	elem = Column(String)
	index = Column(Integer)
	E = Column(Numeric)
	J = Column(Float)
	label = Column(String)
	glande = Column(Numeric)
	
class line(Base):
	__tablename__ = 'lines'##creating the lines table and linking it with levels
	upper_id = Column(Integer, ForeignKey('levels.id'), primary_key=True)
	lower_id = Column(Integer, ForeignKey('levels.id'))

	levels = relationship("level", backref=backref('lines', order_by=lower_id))


os.system("rm parser.sqlite")
engine = create_engine('sqlite:///parser.sqlite', echo=False) ##the database
level.__table__
line.__table__
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)





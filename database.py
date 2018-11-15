from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(votes = 0,name=name)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def delete_by_id(id):
	cat = session.query(Cat
    	).filter_by(id=id).delete()
	session.commit()

def update_votes(id):
	cat = session.query(Cat
    	).filter_by(
    	id=id).first()
	cat.votes+=1
	session.commit()


def get_cat_by_id(id):
    cat = session.query(Cat
    	).filter_by(
    	id=id).first()
    return cat
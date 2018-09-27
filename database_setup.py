from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Family(Base):

    # Make only 10 objects since it is only demo version
    
    __tablename__ = 'family'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    family_img = Column(String(250), nullable=True)

    email = Column(String(250), nullable=True)
    country = Column(String(250), nullable=True)
    description = Column(String(1250), nullable=True)
    
    favorite_thing = Column(String(250), nullable=True)
    favorite_thing_img = Column(String(250), nullable=True)
    
    house_img = Column(String(250), nullable=True)

    water_img = Column(String(250), nullable=True)
    shoes_img = Column(String(250), nullable=True)
    
    books_img = Column(String(250), nullable=True)
    hand_img = Column(String(250), nullable=True)    
    tooth_brush_img = Column(String(250), nullable=True)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'family_img': self.family_img,
            'email': self.email,
            'country': self.country,
            'description': self.description,
            'favorite_thing': self.favorite_thing,
            'favorite_thing_img': self.favorite_thing_img,
            'house_img': self.house_img,
            'water_img': self.water_img,
            'shoes_img': self.shoes_img,
            'books_img': self.books_img,
            'hand_img': self.hand_img,
            'tooth_brush_img': self.tooth_brush_img,
        }


engine = create_engine('sqlite:///amavi.db')


Base.metadata.create_all(engine)
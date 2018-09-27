from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Family(Base):

    # Make only 10 objects since it is only demo version
    
    __tablename__ = 'family'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    family = Column(String(250), nullable=True)
    country = Column(String(250), nullable=True)
    description = Column(String(1250), nullable=True)
    ocuppation = Column(String(250), nullable=True)
    dream_to_be = Column(String(250), nullable=True)
    age = Column(Integer, nullable=True)
    hobby = Column(String(250), nullable=True)
    income = Column(Integer, nullable=True)
    plan_to_buy = Column(String(250), nullable=True)
    dream_to_buy = Column(String(250), nullable=True)
    favorite_thing = Column(String(250), nullable=True)
    thing_you_spend_most_time_on = Column(String(250), nullable=True)
    thing_you_spend_most_money_on = Column(String(250), nullable=True)

    family_img = Column(String(250), nullable=True)
    ocuppation_img = Column(String(250), nullable=True)
    dream_to_be_img = Column(String(250), nullable=True)
    hobby_img = Column(String(250), nullable=True)
    plan_to_buy_img = Column(String(250), nullable=True)
    dream_to_buy_img = Column(String(250), nullable=True)
    favorite_thing_img = Column(String(250), nullable=True)
    thing_you_spend_most_time_on_img = Column(String(250), nullable=True)
    thing_you_spend_most_money_on_img = Column(String(250), nullable=True)
    
    house_img = Column(String(250), nullable=True)
    electricity_img = Column(String(250), nullable=True)
    water_img = Column(String(250), nullable=True)
    drinking_water_img = Column(String(250), nullable=True)
    plate_of_food_img = Column(String(250), nullable=True)
    shoes_img = Column(String(250), nullable=True)
    place_for_guests_img = Column(String(250), nullable=True)
    dining_place_img = Column(String(250), nullable=True)
    light_source_img = Column(String(250), nullable=True)
    source_of_cool_img = Column(String(250), nullable=True)
    books_img = Column(String(250), nullable=True)
    phone_img = Column(String(250), nullable=True)
    transport_img = Column(String(250), nullable=True)
    
    bed_img = Column(String(250), nullable=True)
    hand_img = Column(String(250), nullable=True)
    medicine_img = Column(String(250), nullable=True)
    tooth_brush_img = Column(String(250), nullable=True)
    refrigerator_img = Column(String(250), nullable=True)
    shower_img = Column(String(250), nullable=True)
    toilet_img = Column(String(250), nullable=True)
    street_view_img = Column(String(250), nullable=True)
    uniform_clothing_img = Column(String(250), nullable=True)
    kitchen_img = Column(String(250), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'family': self.family,
        }


engine = create_engine('sqlite:///amavi.db')


Base.metadata.create_all(engine)
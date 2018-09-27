
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Family, Base
engine = create_engine('sqlite:///amavi.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = Family(
    name="Murad family",
    family_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    
    email="MuradSomeMail@gmail.com",
    country="Jordan",
    description="The Murad family lives in Ammani",
    favorite_thing="MacBook computer",
    favorite_thing_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    house_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    water_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    shoes_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    books_img="",
    hand_img="https://static.dollarstreet.org/media/Jordan%204/image/facf911d-3645-4893-8370-e81dba2a44dc/desktops-facf911d-3645-4893-8370-e81dba2a44dc.jpg")
	
session.add(User1)
session.commit()


User2 = Family(
    name="Murad2 family",
    family_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    email="MuradSomeMail@gmail.com",
    country="Jordan",
    description="The Murad family lives in Ammani",
    favorite_thing="MacBook computer",
    favorite_thing_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    house_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    water_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    shoes_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    books_img="",
    hand_img="https://static.dollarstreet.org/media/Jordan%204/image/facf911d-3645-4893-8370-e81dba2a44dc/desktops-facf911d-3645-4893-8370-e81dba2a44dc.jpg")
	
session.add(User2)
session.commit()


User3 = Family(
    name="Murad3 family",
    family_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    email="MuradSomeMail@gmail.com",
    country="Jordan",
    description="The Murad family lives in Ammani",
    favorite_thing="MacBook computer",
    favorite_thing_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    house_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    water_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    shoes_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    books_img="",
    hand_img="https://static.dollarstreet.org/media/Jordan%204/image/facf911d-3645-4893-8370-e81dba2a44dc/desktops-facf911d-3645-4893-8370-e81dba2a44dc.jpg")
	
session.add(User3)
session.commit()

print "DB is populated"

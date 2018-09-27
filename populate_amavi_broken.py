# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Family, Base
engine = create_engine('sqlite:///amavi.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = Family(
    name="Murad",
    email="MuradSomeMail@gmail.com",
    family="Murad family",
    country="Jordan",
    description="The Murad family lives in Amman, Jordan. Bia and her husband Simon (fictitious names) are both 32 years old and are business owners. They live with their young son and a live-in nanny in a rented 3-bedroom house. They like the house because of its size and location, but they aren’t happy with their neighbours. Their most favorite item in the house is their MacBook computer. Their plan is to buy a new house and dream of one day buying a luxury car.",
    ocuppation="business owners",
    age=32,
    hobby="Computers",
    income=7433,
    plan_to_buy="new house",
    dream_to_buy="luxury car",
    favorite_thing="MacBook computer",
    thing_you_spend_most_time_on="family",
    thing_you_spend_most_money_on="child",
    family_img="https://static.dollarstreet.org/media/Jordan%204/image/7472db28-6184-4012-bff8-6c4b69a84cd0/thumb-7472db28-6184-4012-bff8-6c4b69a84cd0.jpg",
    hobby_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    favorite_thing_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    thing_you_spend_most_time_on_img="https://static.dollarstreet.org/media/Jordan%204/image/7472db28-6184-4012-bff8-6c4b69a84cd0/thumb-7472db28-6184-4012-bff8-6c4b69a84cd0.jpg",
    thing_you_spend_most_money_on_img="https://static.dollarstreet.org/media/Jordan%204/image/ff84c62f-8421-40de-8fe6-48fc5d0b1249/desktops-ff84c62f-8421-40de-8fe6-48fc5d0b1249.jpg",
    water_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    drinking_water_img="https://static.dollarstreet.org/media/Jordan%204/image/db4349a0-6dcc-4b04-a22a-7578b4fde637/desktops-db4349a0-6dcc-4b04-a22a-7578b4fde637.jpg",
    shoes_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    place_for_guests_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    dining_place_img="https://static.dollarstreet.org/media/Jordan%204/image/0491cd20-9e19-4ba8-b657-492f348c23b8/desktops-0491cd20-9e19-4ba8-b657-492f348c23b8.jpg",
    toilet_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    shower_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    bed_img="https://static.dollarstreet.org/media/Jordan%204/image/fd0f055d-3c53-4c7e-bb50-7f08a77b4394/desktops-fd0f055d-3c53-4c7e-bb50-7f08a77b4394.jpg",
    hand_img="https://static.dollarstreet.org/media/Jordan%204/image/facf911d-3645-4893-8370-e81dba2a44dc/desktops-facf911d-3645-4893-8370-e81dba2a44dc.jpg")
session.add(User1)
session.commit()

User2 = Family(
    name="Murad",
    email="MuradSomeMail@gmail.com",
    family="Murad family",
    country="Jordan",
    description="The Murad family lives in Amman, Jordan. Bia and her husband Simon (fictitious names) are both 32 years old and are business owners. They live with their young son and a live-in nanny in a rented 3-bedroom house. They like the house because of its size and location, but they aren’t happy with their neighbours. Their most favorite item in the house is their MacBook computer. Their plan is to buy a new house and dream of one day buying a luxury car.",
    ocuppation="business owners",
    age=32,
    hobby="Computers",
    income=7433,
    plan_to_buy="new house",
    dream_to_buy="luxury car",
    favorite_thing="MacBook computer",
    thing_you_spend_most_time_on="family",
    thing_you_spend_most_money_on="child",
    family_img="https://static.dollarstreet.org/media/Jordan%204/image/7472db28-6184-4012-bff8-6c4b69a84cd0/thumb-7472db28-6184-4012-bff8-6c4b69a84cd0.jpg",
    hobby_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    favorite_thing_img="https://static.dollarstreet.org/media/Jordan%204/image/8dcef4cb-46da-4af3-ba1b-bacb9c994763/desktops-8dcef4cb-46da-4af3-ba1b-bacb9c994763.jpg",
    thing_you_spend_most_time_on_img="https://static.dollarstreet.org/media/Jordan%204/image/7472db28-6184-4012-bff8-6c4b69a84cd0/thumb-7472db28-6184-4012-bff8-6c4b69a84cd0.jpg",
    thing_you_spend_most_money_on_img="https://static.dollarstreet.org/media/Jordan%204/image/ff84c62f-8421-40de-8fe6-48fc5d0b1249/desktops-ff84c62f-8421-40de-8fe6-48fc5d0b1249.jpg",
    water_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    drinking_water_img="https://static.dollarstreet.org/media/Jordan%204/image/db4349a0-6dcc-4b04-a22a-7578b4fde637/desktops-db4349a0-6dcc-4b04-a22a-7578b4fde637.jpg",
    shoes_img="https://static.dollarstreet.org/media/Jordan%204/image/4b265912-3ffb-4d92-8b36-e7fa6e70fd5b/desktops-4b265912-3ffb-4d92-8b36-e7fa6e70fd5b.jpg",
    place_for_guests_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    dining_place_img="https://static.dollarstreet.org/media/Jordan%204/image/0491cd20-9e19-4ba8-b657-492f348c23b8/desktops-0491cd20-9e19-4ba8-b657-492f348c23b8.jpg",
    toilet_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    shower_img="https://static.dollarstreet.org/media/Jordan%204/image/36750895-a96b-4262-afba-4fb076ec7858/desktops-36750895-a96b-4262-afba-4fb076ec7858.jpg",
    bed_img="https://static.dollarstreet.org/media/Jordan%204/image/fd0f055d-3c53-4c7e-bb50-7f08a77b4394/desktops-fd0f055d-3c53-4c7e-bb50-7f08a77b4394.jpg",
    hand_img="https://static.dollarstreet.org/media/Jordan%204/image/facf911d-3645-4893-8370-e81dba2a44dc/desktops-facf911d-3645-4893-8370-e81dba2a44dc.jpg")
session.add(User2)
session.commit()



print "DB is populated"

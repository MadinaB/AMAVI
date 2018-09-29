
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Family, Base
engine = create_engine('sqlite:///amavi.db')
Base.metadata.bind = engine

DBSession = scoped_session(sessionmaker(bind=engine))
session = DBSession()

User1 = Family(
    name="Murad family",
    family_img="https://static.dollarstreet.org/media/Jordan%204/image/f4069874-31a0-48aa-9434-50f79d88abe9/desktops-f4069874-31a0-48aa-9434-50f79d88abe9.jpg",
    )
	
session.add(User1)
session.commit()



print "DB is populated"

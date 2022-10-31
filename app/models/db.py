# import os
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# db_url = os.environ.get('DATABASE_URL')
# engine = create_engine(db_url)

# SessionFactory = sessionmaker(bind=engine)

# session = SessionFactory()


# session.create_all()

db = SQLAlchemy()

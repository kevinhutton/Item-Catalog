from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Kevin Hutton", email="kevin@nowhere.com")
session.add(User1)
session.commit()

# Create Category
category1 = Category(name="Clothing")
session.add(category1)
session.commit()

categoryItem1 = CategoryItem(name="Quicksilver T-Shirt", description="Quicksilver T-Shirt",
                     category=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(name="Billabong T-Shirt", description="Billabong T-Shirt",
                     category=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(name="Rusty T-Shirt", description="Rusty T-Shirt",
                     category=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(name="Addias T-Shirt", description="Addias T-Shirt",
                     category=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(name="Oneill T-Shirt", description="Oneill T-Shirt",
                     category=category1)
session.add(categoryItem1)
session.commit()

category2 = Category(name="Sports Equipment")
session.add(category2)
session.commit()

categoryItem1 = CategoryItem(name="Forum Snowboard", description="Forum Snowboard",
                     category=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(name="Channel Islands Surfboard", description="Channel Islands Surfboard",
                     category=category2)
session.add(categoryItem1)
session.commit
ategoryItem1 = CategoryItem(name="Forum Snowboard", description="Forum Snowboard",
                     category=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(name="SUP Board", description="SUP Board",
                     category=category2)
session.add(categoryItem1)
session.commit()

from sqlalchemy.orm import sessionmaker
from main import engine
from main import Category

Session = sessionmaker(bind=engine)
session = Session()

for category in session.query(Category).all():
    print(f"Category: {category.name}, Discription: {category.description}")
    for product in category.products:
        print(f" Product: {product.name}, Price: {product.price}, Available: {product.in_stock}")
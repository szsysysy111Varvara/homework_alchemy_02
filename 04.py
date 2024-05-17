from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from main import engine
from main import Category, Product

Session = sessionmaker(bind=engine)
session = Session()
categories_with_more_products = session.query(Category.name).join(Product).group_by(Category.name).having(func.count(Product.id) > 1).all()
print("Categories with more than one product :", categories_with_more_products)
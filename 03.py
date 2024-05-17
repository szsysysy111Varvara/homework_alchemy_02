from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from main import engine
from main import Category, Product

Session = sessionmaker(bind=engine)
session = Session()

count_products_category = session.query(Category.name, func.count(Product.id)).join(Product).group_by(Category.name).all()
print("Count products and categories:", count_products_category)
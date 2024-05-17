from sqlalchemy.orm import sessionmaker
from main import engine
from main import Product

Session = sessionmaker(bind=engine)
session = Session()

product = session.query(Product).filter_by(name="Смартфон").first()
if product:
    product.price = 349.99
    session.commit()
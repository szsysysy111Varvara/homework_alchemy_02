from sqlalchemy import create_engine, Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


Base = declarative_base()


engine = create_engine('mysql+pymysql://root:Varvara00!@localhost:3306/test_alchemy', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)


categories = [
    Category(name="Электроника", description="Гаджеты и устройства."),
    Category(name="Книги", description="Печатные книги и электронные книги."),
    Category(name="Одежда", description="Одежда для мужчин и женщин."),
]


products = [
    Product(name="Смартфон", price=299.99, in_stock=True, category=categories[0]),
    Product(name="Ноутбук", price=499.99, in_stock=True, category=categories[0]),
    Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=categories[1]),
    Product(name="Джинсы", price=40.50, in_stock=False, category=categories[2]),
    Product(name="Футболка", price=20.00, in_stock=True, category=categories[2]),
]


session.add_all(categories + products)
session.commit()
session.close()
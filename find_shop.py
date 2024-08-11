import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine
from HW4 import create_tables, Publisher, Sale, Shop, Stock, Book

def get_sales_by_publisher(publisher_name, session):

    sales_info = (
        session.query(
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale
        )
        .join(Stock, Book.id == Stock.id_book)
        .join(Sale, Stock.id == Sale.id_stock)
        .join(Shop, Stock.id_shop == Shop.id)
        .join(Publisher, Book.id_publisher == Publisher.id)
        .filter(Publisher.name == publisher_name)
        .all()
    )

    for sale in sales_info:
        print(f"{sale.title} | {sale.name} | {sale.price} | {sale.date_sale}")

if __name__ == "__main__":

    DSN = 'postgresql://postgres:postgres@localhost:5432/book_shop'
    engine = create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()

    publisher_name = input("Введите имя издателя: ")
    get_sales_by_publisher(publisher_name, session)

    session.close()
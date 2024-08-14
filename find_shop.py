import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine
from HW4 import create_tables, Publisher, Sale, Shop, Stock, Book

def get_shops(publisher_identifier, session):

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
    )

    if publisher_identifier.isdigit():
        results = sales_info.filter(Publisher.id == int(publisher_identifier)).all()
    else:
        results = sales_info.filter(Publisher.name == publisher_identifier).all()


    for book_title, shop_name, sale_price, sale_date in results:
        print(f"{book_title: <40} | {shop_name: <10} | {sale_price: <8} | {sale_date.strftime('%d-%m-%Y')}")

if __name__ == "__main__":

    DSN = 'postgresql://postgres:postgres@localhost:5432/book_shop'
    engine = create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()


    publisher_name = input("Введите имя издателя или его ID: ")
    get_shops(publisher_name, session)  # Вызываем функцию для получения данных

    session.close()
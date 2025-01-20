from datetime import date
from models import SessionLocal, Price

def insert_price_example():
    # Create a session
    session = SessionLocal()

    try:
        new_price = Price(
            ticker="AAPL",
            date=date(2025, 1, 20),
            open_price=140.5,
            high_price=142.0,
            low_price=139.8,
            close_price=141.2,
            volume=120_000_000
        )

        # Stage the object
        session.add(new_price)
        # Commit the transaction
        session.commit()
        print("Inserted new price record!")
    except Exception as e:
        session.rollback()
        print("Error inserting price data:", e)
    finally:
        session.close()

if __name__ == "__main__":
    insert_price_example()

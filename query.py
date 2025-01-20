from models import SessionLocal, Price

def query_prices():
    session = SessionLocal()
    try:
        # Example: get all Price records for AAPL
        apple_prices = session.query(Price).filter(Price.ticker == "AAPL").all()
        for p in apple_prices:
            print(f"Date: {p.date}, Close: {p.close_price}")
    finally:
        session.close()

if __name__ == "__main__":
    query_prices()

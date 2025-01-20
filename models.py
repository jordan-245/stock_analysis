from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Define a base class for our models
Base = declarative_base()

# 2. Define your models (example tables: prices, fundamentals, news)
class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(10), index=True)
    date = Column(Date, index=True)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Float)

class Fundamental(Base):
    __tablename__ = "fundamentals"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(10), index=True)
    date_reported = Column(Date, index=True)
    pe_ratio = Column(Float, nullable=True)
    eps = Column(Float, nullable=True)
    market_cap = Column(Float, nullable=True)
    revenue = Column(Float, nullable=True)

class NewsArticle(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(10), index=True)
    headline = Column(String, nullable=False)
    published_at = Column(DateTime, index=True)
    sentiment_score = Column(Float, nullable=True)
    source = Column(String(255), nullable=True)
    url = Column(String(1024), nullable=True)


# 3. Set up your PostgreSQL connection string
# (Make sure you keep credentials secure and not in public repos.)
DATABASE_URL = "postgresql://stock_analysis_owner:HrSw9QJ2MeIj@ep-sparkling-wave-a8khgq87.eastus2.azure.neon.tech/stock_analysis?sslmode=require"

# 4. Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# 5. Create a session factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
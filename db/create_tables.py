from models import Base, engine

def init_db():
    # This call will create any tables that do not yet exist in the database
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Tables created successfully!")

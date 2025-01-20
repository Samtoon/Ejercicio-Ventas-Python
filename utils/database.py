from sqlmodel import create_engine

DATABASE_URL = "mysql+mysqlconnector://client:123456@localhost:3306/ventas_db"
engine = create_engine(DATABASE_URL, echo=True)
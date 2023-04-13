from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Session
from pydantic import BaseModel

sqlite_db = 'sqlite:///analysis.db'
engine = create_engine(sqlite_db, echo=True)


class Base(DeclarativeBase): pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    salary = Column(Float)
    current_funds = Column(Float)
    expenditure_funds = Column(Float)


Base.metadata.create_all(bind=engine)


data = {
    "name": "John",
    "salary": "1000",
    "current_funds": "100",
    "expenditure_funds": "900"
}


def add_user_data(data: dict):
    with Session(autoflush=False, bind=engine) as db:
        user_data = User(
            name=data['name'],
            salary=data['salary'],
            current_funds=data['current_funds'],
            expenditure_funds=data['expenditure_funds']
        )
        db.add(user_data)
        db.commit()
        db.refresh(user_data)


def retrieve_users_data():
    with Session(autoflush=False, bind=engine) as db:
        users_data = db.query(User).all()
        for user_data in users_data:
            print(
                f"user_id: {user_data.id}"
                f"user_name: {user_data.name}"
                f"user_salary: {user_data.salary}"
                f"user_current_funds: {user_data.current_funds}"
                f"user_expenditure_funds: {user_data.expenditure_funds}"
            )


def retrieve_user_data_by_id(_id: int):
    with Session(autoflush=False, bind=engine) as db:
        user_data = db.get(User, _id)
        print(
            f"user_id: {user_data.id}"
            f"user_name: {user_data.name}"
            f"user_salary: {user_data.salary}"
            f"user_current_funds: {user_data.current_funds}"
            f"user_expenditure_funds: {user_data.expenditure_funds}"
        )


def update_user_data_by_id(_id: int, name: str, salary: float, current_funds: float, expenditure_funds: float):
    with Session(autoflush=False, bind=engine) as db:
        user_data = db.query(User).filter(User.id == _id).first()

        if user_data is not None:
            print(f"user_id: {user_data.id}"
                  f"user_name: {user_data.name}"
            )

            user_data.name = name
            user_data.salary = salary
            user_data.current_funds = current_funds
            user_data.expenditure_funds = expenditure_funds

            db.commit()

            result = db.query(User).filter(User.id == _id).first()
            print(
                f"user_id: {user_data.id}"
                f"user_name: {user_data.name}"
                f"user_salary: {user_data.salary}"
                f"user_current_funds: {user_data.current_funds}"
                f"user_expenditure_funds: {user_data.expenditure_funds}"
            )


def delete_user_data_by_id(_id: int):
    with Session(autoflush=False, bind=engine) as db:
        user_data = db.query(User).filter(User.id == _id).first()
        db.delete(user_data)
        db.commit()

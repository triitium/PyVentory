import sys

from sqlalchemy import Column, Integer, Float, Date, Boolean, String, create_engine, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

from datetime import datetime

Base = declarative_base()

class Samples(Base):
    __tablename__ = 'samples'
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_id"),
    )

    id = Column(Integer)
    sid = Column(String(100), nullable=False, unique=False)
    description = Column(String(200), nullable=False)
    compound = Column(String(100))
    volume = Column(Float)
    series_name = Column(String(100))
    series_id = Column(Integer)
    validity = Column(Boolean, nullable=False)
    expiration_date = Column(Date, nullable=False)
    comment = Column(String(250))
    timestamp = Column(DateTime(timezone=True), default=datetime.now())

    #def __repr__(self):
    #    return "<User(sid='%s', compound='%s', volume='%s', series_name='%s', validity='%s', expiration_date='%s', comment='%s')>" % (
    #        self.sid, self.compound, self.volume, self.series_name, self.series_id, self.validity, self.expiration_date, self.comment)

class SQL:
    def __init__(self, host: str, port: str, user: str, password: str, database: str):
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}', echo=True)
        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_table(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    sys.exit(1)

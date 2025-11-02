from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.database import Base

class Menus(Base):
    __tablename__ = 'menus'

    id_menu = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String(100), nullable=False)
    harga = Column(Integer, nullable=False)
    kategori = Column(String(100), nullable=False)
    image = Column(String(255), nullable=False)
    deskripsi = Column(String(255), nullable=False)
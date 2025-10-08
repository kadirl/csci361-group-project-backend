from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    picture_urls = Column(JSON, nullable=False)
    stock = Column(Integer, nullable=False)

    retail_price = Column(Integer, nullable=False)
    threshold_price = Column(Integer, nullable=True)
    bulk_price = Column(Integer, nullable=True)

    minimum_order_quantity = Column(Integer, nullable=False)
    unit = Column(String, nullable=False)

    company = relationship("Companies", back_populates="products")
    order_products = relationship("OrderProducts", back_populates="product")
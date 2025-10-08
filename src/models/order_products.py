from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from src.database import Base

class OrderProducts(Base):
    __tablename__ = "order_products"

    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    product_price = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('product_id', 'order_id')
    )

    order = relationship("Orders", back_populates="order_products")
    product = relationship("Products", back_populates="order_products")
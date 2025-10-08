from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
import enum

class OrderStatus(enum.Enum):
    created = "created"
    processing = "processing"
    shipping = "shipping"
    completed = "completed"

class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    linking_id = Column(Integer, ForeignKey("linkings.company_id"), nullable=False)
    consumer_staff_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)

    status = Column(Enum(OrderStatus), default=OrderStatus.created, nullable=False)

    total_price = Column(Integer, nullable=False)

    created_at = Column(DateTime, nullable=False)

    linking = relationship("Linkings", back_populates="orders")
    order_products = relationship("OrderProducts", back_populates="order")
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base
import enum

class LinkingStatus(enum.Enum):
    accepted = "accepted"
    pending = "pending"
    rejected = "rejected"
    unlinked = "unlinked"

class Linkings(Base):
    __tablename__ = "linkings"

    linking_id = Column(Integer, primary_key=True, index=True)
    consumer_company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    supplier_company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)

    requested_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    responded_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_salesman_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    status = Column(Enum(LinkingStatus), default=LinkingStatus.pending, nullable=False)
    message = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    
    consumer_company = relationship("Companies", foreign_keys=[consumer_company_id], back_populates="linkings_as_consumer")
    supplier_company = relationship("Companies", foreign_keys=[supplier_company_id], back_populates="linkings_as_supplier")
    requested_by_user = relationship("Users", foreign_keys=[requested_by_user_id], back_populates="linkings_requested")
    responded_by_user = relationship("Users", foreign_keys=[responded_by_user_id], back_populates="linkings_responded")
    assigned_salesman = relationship("Users", foreign_keys=[assigned_salesman_id], back_populates="linkings_assigned")
    orders = relationship("Orders", back_populates="linking")
    
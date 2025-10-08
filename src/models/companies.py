from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from src.database import Base
import enum

class CompanyType(enum.Enum):
    supplier = "supplier"
    consumer = "consumer"

class CompanyStatus(enum.Enum):
    active = "active"
    suspended = "suspended"

class Companies(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(CompanyStatus), default=CompanyStatus.active, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    location = Column(String, nullable=True)
    type = Column(Enum(CompanyType), nullable=False)

    users = relationship("Users", back_populates="company")
    products = relationship("Products", back_populates="company")
    linkings_as_consumer = relationship("Linkings", foreign_keys="Linkings.consumer_company_id", back_populates="consumer_company")
    linkings_as_supplier = relationship("Linkings", foreign_keys="Linkings.supplier_company_id", back_populates="supplier_company")

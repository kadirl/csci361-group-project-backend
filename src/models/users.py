from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from src.database import Base
from sqlalchemy.orm import relationship
import enum

class UserStatus(enum.Enum):
    active = "active"
    suspended = "suspended"

class UserRole(enum.Enum):
    owner = "owner"
    manager = "manager"
    staff = "staff"

class Locale(enum.Enum):
    en = "en"
    ru = "ru"
    kz = "kz"

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    status = Column(Enum(UserStatus), default=UserStatus.active, nullable=False)
    locale = Column(Enum(Locale), default=Locale.en, nullable=False)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    company = relationship("Companies", back_populates="users")
    linkings_requested = relationship("Linkings", foreign_keys="Linkings.requested_by_user_id", back_populates="requested_by_user")
    linkings_responded = relationship("Linkings", foreign_keys="Linkings.responded_by_user_id", back_populates="responded_by_user")
    linkings_assigned = relationship("Linkings", foreign_keys="Linkings.assigned_salesman_id", back_populates="assigned_salesman")
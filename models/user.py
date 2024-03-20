#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents a User for a MySQL database."""
    __tablename__ = 'users'  # Represents the table name
    email = Column(String(128), nullable=False)  # Email column, must not be null
    password = Column(String(128), nullable=False)  # Password column, must not be null
    first_name = Column(String(128), nullable=True)  # First name column, can be null
    last_name = Column(String(128), nullable=True)  # Last name column, can be null

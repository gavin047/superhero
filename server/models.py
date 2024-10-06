from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, validates  # Import validates here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

db = SQLAlchemy()
Base = declarative_base()

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    super_name = Column(String, nullable=False)
    
    # Relationship with HeroPower
    hero_powers = relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # Validation for description length
    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description
    
    # Relationship with HeroPower
    hero_powers = relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = Column(Integer, primary_key=True)
    strength = Column(String, nullable=False)
    hero_id = Column(Integer, ForeignKey('heroes.id'), nullable=False)
    power_id = Column(Integer, ForeignKey('powers.id'), nullable=False)

    # Relationships
    hero = relationship('Hero', back_populates='hero_powers')
    power = relationship('Power', back_populates='hero_powers')

    # Validation for strength values
    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")
        return strength
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }
    
class Power(db.Model):
    __tablename__= 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    hero_powers = db.relationship('HeroPower', backref='power', cascade ="all, delete")

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description to be atleast 20 characters")
        return value 
    
    def to_dic(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    
class HeroPower(db.Model):
    __tablename__= 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength =db.Column(db.Integer, db.ForeignKey('powers.id'))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        raise value
    
    def to_dict(self):
        return{
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "power": self.power.to_dict(),
            "hero": self.hero.to_dict()
        }
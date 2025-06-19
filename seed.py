from models import db, Hero, Power, HeroPower
from app import app

with app.app_context():
    # Clear existing data
    print("🧹 Clearing database...")
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Create heroes
    print("🦸 Creating heroes...")
    h1 = Hero(name="Superman", super_name="Man of Steel")
    h2 = Hero(name="Wonder Woman", super_name="Amazon Princess")
    h3 = Hero(name="Flash", super_name="Fastest Man Alive")

    db.session.add_all([h1, h2, h3])
    db.session.commit()

    # Create powers
    print("⚡ Creating powers...")
    p1 = Power(name="Flight", description="Allows the hero to fly across the sky at incredible speeds.")
    p2 = Power(name="Super Strength", description="Gives the hero immense physical strength and power.")
    p3 = Power(name="Telepathy", description="Enables the hero to read and communicate through thoughts.")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Create hero powers
    print("🔗 Linking heroes and powers...")
    hp1 = HeroPower(strength="Strong", hero_id=h1.id, power_id=p1.id)
    hp2 = HeroPower(strength="Average", hero_id=h1.id, power_id=p2.id)
    hp3 = HeroPower(strength="Weak", hero_id=h2.id, power_id=p3.id)
    hp4 = HeroPower(strength="Strong", hero_id=h3.id, power_id=p2.id)

    db.session.add_all([hp1, hp2, hp3, hp4])
    db.session.commit()

    print("✅ Seeding completed!")

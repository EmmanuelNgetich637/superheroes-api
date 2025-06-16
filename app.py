from flask import Flask, request, jsonify
from models import db, Hero, Power, HeroPower
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    hero_dict = hero.to_dict()
    hero_dict["hero_powers"] = [hp.to_dict() for hp in hero.hero_powers]
    return jsonify(hero_dict), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([p.to_dict() for p in powers]), 200

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 400
    try:
        data = request.get_json()
        power.description = ['description']
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        return jsonify({"error": [str(e)]}), 400
    
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        new_hp = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

from random import choice as rc
from app import app, db
from models import Hero, Power, HeroPower
from sqlalchemy import text  # Import text for raw SQL execution

if __name__ == '__main__':
    with app.app_context():
        print("Clearing existing data from the database...")
        
        # Clear existing data using text()
        db.session.execute(text('DELETE FROM hero_powers'))  # Clear HeroPower first due to foreign key constraints
        db.session.execute(text('DELETE FROM heroes'))
        db.session.execute(text('DELETE FROM powers'))
        
        db.session.commit()  # Commit the deletions

        print("Seeding powers...")
        powers = [
            Power(name="super strength", description="gives the wielder super-human strengths"),
            Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
            Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
            Power(name="elasticity", description="can stretch the human body to extreme lengths"),
        ]

        db.session.add_all(powers)
        db.session.commit()  # Commit after adding powers
        print(f"Added {len(powers)} powers.")

        print("Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]

        db.session.add_all(heroes)
        db.session.commit()  # Commit after adding heroes
        print(f"Added {len(heroes)} heroes.")

        print("Assigning random powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = []
        
        for hero in heroes:
            power = rc(powers)
            strength = rc(strengths)
            hero_power = HeroPower(hero=hero, power=power, strength=strength)
            hero_powers.append(hero_power)

        db.session.add_all(hero_powers)
        db.session.commit()  # Commit after adding hero powers
        print(f"Assigned {len(hero_powers)} hero powers.")

        print("Done seeding!")
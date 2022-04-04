from models import db


def add_object_to_db(obj):
    db.session.add(obj)
    db.session.commit()

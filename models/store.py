from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    # (1) addtional argument if we want to load 'json' slower but 'items' can be
    # read faster. As we want to implement it with intense access, we want 'json'
    # faster and so the default is without the part with hashtag in code.

    items = db.relationship('ItemModel')
    # (1), lazy = 'dynamic')

    def __init__(self,name):
        self.name  = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items]}
        # (1) self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first() # SELECT * FROM items (__tablename__) WHERE name = name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

from crud import db

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"List('{self.id}', '{self.item}')"

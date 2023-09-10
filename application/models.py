from application import db


class Tune(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    new_column = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Tune> {self.id}, {self.name}"


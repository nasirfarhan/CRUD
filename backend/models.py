from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Fixed: column → Column
    first_name = db.Column(db.String(80), unique=False, nullable=False)  # Fixed: column → Column
    last_name = db.Column(db.String(80), unique=False, nullable=False)  # Fixed: column → Column
    email = db.Column(db.String(120), unique=True, nullable=False)  # Fixed: column → Column

    def to_json(self):  # Fixed: to_jspon → to_json
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
from app import db
from hospital.security import encrypt_data, decrypt_data

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nin = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    medical_history_encrypted = db.Column(db.LargeBinary, nullable=False)

    def set_medical_history(self, history):
        self.medical_history_encrypted = encrypt_data(history)

    def get_medical_history(self):
        return decrypt_data(self.medical_history_encrypted)

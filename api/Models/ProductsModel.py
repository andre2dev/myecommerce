from . import db
class Product(db.Model):
        id      = db.Column(db.Integer, primary_key=True)
        title   = db.Column(db.String(255), unique=False, nullable=False)
        amount  = db.Column(db.Numeric, unique=False, nullable=False)
        installments = db.Column(db.Integer, unique=False, nullable=False)
        installments_fee = db.Column(db.Boolean, unique=False, nullable=False)

        def __repr__(self):
            return f"<Product id={self.id} title={self.title!r}>"
        
        @property
        def serialized(self):
            return {
                'id': self.id,
                'title': self.title,
                'amount': round(self.amount, 2),
                'installments': {
                    'number': self.installments,
                    'total': round( self.amount / self.installments, 2),
                    'fee': self.installments_fee
                },
                
            }
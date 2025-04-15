@classmethod
def find(cls, product_id):
    return cls.query.get(product_id)

@classmethod
def all(cls):
    return cls.query.all()

@classmethod
def find_by_name(cls, name):
    return cls.query.filter_by(name=name).all()

@classmethod
def find_by_category(cls, category):
    return cls.query.filter_by(category=category).all()

@classmethod
def find_by_availability(cls, available):
    return cls.query.filter_by(available=available).all()

def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()

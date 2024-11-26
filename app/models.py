from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    hashed_password = db.Column(
        db.String(1000),
        nullable=False,
    )

    portfolios = db.relationship(
        "Portfolio", back_populates="user", cascade="all, delete-orphan"
    )


class Portfolio(db.Model):
    __tablename__ = "portfolios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="portfolios")


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker_symbol = db.Column(db.String(10), nullable=False)
    quantity = db.Column(
        db.Float,
        nullable=False,
    )
    portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolios.id"), nullable=False)

    portfolio = db.relationship("Portfolio", back_populates="assets")

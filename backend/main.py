from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Product
import database_model
from database import session, engine
from sqlalchemy.orm import Session

database_model.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"]
)


@app.get("/")
def greet():
    return "Hello, World!"


products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=2),
    Product(id=2, name="laptop", description="gaming laptop", price=500, quantity=3),
    Product(
        id=3,
        name="headphones",
        description="noise cancelling headphones",
        price=299,
        quantity=10,
    ),
    Product(
        id=4,
        name="smartwatch",
        description="fitness tracking smartwatch",
        price=199,
        quantity=15,
    ),
    Product(
        id=5,
        name="tablet",
        description="lightweight android tablet",
        price=349,
        quantity=7,
    ),
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# def db_init():
#     db = session()

#     count = db.query(database_model.Product).count()

#     if count == 0:
#         for product in products:
#             db.add(database_model.Product(**product.model_dump()))
#         db.commit()


# db_init()


@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    get_product = db.query(database_model.Product).all()
    return get_product


@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )

    if product:
        return product
    return "product not found"


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "updated successfully"
    return "product id is not found"


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "deleted successfully", "data": db_product}
    return "product not found"

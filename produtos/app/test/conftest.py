import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModel(name='Roupa', slug='roupa'),
        CategoryModel(name='Carro', slug='carro'),
        CategoryModel(name='Itens de cozinha', slug='itens-de-cozinha'),
        CategoryModel(name='Decoração', slug='decoracao')
    ]

    try:
        for category in categories:
            db_session.add(category)
        db_session.commit()

        for category in categories:
            db_session.refresh(category)

        yield categories

    finally:
        for category in categories:
            db_session.delete(category)
        db_session.commit()

@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name='Camisas', slug='camisas')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Camisa Abibas',
        slug='camisa-abibas',
        price=100.99,
        stock=20,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    yield product

    if db_session.query(ProductModel).filter_by(id=product.id).first():
        db_session.delete(product)

    if db_session.query(CategoryModel).filter_by(id=category.id).first():
        db_session.delete(category)

    db_session.commit()
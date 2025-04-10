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

@pytest.fixture()
def products_on_db(db_session):
    category = CategoryModel(name='Roupa', slug='roupa')
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)

    products = [
        ProductModel(name='Camisa Mike', slug='camisa-mike', price=32.99, stock=11, category_id=category.id),
        ProductModel(name='Moletom Mike', slug='moletom', price=109.90, stock=28, category_id=category.id),
        ProductModel(name='Camiseta', slug='camiseta-mike', price=45.90, stock=105, category_id=category.id),
        ProductModel(name='Short', slug='short', price=29.90, stock=57, category_id=category.id)
    ]

    for product in products:
        db_session.add(product)
    db_session.commit()

    for product in products:
        db_session.refresh(product)
    db_session.commit()

    yield products

    for product in products:
        db_session.delete(product)

    db_session.delete(category)

    db_session.commit()
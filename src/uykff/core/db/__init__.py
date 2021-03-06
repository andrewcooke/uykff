
from logging import debug

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

from uykff.core.db.catalogue import TableBase


def startup(config):
    metadata = TableBase.metadata
    debug('creating engine for %s' % config.db_url)
    engine = create_engine(config.db_url)
    metadata.bind = engine
    debug('creating tables (if missing)')
    metadata.create_all()
    return sessionmaker(bind=engine)


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if not instance:
        instance = model(**kwargs)
        session.add(instance)
    return instance

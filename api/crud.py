from sqlalchemy.orm import Session
from models import DataDelItem
from schemas import DataDelItemCreate, DataDelItemUpdate
from datetime import datetime

def get_all_cis(db: Session):
    return db.query(DataDelItem).all()

def get_ci(db: Session, ci_id: int):
    return db.query(DataDelItem).filter(DataDelItem.id == ci_id).first()

def create_ci(db: Session, ci: DataDelItemCreate):
    db_ci = DataDelItem(**ci.dict(), fecha_creacion_registro=datetime.utcnow(), ultima_actualizacion_registro=datetime.utcnow())
    db.add(db_ci)
    db.commit()
    db.refresh(db_ci)
    return db_ci

def update_ci(db: Session, ci_id: int, ci: DataDelItemUpdate):
    db_ci = db.query(DataDelItem).filter(DataDelItem.id == ci_id).first()
    if db_ci:
        for key, value in ci.dict(exclude_unset=True).items():
            setattr(db_ci, key, value)
        db_ci.ultima_actualizacion_registro = datetime.utcnow()
        db.commit()
        db.refresh(db_ci)
    return db_ci

def delete_ci(db: Session, ci_id: int):
    db_ci = db.query(DataDelItem).filter(DataDelItem.id == ci_id).first()
    if db_ci:
        db.delete(db_ci)
        db.commit()
    return db_ci

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMDB API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cis/", response_model=list[schemas.DataDelItemOut])
def list_cis(db: Session = Depends(get_db)):
    return crud.get_all_cis(db)

@app.get("/cis/{ci_id}", response_model=schemas.DataDelItemOut)
def get_ci(ci_id: int, db: Session = Depends(get_db)):
    ci = crud.get_ci(db, ci_id)
    if not ci:
        raise HTTPException(status_code=404, detail="CI no encontrado")
    return ci

@app.post("/cis/", response_model=schemas.DataDelItemOut)
def create_ci(ci: schemas.DataDelItemCreate, db: Session = Depends(get_db)):
    return crud.create_ci(db, ci)

@app.put("/cis/{ci_id}", response_model=schemas.DataDelItemOut)
def update_ci(ci_id: int, ci: schemas.DataDelItemUpdate, db: Session = Depends(get_db)):
    updated = crud.update_ci(db, ci_id, ci)
    if not updated:
        raise HTTPException(status_code=404, detail="CI no encontrado")
    return updated

@app.delete("/cis/{ci_id}")
def delete_ci(ci_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_ci(db, ci_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="CI no encontrado")
    return {"ok": True, "message": "CI eliminado"}

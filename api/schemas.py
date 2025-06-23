from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class DataDelItemBase(BaseModel):
    nombre: str
    tipo_ci_id: int
    decstipcion: Optional[str] = None
    num_serial: Optional[str] = None
    version: Optional[str] = None
    fecha_adquisicion: Optional[date] = None
    estado: Optional[str] = None
    localizacion: Optional[str] = None
    propietario: Optional[str] = None
    enlace_documentacion: Optional[str] = None
    enlace_incidente: Optional[str] = None
    nivel_seguridad: Optional[str] = None
    cumplimiento: Optional[str] = None
    estado_configuracion: Optional[str] = None
    numero_licencia: Optional[str] = None
    fecha_expiracion: Optional[date] = None

class DataDelItemCreate(DataDelItemBase):
    pass

class DataDelItemUpdate(DataDelItemBase):
    pass

class DataDelItemOut(DataDelItemBase):
    id: int
    fecha_creacion_registro: Optional[datetime]
    ultima_actualizacion_registro: Optional[datetime]

    class Config:
        orm_mode = True

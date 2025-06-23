from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class TipoCI(Base):
    __tablename__ = "tipo_ci"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)

    items = relationship("DataDelItem", back_populates="tipo_ci")


class Entorno(Base):
    __tablename__ = "entorno"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)

    entornos_ci = relationship("EntornoCI", back_populates="entorno")


class DataDelItem(Base):
    __tablename__ = "data_del_item"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    tipo_ci_id = Column(Integer, ForeignKey("tipo_ci.id"), nullable=False)
    decstipcion = Column(Text)
    num_serial = Column(String(100))
    version = Column(String(50))
    fecha_adquisicion = Column(Date)
    estado = Column(String(50))
    localizacion = Column(String(255))
    propietario = Column(String(255))
    enlace_documentacion = Column(Text)
    enlace_incidente = Column(Text)
    nivel_seguridad = Column(String(50))
    cumplimiento = Column(String(100))
    estado_configuracion = Column(String(50))
    numero_licencia = Column(String(100))
    fecha_expiracion = Column(Date)
    fecha_creacion_registro = Column(DateTime, default=datetime.utcnow)
    ultima_actualizacion_registro = Column(DateTime, default=datetime.utcnow)

    tipo_ci = relationship("TipoCI", back_populates="items")
    entornos = relationship("EntornoCI", back_populates="ci")
    logs = relationship("CILog", back_populates="ci")
    hijos = relationship("CIRelacion", back_populates="padre", foreign_keys='CIRelacion.padre_id')
    padres = relationship("CIRelacion", back_populates="hijo", foreign_keys='CIRelacion.hijo_id')


class EntornoCI(Base):
    __tablename__ = "entorno_ci"
    __table_args__ = (UniqueConstraint("ci_id", "entorno_id"),)

    id = Column(Integer, primary_key=True, index=True)
    ci_id = Column(Integer, ForeignKey("data_del_item.id"), nullable=False)
    entorno_id = Column(Integer, ForeignKey("entorno.id"), nullable=False)

    ci = relationship("DataDelItem", back_populates="entornos")
    entorno = relationship("Entorno", back_populates="entornos_ci")


class CIRelacion(Base):
    __tablename__ = "ci_relacion"
    __table_args__ = (
        CheckConstraint("padre_id <> hijo_id", name="no_autoreferencia"),
    )

    id = Column(Integer, primary_key=True, index=True)
    padre_id = Column(Integer, ForeignKey("data_del_item.id"), nullable=False)
    hijo_id = Column(Integer, ForeignKey("data_del_item.id"), nullable=False)
    tipo_relacion = Column(String(100))

    padre = relationship("DataDelItem", foreign_keys=[padre_id], back_populates="hijos")
    hijo = relationship("DataDelItem", foreign_keys=[hijo_id], back_populates="padres")


class CILog(Base):
    __tablename__ = "ci_log"

    id = Column(Integer, primary_key=True, index=True)
    ci_id = Column(Integer, ForeignKey("data_del_item.id"), nullable=False)
    description = Column(Text, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)

    ci = relationship("DataDelItem", back_populates="logs")

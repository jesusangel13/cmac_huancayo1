from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from src.database import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )

    dni = Column(
        String(8),
        unique=True,
        nullable=False
    )

    tarjeta = Column(
        String(16),
        unique=True,
        nullable=False
    )

    correo = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    codigo_seguridad = Column(
        String(4),
        nullable=False
    )
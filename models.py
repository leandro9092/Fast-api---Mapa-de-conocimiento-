from sqlalchemy import Column, Integer, String, Date, ForeignKey, Double, Text, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

# --- TABLAS MAESTRAS ---
class AreaConocimiento(Base):
    __tablename__ = "area_conocimiento"
    id = Column(Integer, primary_key=True)
    gran_area = Column(String(60), nullable=False)
    area = Column(String(60), nullable=False)
    disciplina = Column(String(60), nullable=False)

class ObjetivoDesarrolloSostenible(Base):
    __tablename__ = "objetivo_desarrollo_sostenible"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    categoria = Column(String(45), nullable=False)

class AreaAplicacion(Base):
    __tablename__ = "area_aplicacion"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)

class TerminoClave(Base):
    __tablename__ = "termino_clave"
    termino = Column(String(30), primary_key=True)
    termino_ingles = Column(String(30))

class LineaInvestigacion(Base):
    __tablename__ = "linea_investigacion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(256), nullable=False)

class Aliado(Base):
    __tablename__ = "aliado"
    nit = Column(Integer, primary_key=True)
    razon_social = Column(String(60), nullable=False)
    nombre_contacto = Column(String(60), nullable=False)
    correo = Column(String(70), nullable=False)
    telefono = Column(String(45), nullable=False)
    ciudad = Column(String(45), nullable=False)

class TipoProducto(Base):
    __tablename__ = "tipo_producto"
    id = Column(Integer, primary_key=True)
    categoria = Column(String(45), nullable=False)
    clase = Column(String(45), nullable=False)
    nombre = Column(String(45), nullable=False)
    tipologia = Column(String(45), nullable=False)


class Docente(Base):
    __tablename__ = "docente"
    cedula = Column(Integer, primary_key=True)
    nombres = Column(String(60), nullable=False)
    apellidos = Column(String(60), nullable=False)
    genero = Column(String(12), nullable=False)
    cargo = Column(String(30), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    correo = Column(String(70), nullable=False)
    telefono = Column(String(20), nullable=False)
    url_cvlac = Column(String(128), nullable=False)
    fecha_actualizacion = Column(Date, nullable=False)
    escalafon = Column(String(45), nullable=False)
    perfil = Column(Text, nullable=False)
    cat_minciencia = Column(String(45))
    conv_minciencia = Column(String(45), nullable=False)
    nacionalidaad = Column(String(45), nullable=False)
    linea_investigacion_principal = Column(Integer, ForeignKey("linea_investigacion.id"))

class Proyecto(Base):
    __tablename__ = "proyecto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(70), nullable=False)
    resumen = Column(String(256), nullable=False)
    presupuesto = Column(Double, nullable=False)
    tipo_financiacion = Column(String(45), nullable=False)
    tipo_fondos = Column(String(45), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    categoria = Column(String(45), nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    proyecto = Column(Integer, ForeignKey("proyecto.id"))
    tipo_producto = Column(Integer, ForeignKey("tipo_producto.id"))

# --- TABLAS DE RELACIÓN (MUCHOS A MUCHOS) ---
class Desarrolla(Base):
    __tablename__ = "desarrolla"
    docente = Column(Integer, ForeignKey("docente.cedula"), primary_key=True)
    proyecto = Column(Integer, ForeignKey("proyecto.id"), primary_key=True)
    rol = Column(String(45), nullable=False)
    descripcion = Column(String(256), nullable=False)

class ACProyecto(Base):
    __tablename__ = "ac_proyecto"
    proyecto = Column(Integer, ForeignKey("proyecto.id"), primary_key=True)
    area_conocimiento = Column(Integer, ForeignKey("area_conocimiento.id"), primary_key=True)

class ODSProyecto(Base):
    __tablename__ = "ods_proyecto"
    proyecto = Column(Integer, ForeignKey("proyecto.id"), primary_key=True)
    ods = Column(Integer, ForeignKey("objetivo_desarrollo_sostenible.id"), primary_key=True)


class Rol(Base):
    __tablename__ = "rol"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)
    activo = Column(Boolean, default=True)

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    activo = Column(Boolean, default=True)
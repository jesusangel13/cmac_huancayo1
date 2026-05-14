from fastapi import FastAPI
from fastapi import Request
from fastapi import Form

from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from src.database import Base
from src.database import engine
from src.database import SessionLocal

from src.models import Usuario

from src.security import hash_password
from src.security import verify_password


Base.metadata.create_all(bind=engine)

app = FastAPI()


# =========================
# STATIC FILES
# =========================

app.mount(
    "/css",
    StaticFiles(directory="src/css"),
    name="css"
)

app.mount(
    "/js",
    StaticFiles(directory="src/js"),
    name="js"
)

app.mount(
    "/img",
    StaticFiles(directory="src/img"),
    name="img"
)

app.mount(
    "/videos",
    StaticFiles(directory="src/videos"),
    name="videos"
)


# =========================
# JINJA2
# =========================

templates = Jinja2Templates(
    directory="src/html"
)


# =========================
# LOGIN PAGE
# =========================

@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


# =========================
# REGISTER PAGE
# =========================

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


# =========================
# REGISTER USER
# =========================

@app.post("/register")
def register(

    nombre: str = Form(...),
    dni: str = Form(...),
    tarjeta: str = Form(...),
    correo: str = Form(...),
    password: str = Form(...),

    pin1: str = Form(...),
    pin2: str = Form(...),
    pin3: str = Form(...),
    pin4: str = Form(...)

):

    db = SessionLocal()

    existing_user = db.query(Usuario).filter(
        Usuario.correo == correo
    ).first()

    if existing_user:

        db.close()

        return {
            "mensaje": "El correo ya existe"
        }

    codigo_seguridad = (
        pin1 +
        pin2 +
        pin3 +
        pin4
    )

    hashed_password = hash_password(password)

    nuevo_usuario = Usuario(

        nombre=nombre,
        dni=dni,
        tarjeta=tarjeta,
        correo=correo,
        password=hashed_password,
        codigo_seguridad=codigo_seguridad
    )

    db.add(nuevo_usuario)

    db.commit()

    db.close()

    return RedirectResponse(
        url="/",
        status_code=303
    )


# =========================
# LOGIN USER
# =========================

@app.post("/login")
def login(

    correo: str = Form(...),
    password: str = Form(...)

):

    db = SessionLocal()

    usuario = db.query(Usuario).filter(
        Usuario.correo == correo
    ).first()

    if not usuario:

        db.close()

        return {
            "mensaje": "Correo incorrecto"
        }

    valid_password = verify_password(
        password,
        usuario.password
    )

    if not valid_password:

        db.close()

        return {
            "mensaje": "Contraseña incorrecta"
        }

    db.close()

    return {
        "mensaje": f"Bienvenido {usuario.nombre}"
    }


# =========================
# DELETE USER
# =========================

@app.post("/delete-user")
def delete_user(

    dni: str = Form(...)

):

    db = SessionLocal()

    usuario = db.query(Usuario).filter(
        Usuario.dni == dni
    ).first()

    if not usuario:

        db.close()

        return {
            "mensaje": "Usuario no encontrado"
        }

    db.delete(usuario)

    db.commit()

    db.close()

    return {
        "mensaje": f"Usuario con DNI {dni} eliminado"
    }


# =========================
# ADMIN PAGE
# =========================

@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="admin.html"
    )
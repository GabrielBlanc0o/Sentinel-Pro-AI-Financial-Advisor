from passlib.context import CryptContext

# use bcrypt  para encriptar

pass_context = CryptContext(schemes=["argon2"],deprecated = "auto")

def encriptar_contra(contrasenia):
    return pass_context.hash(contrasenia)

def verificar_contra(contrasenia_plana, password_encriptada):
    try:
        return pass_context.verify(contrasenia_plana, password_encriptada)
    except Exception as e:
        print(f"Error de verificacion: {e}")
        return False
from models import session, Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["123123"]).generate()[0]
usuario = Usuario(nome="Lira", senha=senha_criptografada, email="lira@gmail.com", admin=True)
session.add(usuario)
session.commit()
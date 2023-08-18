from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

#creamos una extension de SQLAlchemy
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    
    # Configuración del poyecto 
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    
    )
    
    #inicializamos nuestra conexion a la base de datos
    db.init_app(app)

    # Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)

    from.import auth
    app.register_blueprint(auth.bp)
     
    @app.route('/')
    def index():
        return render_template ('index.html')
    
    #Aqui pegamos el comando para poder crear o migrar mis modelos en la BD relacional
    with app.app_context():
        db.create_all()
    
    return app

 

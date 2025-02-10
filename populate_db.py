from pymongo import MongoClient
from werkzeug.security import generate_password_hash

# Conectar a MongoDB
client = MongoClient('localhost', 27017)
db = client['tienda_virtual']

# Eliminar datos existentes (opcional)
db.users.delete_many({})
db.instruments.delete_many({})
db.cards.delete_many({})
db.orders.delete_many({})
db.reviews.delete_many({})

# Crear índice de texto en la colección de instrumentos
db.instruments.create_index([('name', 'text'), ('description', 'text')])

# Insertar usuarios
users = [
    {'username': 'cliente', 'password': generate_password_hash('1234'), 'role': 'user'},
    {'username': 'admin', 'password': generate_password_hash('admin'), 'role': 'admin'}
]
db.users.insert_many(users)

# Insertar instrumentos
instruments = [
    {'name': 'Guitarra Eléctrica', 'description': 'Una guitarra eléctrica de alta calidad', 'category': 'Cuerdas', 'price': 750.0, 'image_url': 'guitarra_electrica.jpg'},
    {'name': 'Batería Acústica', 'description': 'Perfecta para principiantes y profesionales', 'category': 'Percusión', 'price': 1250.0, 'image_url': 'bateria_acustica.jpg'},
    {'name': 'Piano Digital', 'description': 'Piano digital con múltiples funciones', 'category': 'Teclas', 'price': 1500.0, 'image_url': 'piano_digital.jpg'},
    {'name': 'Violín', 'description': 'Violín para estudiantes y avanzados', 'category': 'Cuerdas', 'price': 400.0, 'image_url': 'violin.jpg'},
    {'name': 'Flauta', 'description': 'Flauta de alta precisión para músicos profesionales', 'category': 'Viento', 'price': 250.0, 'image_url': 'flauta.jpg'},
    {'name': 'Saxofón', 'description': 'Saxofón de alto rendimiento', 'category': 'Viento', 'price': 1250.0, 'image_url': 'saxofon.jpg'},
]
db.instruments.insert_many(instruments)

print("Datos insertados correctamente")

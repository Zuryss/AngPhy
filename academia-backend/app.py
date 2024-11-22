from flask import Flask, jsonify

app = Flask(__name__)

# Datos hardcodeados
data = [
    {"id": 1, "nombre": "Elemento 1", "descripcion": "Descripción del elemento 1"},
    {"id": 2, "nombre": "Elemento 2", "descripcion": "Descripción del elemento 2"},
    {"id": 3, "nombre": "Elemento 3", "descripcion": "Descripción del elemento 3"}
]

@app.route('/api/elementos', methods=['GET'])
def get_elementos():
    return jsonify(data)

# Manejo de errores
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)

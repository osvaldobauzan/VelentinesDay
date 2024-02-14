from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

participants = []
selected_participants = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_participant', methods=['POST'])
def add_participant():
    data = request.get_json()
    participant = data.get('participant', '')
    if participant:
        participants.append(participant)
        return jsonify({'message': f"Participante '{participant}' agregado correctamente."}), 200
    else:
        return jsonify({'error': 'Por favor, ingrese un nombre de participante.'}), 400

@app.route('/select_next')
def select_next():
    if participants:
        if len(selected_participants) < len(participants):
            remaining_participants = [p for p in participants if p not in selected_participants]
            selected_participant = random.choice(remaining_participants)
            selected_participants.append(selected_participant)
            return jsonify({'selected_participant': selected_participant}), 200
        else:
            return jsonify({'message': '¡Todos los participantes han sido seleccionados!'}), 200
    else:
        return jsonify({'error': 'No hay participantes para seleccionar.'}), 400

@app.route('/reset_selection')
def reset_selection():
    global selected_participants
    selected_participants = []
    return jsonify({'message': 'Selección reiniciada. Puede volver a seleccionar participantes.'}), 200

if __name__ == '__main__':
    app.run(debug=True)

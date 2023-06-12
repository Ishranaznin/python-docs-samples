from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-even-numbers', methods=['POST'])
def hello():
    data = request.get_json()
    n = data['n']
    even_numbers = [num for num in range(2, 2*n+1, 2)]
    return jsonify({'even_numbers': even_numbers})

if __name__ == '__main__':
    app.run(debug=True)

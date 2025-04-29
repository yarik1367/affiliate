from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище (в реальности лучше использовать БД)
registered_traders = set()

@app.route('/postback', methods=['POST'])
def postback():
    data = request.json
    trader_id = data.get("trader_id")
    if trader_id:
        registered_traders.add(trader_id)
        print(f"New registration: {trader_id}")
        return jsonify({"status": "ok"})
    return jsonify({"status": "missing trader_id"}), 400

@app.route('/check/<trader_id>')
def check(trader_id):
    return jsonify({"registered": trader_id in registered_traders})

if __name__ == '__main__':
    app.run()

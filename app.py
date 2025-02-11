import yfinance as yf
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=["GET"])
def index():
    return "Welcome to my API!"
@app.route("/stock/<symbol>", methods=["GET"])
def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")  # Get the latest day's data
        if data is None or data.empty:
            return jsonify({"error": "No data found for stock symbol"}), 404
        last_price = data["Close"].iloc[-1]  # Get the last closing price
        return jsonify({"symbol": symbol, "price": round(last_price, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


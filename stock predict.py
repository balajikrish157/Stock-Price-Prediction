import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import yfinance as yf
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fetch_stock_data():
    symbol = symbol_entry.get()
    try:
        stock = yf.Ticker(symbol)x
        historical_data = stock.history(period="1y")
        current_price = historical_data["Close"].iloc[-1]
        future_price = current_price + (current_price * 0.01)  # A simple 1% increase prediction
        plot_stock_data(historical_data, future_price)
        result_var.set(f"Current Price: {current_price:.2f}\nPredicted Future Price: {future_price:.2f}")
    except Exception as e:
        result_var.set("Error: " + str(e))

def plot_stock_data(historical_data, future_price):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(historical_data.index, historical_data["Close"], label="Historical Price")
    ax.axhline(y=future_price, color='r', linestyle='--', label="Predicted Price")
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()

# Create the main application window
app = tk.Tk()
app.title("Stock Price Prediction")

frame = tk.Frame(app)
frame.pack()

symbol_label = Label(frame, text="Enter Stock Symbol:")
symbol_label.pack()
symbol_entry = Entry(frame)
symbol_entry.pack()

fetch_button = Button(frame, text="Fetch Data and Predict", command=fetch_stock_data)
fetch_button.pack()

result_var = StringVar()
result_label = Label(frame, textvariable=result_var)
result_label.pack()

app.mainloop()

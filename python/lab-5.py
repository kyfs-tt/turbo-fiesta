import numpy as np
import csv

try:
    with open('AAPL-2017.csv', newline="") as f:
        reader = csv.DictReader(f)
        trades = np.empty((0, 6), dtype=float)

        for row in reader:
            oneRow = np.array([[
                row['Open'],
                row['High'],
                row['Low'],
                row['Close'],
                row['Adj Close'],
                row['Volume']
            ]])
            trades = np.append(trades, oneRow, axis=0)

    print("DEBUG: ", trades.ndim)
    print("DEBUG: ", trades.shape)
    print("DEBUG: ", trades)

except IOError as e:
    print("IOError:", e.with_traceback())

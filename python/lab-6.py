import numpy as np
import csv


def deduce_least_num_of_lines_in_file(files=[]):
    try:
        i = 0
        least_count = 0
        for fp in files:
            # determine length of files
            with open(fp) as f:
                for j, _ in enumerate(f, 1):
                    pass
            if i == 0:
                least_count = j
            else:
                least_count = min(least_count, j)
            i += 1
        return least_count
    except IOError as e:
        print("IOError: ", e.with_traceback())


try:
    file1_path = "AAPL-2016.csv"
    file2_path = "AAPL-2017.csv"

    num_lines_to_read = deduce_least_num_of_lines_in_file([
      file1_path,
      file2_path
    ]) - 1  # subtract column row

    # read files
    with open(file1_path, newline="") as f1:
        with open(file2_path, newline="") as f2:
            r1 = csv.DictReader(f1)
            r2 = csv.DictReader(f2)
            trades1 = np.empty((0, 6), dtype=float)
            trades2 = np.empty((0, 6), dtype=float)

            for _ in range(num_lines_to_read):
                # read from file1 to trades1
                row1 = next(r1)
                trades1 = np.append(trades1,
                                    np.array([[
                                        float(row1['Open']),
                                        float(row1['High']),
                                        float(row1['Low']),
                                        float(row1['Close']),
                                        float(row1['Adj Close']),
                                        float(row1['Volume'])
                                    ]]), axis=0)
                # read from file2 to trades2
                row2 = next(r2)
                trades2 = np.append(trades2,
                                    np.array([[
                                        float(row2['Open']),
                                        float(row2['High']),
                                        float(row2['Low']),
                                        float(row2['Close']),
                                        float(row2['Adj Close']),
                                        float(row2['Volume'])
                                    ]]), axis=0)

    # 1. Using the correct axis, sum the columns for both your arrays,
    # and display the total volume traded for both years. Also calculate and
    # print the change in the traded volume from 2017 to 2016.
    total_volume_2016 = trades1.sum(axis=0)[-1]
    total_volume_2017 = trades2.sum(axis=0)[-1]
    print("Total volume traded in 2016: ", total_volume_2016)
    print("Total volume traded in 2017: ", total_volume_2017)
    print("Total volume traded in both years: ",
          total_volume_2016 + total_volume_2017)
    print("Difference in volume traded from 2017 to 2016: ",
          total_volume_2017 - total_volume_2016)

    # 2. Subtract the respective columns of both NumPy arrays and store
    # the results into a new array called change. Then sum up the columns
    # of this array and display just the volume traded.
    # Verify the result - it should be the same as the difference you
    # calculated in the previous step.
    change = np.subtract(trades2, trades1)
    print("Verifying...: ", change.sum(axis=0)[-1])

    # TODO: 3. Print one of your arrays, say the change array...

except IOError as e:
    print("IOError: ", e.with_traceback())

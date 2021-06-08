"""
Name: Ezgi Nihal Subasi
Date: 19.05.2021
Project: Linear Regression Using Gradient Descent

"""

import pandas as pd
import matplotlib.pyplot as plt
import random as random
import numpy as np


# reading csv file according to path and adds column names for separating class, x and y values
def reading_data(path):
    data = pd.read_csv(path)  # reading csv file
    first_row = []
    # appending first row in a list
    for i in range(0, 2):
        first_row.append(float(data.columns[i]))

    data.loc[-1] = first_row  # adding a row
    data.index = data.index + 1  # shifting index
    data = data.sort_index()  # sorting indexes

    data.columns = ["x", "y"]  # assigning column names
    return data


# visualizing data with analytical solution and sgd
def scatter_plot(plotted_df, analytical, sgd):
    x = plotted_df['x'].tolist()
    fig, ax = plt.subplots()
    # selecting x and y axises without labels
    ax.scatter(plotted_df['x'], plotted_df['y'], s=10)
    plt.plot(x, analytical, '-r', color="#C0C0C0", label='Analytical')
    plt.plot(x, sgd, '-r', color="#000000", label='SGD')
    plt.xlabel('x')  # entering name for x axis
    plt.ylabel('y')  # entering name for y axis
    plt.title("Dataset")  # entering a title for plot
    plt.show()


# analytical solution calculator
def analytical_solution(df):
    mean_x = df['x'].mean()
    mean_y = df['y'].mean()

    first_part = 0
    second_part = 0

    for i in range(len(df)):
        first_part += (df.loc[i, "x"] - mean_x) * (df.loc[i, "y"] - mean_y)
        second_part += (df.loc[i, "x"] - mean_x) ** 2

    w1 = first_part / second_part
    w0 = mean_y - w1 * mean_x

    return w0, w1


def stochastic_gradient_descent(df, learning_rate):
    y = df['y'].tolist()
    x = df['x'].tolist()
    w1 = random.uniform(-1, 1)
    w0 = random.uniform(-1, 1)

    old_err = 10000
    epoch = 0
    mse = []

    while True:
        epoch += 1
        for i, j in zip(x, y):

            w0 += (learning_rate * (j - ((w1 * i) + w0)))
            w1 += (learning_rate * (j - ((w1 * i) + w0))) * i

            predictions = predict(w1, w0, x)
            new_err = loss_func(predictions, y)
            mse.append(new_err)

            if new_err < old_err:
                old_err = new_err

            if new_err - old_err < 10 ** -7 and new_err < 0.008:
                print(f"Predicted Solutions: w1 = {w1} w0 = {w0}")
                return w1, w0, mse


def loss_func(y_predict, y_real):
    total = 0
    sample_numbers = len(y_predict)
    for i, j in zip(y_predict, y_real):
        total += (i - j) ** 2

    total = (1 / (sample_numbers)) * total

    return total


def predict(w_1, w_0, x_list):
    y_predict = []
    for i in x_list:
        y_predict.append((w_1 * i) + w_0)
    return y_predict


def plot_loss(mse):
    iterations = np.arange(1, len(mse) + 1, 1).tolist()
    fig, ax = plt.subplots()
    ax.scatter(iterations, mse, s=10)
    plt.plot(iterations, mse, '-r', color="BLUE")
    plt.xlabel('Iterations')  # entering name for x axis
    plt.ylabel('Loss')  # entering name for y axis
    plt.show()


if __name__ == "__main__":
    # ----DATA SET 1---- #
    data_path = "data1.csv"  # path of data training csv file
    data1 = reading_data(data_path)  # reading csv file with adding columns

    analytic_w0, analytic_w1 = analytical_solution(data1)

    print(f"Analytical Solutions: w1 = {analytic_w1} w0 = {analytic_w0}")

    for i in [0.001, 0.01, 0.1]:
        learning_rate = i
        w1, w0, mse = stochastic_gradient_descent(data1, learning_rate)

        x = data1['x'].tolist()

        analytical = predict(analytic_w1, analytic_w0, x)
        sgd = predict(w1, w0, x)
        scatter_plot(data1, analytical, sgd)
        plot_loss(mse)
        print("Final Loss Function Value: ", mse[-1])




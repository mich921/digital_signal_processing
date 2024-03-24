import numpy as np


# x(n) – 0.5x(n-1) = y(n)
def filter_function_one(input_signal):
    output_signal = np.zeros_like(input_signal)
    for i in range(2, len(input_signal)):
        output_signal[i] = input_signal[i] - 0.5 * input_signal[i-1]
    return output_signal


# 0.5 x(n) + 0.25x(n-1) +0.25x(n-2) = y(n).
def filter_function_four(input_signal):
    output_signal = np.zeros_like(input_signal)
    for i in range(2, len(input_signal)):
        output_signal[i] = 0.5 * input_signal[i] + 0.25 * input_signal[i-1] + 0.25 * input_signal[i-2]
    return output_signal


# x(n) – 0.5x(n-1) +0.5y(n-1) = y(n).
def filter_function_five(input_signal):
    output_signal = np.zeros_like(input_signal)
    for i in range(2, len(input_signal)):
        output_signal[i] = input_signal[i] - 0.5 * input_signal[i-1] + 0.5 * output_signal[i-1]
    return output_signal


# x(n) -0.5x(n-1) +0.5 x(n-2) + 0.5y(n-1) = y(n)
def filter_function_ten(input_signal):
    output_signal = np.zeros_like(input_signal)
    for i in range(2, len(input_signal)):
        output_signal[i] = input_signal[i] - 0.5 * input_signal[i-1] + 0.5 * input_signal[i-2] + 0.5 * output_signal[i-1]
    return output_signal
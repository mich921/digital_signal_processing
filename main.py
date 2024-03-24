import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import tkinter as tk
import tkinter.filedialog as fd
WAV_PATH = 'krokodil.wav'


def set_wav():
    filetypes = (("Текстовый файл", "*.wav"),)
    filename = fd.askopenfilename(title="Выбрать файл", initialdir="/", filetypes=filetypes)
    if filename:
        file = filename.rsplit("/", 1)[-1]
        global WAV_PATH
        WAV_PATH = filename
        print(WAV_PATH)
        # write_config(file, 1)
        text_file.set(f'Файл с клиентами: {file}')


# Функция для загрузки сигнала из файла WAV
def load_wav(filename):
    rate, data = wavfile.read(filename)
    return rate, data


# Функция для отображения графика сигнала
def plot_signal(signal, title):
    plt.figure()
    plt.plot(signal)
    plt.title(title)
    plt.xlabel('Время')
    plt.ylabel('Амплитуда')
    plt.show()


# Функция для вычисления и отображения амплитудно-частотной характеристики (АЧХ)
def plot_frequency_response(signal, title):
    signal = np.squeeze(signal)
    if len(signal.shape) > 1:
        signal = signal[:, 1]

    plt.figure()
    plt.magnitude_spectrum(signal, Fs=44100)
    plt.title(title)
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.show()


# region Реализация процедуры ЦФ
# 0.5 x(n) + 0.25x(n-1) +0.25x(n-2) = y(n).
def filter_function_four(input_signal):
    output_signal = np.zeros_like(input_signal)
    for i in range(2, len(input_signal)):
        output_signal[i] = 0.5 * input_signal[i] + 0.25 * input_signal[i-1] + 0.25 * input_signal[i-2]
    return output_signal


# x(n) -0.5x(n-1) +0.5 x(n-2) + 0.5y(n-1) = y(n)
def filter_function_ten(input_signal):
    output_signal = np.zeros_like(input_signal)
    for i in range(2, len(input_signal)):
        output_signal[i] = input_signal[i] - 0.5 * input_signal[i-1] + 0.5 * input_signal[i-2] + 0.5 * output_signal[i-1]
    return output_signal
# endregion

# Основная функция программы
def main():
    # Загрузка входного сигнала из файла WAV
    filename = WAV_PATH
    rate, input_signal = load_wav(filename)

    # Отображение входного сигнала
    plot_signal(input_signal, "Входной сигнал")

    # Применение процедуры ЦФ
    output_signal = filter_function_four(input_signal)

    # Отображение выходного сигнала
    plot_signal(output_signal, "Выходной сигнал")

    # Отображение АЧХ входного и выходного сигналов
    plot_frequency_response(input_signal, "АЧХ входного сигнала")
    plot_frequency_response(output_signal, "АЧХ выходного сигнала")


if __name__ == "__main__":
    win = tk.Tk()
    photo = tk.PhotoImage(file='krokodil.png')
    win.config(bg='#141414')
    win.iconphoto(True, photo)
    win.title("Krokodil")
    win.geometry('1200x550+100+100')

    # выбор пути к файлу
    text_file = tk.StringVar()
    text_file.set(f'Файл с музычкой: {WAV_PATH}')
    tk.Button(win, textvariable=text_file, command=set_wav,
              bg='#7FFFD4', activebackground="#00FF00", width=50, height=1).place(x=550, y=210)

    # жахнем
    start_button = tk.Button(win, text='Начинаем', bg='#7FFFD4', activebackground="#00FF00",
                             fg='black', command=main, width=40, height=3)
    start_button.place(x=860, y=70)
    win.mainloop()

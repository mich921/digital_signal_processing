from scipy.io import wavfile

import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import tkinter.filedialog as fd

from cfg import FUNCTION_CFG

WAV_PATH = 'krokodil.wav'
FUNC_CHOOSE = 0
FUNCTIONS = ["x(n) – 0.5x(n-1) = y(n)", "0.5 x(n) + 0.25x(n-1) +0.25x(n-2) = y(n)",
             "x(n) – 0.5x(n-1) +0.5y(n-1) = y(n)", "x(n) -0.5x(n-1) +0.5 x(n-2) + 0.5y(n-1) = y(n)"]


def set_wav():
    filetypes = (("Аудио файл", "*.wav"),)
    filename = fd.askopenfilename(title="Выбрать файл", initialdir="/", filetypes=filetypes)
    if filename:
        file = filename.rsplit("/", 1)[-1]
        global WAV_PATH
        WAV_PATH = filename
        print(WAV_PATH)
        text_file.set(f'Файл с музычкой: {file}')


def set_func(value):
    global FUNC_CHOOSE

    for key, func_value in enumerate(FUNCTIONS):
        if value == func_value:
            FUNC_CHOOSE = key
            break

    print(FUNC_CHOOSE)


def load_wav(filename: str):
    """Функция для загрузки сигнала из файла WAV"""
    rate, data = wavfile.read(filename)
    return rate, data


def plot_signal(signal, title):
    """Функция для отображения графика сигнала"""
    plt.figure(title)
    plt.plot(signal)
    plt.title(title)
    plt.xlabel('Время')
    plt.ylabel('Амплитуда')
    plt.show()


def plot_frequency_response(signal, title):
    """Функция для вычисления и отображения амплитудно-частотной характеристики (АЧХ)"""
    signal = np.squeeze(signal)
    if len(signal.shape) > 1:
        signal = signal[:, 1]

    plt.figure(title)
    plt.magnitude_spectrum(signal, Fs=44100)
    plt.title(title)
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.show()


def main():
    # Загрузка входного сигнала из файла WAV
    filename = WAV_PATH
    rate, input_signal = load_wav(filename)

    # Отображение входного сигнала
    plot_signal(input_signal, "Входной сигнал")

    # Применение процедуры ЦФ
    output_signal = FUNCTION_CFG[FUNC_CHOOSE](input_signal)

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
    win.geometry('600x400+100+100')

    # Создание выпадающего списка
    selected_func = tk.StringVar(win)
    selected_func.set(FUNCTIONS[FUNC_CHOOSE])  # Устанавливаем начальное значение
    # Создание OptionMenu
    tk.OptionMenu(win, selected_func, *FUNCTIONS, command=set_func).place(x=200, y=50)

    # выбор пути к файлу
    text_file = tk.StringVar()
    text_file.set(f'Файл с музычкой: {WAV_PATH}')
    tk.Button(win, textvariable=text_file, command=set_wav,
              bg='#7FFFD4', activebackground="#00FF00", width=50, height=1).place(x=140, y=200)

    # жахнем
    start_button = tk.Button(win, text='Начинаем', bg='#7FFFD4', activebackground="#00FF00",
                             fg='black', command=main, width=40, height=3)
    start_button.place(x=170, y=300)
    win.mainloop()

from Task5.comparesignal2 import *
import numpy as np
from Task6.Shift_Fold_Signal import Shift_Fold_Signal

def moving_average(guiobj):
    if len(guiobj.lst) == 1:
        if guiobj.expected_signal is None:
            print("Select Expected Output File")
            return
        output_file = guiobj.outfile_text.get("1.0", "end-1c")
        if output_file == "":
            print("Enter Output File Name")
            return
        sig = guiobj.lst[0]
        signal_values = sig.samples

    smoothed_signal = []
    window_size = int(guiobj.num_text.get("1.0", "end-1c"))

    # Adjust range to start from window_size - 1 to ensure a full window
    for i in range(window_size - 1, len(signal_values)):
        window = signal_values[i - window_size + 1:i + 1]
        smoothed_signal.append(sum(window) / window_size)

    # Display the smoothed signal
    SignalSamplesAreEqual(guiobj.outfile_name, smoothed_signal)

def remove_DC_avg(guiobj):
    if len(guiobj.lst) == 1:
        if guiobj.expected_signal is None:
            print("Select Expected Output File")
            return
        output_file = guiobj.outfile_text.get("1.0", "end-1c")
        if output_file == "":
            print("Enter Output File Name")
            return
        avg = np.average(guiobj.lst[0].samples)
        guiobj.lst[0].samples -= avg
        guiobj.lst[0].write_signal(output_file)
        SignalSamplesAreEqual(guiobj.outfile_name, guiobj.lst[0].samples)


def fold_signal(guiobj):
    if len(guiobj.lst) == 1:
        if guiobj.expected_signal is None:
            print("Select Expected Output File")
            return
        output_file = guiobj.outfile_text.get("1.0", "end-1c")
        if output_file == "":
            print("Enter Output File Name")
            return
        guiobj.lst[0].samples = guiobj.lst[0].samples[::-1]
        guiobj.lst[0].write_signal(output_file)
        Shift_Fold_Signal(guiobj.outfile_name, guiobj.lst[0].indices, guiobj.lst[0].samples)


def shift():
    pass


def fold_shift(guiobj):
    if len(guiobj.lst) == 1:
        if guiobj.expected_signal is None:
            print("Select Expected Output File")
            return
        output_file = guiobj.outfile_text.get("1.0", "end-1c")
        if output_file == "":
            print("Enter Output File Name")
            return
        fold_signal(guiobj)
        # multiply value of const by -1
        shift(guiobj)
        Shift_Fold_Signal(guiobj.outfile_name, guiobj.lst[0].indices, guiobj.lst[0].samples)


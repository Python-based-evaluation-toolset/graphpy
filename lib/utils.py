# List of reusable functions
import matplotlib.pyplot as plt


def plt_save_close(ax, file):
    plt.savefig(file, transparent=True)
    plt.clf()
    plt.close()

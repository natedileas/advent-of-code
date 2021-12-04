import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

INPUT = open('input.txt').read()
DEPTH = np.asarray(list(map(lambda i: int(i) * 10,
                            open('../1/input1.txt').read().splitlines())))


def plot_pos():
    x = 0
    y = 0

    for line in INPUT.splitlines():
        if not line:
            continue

        if line.startswith('forward'):
            x += int(line.replace('forward ', ''))
        elif line.startswith('down'):
            y -= int(line.replace('down ', ''))
        elif line.startswith('up'):
            y += int(line.replace('up ', ''))

        yield x, y


def plot_posv2():
    x = 0
    y = 0
    aim = 0

    for line in INPUT.splitlines():
        if not line:
            continue

        if line.startswith('forward'):
            w = int(line.replace('forward ', ''))
            x += w
            y += aim * w
        elif line.startswith('down'):
            aim += int(line.replace('down ', ''))
        elif line.startswith('up'):
            aim -= int(line.replace('up ', ''))

        yield x, y, aim


# plt.figure()
# plt.plot(DEPTH)
# x, y, a = map(np.asarray, zip(*plot_posv2()))
# dx, dy = map(np.asarray, zip(*plot_pos()))
# # plt.plot(x, y)
# plt.plot(dx, dy)
# plt.show()

n_frames = len(INPUT.splitlines())

with plt.rc_context({'axes.edgecolor': '#ffff66', 'xtick.color': '#ffff66', 'ytick.color': '#ffff66'}):
    pos = plot_posv2()
    fig, ax = plt.subplots(facecolor="#0f0f23")
    ax.set_facecolor("#0f0f23")
    ax.tick_params(color="#ffff66", which='both')
    ax.xaxis.label.set_color("#ffff66")
    ax.yaxis.label.set_color("#ffff66")

    xdata, ydata = [], []
    depthx, depthy = [], []
    ln, = plt.plot([], [], color="#ffff66")
    ln2, = plt.plot([], [], color="#ff4c4c")
    arrow = plt.arrow(0, 0, 1, 0, color="#ffff66")
    ax.set_xlim(0, 2007)
    ax.set_ylim(0, 668080)
    ax.invert_yaxis()
    #2007, 668080

    def update(frame):
        x, y, a = next(pos)
        arrow.set_data(x=x, y=y, dx=1, dy=a)
        xdata.append(x)
        ydata.append(y)
        depthx.append(x)
        depthy.append(y + DEPTH[frame])
        ln.set_data(xdata, ydata)
        ln2.set_data(depthx, depthy)
        ax.set_ylim(
            y - 50000,
            y + 50000)
        ax.invert_yaxis()
        return ln, arrow, ln2

    ani = FuncAnimation(fig, update, frames=range(
        n_frames), blit=True, interval=30)
    ani.save("movie.mp4")
    plt.show()

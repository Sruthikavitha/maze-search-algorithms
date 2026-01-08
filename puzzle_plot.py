import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_puzzle_state(state, step_number=None):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.set_aspect('equal')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.invert_yaxis()

    for r in range(3):
        for c in range(3):
            tile_value = state[r][c]
            rect = patches.Rectangle((c, r), 1, 1,
                                     linewidth=1,
                                     edgecolor='black',
                                     facecolor='lightgray')
            ax.add_patch(rect)

            if tile_value != 0:
                ax.text(c + 0.5, r + 0.5,
                        str(tile_value),
                        ha='center',
                        va='center',
                        fontsize=24)

    if step_number is not None:
        plt.title(f"Step {step_number}", fontsize=16)
    else:
        plt.title("Puzzle State", fontsize=16)

    plt.show()


# ✅ THIS PART MAKES IT RUN
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    plot_puzzle_state(initial_state, step_number=1)

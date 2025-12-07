import gradio as gr
import matplotlib
matplotlib.use("Agg")  # safe backend
import matplotlib.pyplot as plt
import io
from PIL import Image
import time
import numpy as np
import random

# bubble sort function with steps tracking
def bubble(a):
    n = len(a)
    steps = [(a.copy(), "Initial array")]
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                steps.append((a.copy(), f"Swapped indices {j} and {j+1}"))
        if not swapped:
            break
    steps.append((a.copy(), "Sorted array"))
    return steps

# function to plot array as a bar chart with optional custom x positions
def plot_array(arr, positions=None, highlight=[], step_num=None, total_steps=None, sorted_banner=False, fixed_ylim=None):
    plt.figure(figsize=(6, 4))

    if positions is None or len(positions) != len(arr):
        positions = list(range(len(arr)))

    colors = ["skyblue"] * len(arr)
    for idx in highlight:
        if 0 <= idx < len(colors):
            colors[idx] = "orange"

    bars = plt.bar(positions, arr, color=colors, width=0.8, edgecolor="black")

    ax = plt.gca()
    ax.axes.get_yaxis().set_visible(False)

    # lock ticks and axis limits
    plt.xticks(range(len(arr)), range(len(arr)))
    plt.xlabel("Array Index")
    plt.xlim(-0.5, len(arr) - 0.5)   # <--- this line fixes the wobble

    if fixed_ylim is not None:
        plt.ylim(0, max(1, int(fixed_ylim)))
    else:
        m = max(arr) if arr else 1
        plt.ylim(0, m + 5)

    for spine in ax.spines.values():
        spine.set_visible(False)

    for rect, value in zip(bars, arr):
        plt.text(rect.get_x() + rect.get_width()/2, rect.get_height(), str(value),
                 ha="center", va="bottom")

    if step_num is not None and total_steps is not None and not sorted_banner:
        plt.title(f"Sorting, step {step_num} of {total_steps}", fontsize=12)
    if sorted_banner:
        plt.title("Array sorted!", fontsize=14, color="green")

    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return Image.open(buf)

# generator function to stream bubble sort steps with smooth horizontal swaps
def visualize_bubble_sort(input_str, speed):
    # parse and validate input
    try:
        tokens = [t.strip() for t in input_str.split(",") if t.strip() != ""]
        arr = [int(t) for t in tokens]
    except ValueError:
        yield None, "Input contains non-integers; please use commas and whole numbers"
        return

    if len(arr) < 2:
        yield None, "Please enter at least 2 numbers"
        return

    speed = max(0.01, float(speed))  # allow faster speeds

    steps_info = bubble(arr)
    total_steps = len(steps_info)
    fixed_ylim = max(arr) + 5
    prev_arr = steps_info[0][0]

    for idx, (step, info) in enumerate(steps_info, start=1):
        highlight = []

        if "Swapped indices" in info:
            diff_indices = [i for i in range(len(prev_arr)) if prev_arr[i] != step[i]]
            if len(diff_indices) == 2:
                idx1, idx2 = diff_indices
            else:
                idx1, idx2 = 0, 1

            highlight = [idx1, idx2]
            val1 = prev_arr[idx1]
            val2 = prev_arr[idx2]

            # smoother animation: increase frames
            frames = 10
            for alpha in np.linspace(0, 1, frames):
                positions = list(range(len(step)))  # default integer positions
                # only animate the two swapped bars
                positions[idx1] = idx1*(1-alpha) + idx2*alpha
                positions[idx2] = idx2*(1-alpha) + idx1*alpha

                msg = f"{val1} > {val2}, so swap (index {idx1}) and (index {idx2})"
                yield plot_array(prev_arr, positions=positions, highlight=highlight,
                                 step_num=idx, total_steps=total_steps, fixed_ylim=fixed_ylim), msg
                time.sleep(speed / frames)

            # show the final swapped state
            yield plot_array(step, highlight, step_num=idx, total_steps=total_steps,
                             fixed_ylim=fixed_ylim), f"finished swap of {val1} and {val2}"
            time.sleep(speed)

        else:
            sorted_banner = (info == "Sorted array")
            yield plot_array(step, highlight, step_num=idx, total_steps=total_steps,
                             sorted_banner=sorted_banner, fixed_ylim=fixed_ylim), info
            time.sleep(speed)

        prev_arr = step.copy()

# function to generate random array
def generate_random_array(num_elements, lower_limit, upper_limit):
    lower = max(0, int(lower_limit))
    upper = min(100, int(upper_limit))
    if lower > upper:
        lower, upper = upper, lower
    arr = [random.randint(lower, upper) for _ in range(int(num_elements))]
    return ",".join(map(str, arr))

# gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Learning Algorithms: Bubble Sort")
    gr.Markdown("Bubble Sort repeatedly compares adjacent elements and swaps them if they're in the wrong order.")
    gr.Markdown("Enter or generate an array to be sorted, then press Run Sort to watch the algorithm work its magic!")

    with gr.Row():
        input_box = gr.Textbox(label="Enter numbers separated by commas", placeholder="e.g. 5,3,8,1")
        speed_slider = gr.Slider(0.01, 1.0, step=0.01, value=0.5, label="Animation speed (seconds per step)")

    with gr.Row():
        num_elements_slider = gr.Slider(2, 20, step=1, value=5, label="# of elements in random array")
        lower_limit_slider = gr.Slider(0, 100, step=1, value=0, label="Lower limit of random values")
        upper_limit_slider = gr.Slider(0, 100, step=1, value=50, label="Upper limit of random values")

    with gr.Row():
        random_button = gr.Button("Generate Random Array")
        sort_button = gr.Button("Run Sort")

    output_image = gr.Image(label="Sorting Animation")
    output_text = gr.Textbox(label="Current Step")

    sort_button.click(visualize_bubble_sort, [input_box, speed_slider], [output_image, output_text])
    random_button.click(generate_random_array, [num_elements_slider, lower_limit_slider, upper_limit_slider], input_box)

demo.launch(share=True)
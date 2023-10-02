---
icon: octicons/desktop-download-24
description: Installation instructions
---

# Installation

CAREamics is a deep-learning library and we therefore recommend having GPU support as
training the algorithms on the CPU can be very slow. MacOS users can also benefit from
GPU-acceleration if they have an M1 or M2 chip.

## Step-by-step

1. We recommend using a virtual environment to install CAREamics.

    ```bash
    conda create -y -n careamics python=3.9
    conda activate careamics
    ```

2. Install PyTorch following the [official instructions](https://pytorch.org/get-started/locally/).

3. You can verify that PyTorch has access to a GPU:

    ```bash
    python -m "import torch; print(torch.cuda.is_available())"
    ```

4. Install CAREamics using pip:

    === "Fully featured"
        The fully featured CAREamics include all the dependencies needed to run the
        notebooks, but that are not necessary to run CAREamics itself.

        ```bash
        pip install "careamics[all]"
        ```

    === "Simple"
        If you only want to use CAREamics, you can install it without the extra
        dependencies.

        ```bash
        pip install careamics
        ```
        
## Quickstart

Once you have [installed CAREamics](installation.md), the easiest way to get started
is to look at the [applications](applications/index.md) for full examples and the 
[guides](guides/index.md) for in-depth tweaking.
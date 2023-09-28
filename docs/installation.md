# Installation

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

    ```bash
    pip install careamics
    ```

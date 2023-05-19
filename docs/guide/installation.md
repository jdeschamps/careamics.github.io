# Installation


## Pre-requisite

git
conda

## Installation steps


1. Create a conda environment:
    ```console
    $ conda create -n juglab-torch python=3.10 
    ```

2. Set-up `torch` using the 
[official guidelines](https://pytorch.org/get-started/locally/) for your os:

    === "Windows"
        ```console
        $ pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu117
        ```
    === "macOS/Linux"
        ```console
        $ pip3 install torch torchvision
        ```

3. Install the juglab torch suite





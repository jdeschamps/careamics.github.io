---
icon: octicons/desktop-download-24
description: Installation instructions
---

# Installation

CAREamics is a deep-learning library and we therefore recommend having GPU support as
training the algorithms on the CPU can be very slow. MacOS users can also benefit from
GPU-acceleration if they have the new chip generations (M1, M2, etc.).

## Step-by-step

We recommend using [conda 
(miniconda)](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) or 
[mamba (miniforge)](https://github.com/conda-forge/miniforge#download) to install 
all packages in a virtual environment. 


=== "mamba"

    === "Linux"
        1. Open the terminal and type `mamba` to verify that mamba is available.
        2. Create a new environment:
            
            ``` bash
            mamba create -n careamics python=3.10
            mamba activate careamics
            ```

        3. Install PyTorch (you can find the official instructions 
        [here](https://pytorch.org/get-started/locally/)):

            ``` bash
            mamba install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
            ```
        
        4. Verify that the GPU is available:
            
            ``` bash
            python -c "import torch; print([torch.cuda.get_device_properties(i) for i in range(torch.cuda.device_count())])"
            ```

            This should show a list of available GPUs.
        
        5. Install CAREamics:

            ``` bash
            pip install --pre "careamics[all]"
            ```

        These instructions were tested on a linux virtual machine (RedHat 8.6) with a 
        NVIDIA A40-8Q GPU.

    === "macOS"
        
        (Instructions to come)

    === "Windows"
        In Windows systems, we will use unix-style commands. To do so, we recommend
        installing [Git for Windows](https://gitforwindows.org/) and using it as your
        terminal.

        (Instructions to come)

=== "conda"

    === "Linux"

        1. Open the terminal and type `mamba` to verify that mamba is available.
        2. Create a new environment:
            
            ``` bash
            mamba create -n careamics python=3.10
            mamba activate careamics
            ```

        3. Install PyTorch (you can find the official instructions 
        [here](https://pytorch.org/get-started/locally/)):

            ``` bash
            mamba install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
            ```
        
        4. Verify that the GPU is available:
            
            ``` bash
            python -c "import torch; print([torch.cuda.get_device_properties(i) for i in range(torch.cuda.device_count())])"
            ```

            This should show a list of available GPUs.
        
        5. Install CAREamics:

            ``` bash
            pip install --pre "careamics[all]"
            ```

        These instructions were tested on a linux virtual machine (RedHat 8.6) with a 
        NVIDIA A40-8Q GPU.

    === "macOS"
        
        (Instructions to come)

    === "Windows"
        In Windows systems, we will use unix-style commands. To do so, we recommend
        installing [Git for Windows](https://gitforwindows.org/) and using it as your
        terminal.

        (Instructions to come)


        
## Quickstart

Once you have [installed CAREamics](installation.md), the easiest way to get started
is to look at the [applications](applications/index.md) for full examples and the 
[guides](guides/index.md) for in-depth tweaking.
# Configuration

CAREamics relies on a configuration, either a Python object or a `.yml` file. The
configuration holds all the information necessary to train a CAREamics model.

## Minimum configuration

??? note "Minimum `.yml` file example"

    ```yaml
    working_directory: .
    experiment_name: ConfigTest

    algorithm:
        is_3D: false
        loss: n2v
        model: UNet

    data:
        axes: SYX
        data_format: tif
        in_memory: true

    training:
        augmentation: true
        batch_size: 16
        lr_scheduler:
            name: ReduceLROnPlateau
        num_epochs: 100
        optimizer:
            name: Adam
        patch_size: [64,64]
    ```

## In-depth

- [Full description](config_description.md)
- Instantiate a configuration
- Modify a configuration
- Import/export a configuration
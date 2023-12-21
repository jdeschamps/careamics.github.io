# Engine

The `Engine` class is the main class of CAREamics. It is used to train and predict with
CAREamics models.

## Create an Engine object

There are three ways to create an `Engine` object:

- Provide a configuration (object)
- Provide a configuration file (path)
- Provide a model (path)


=== "from a Configuration object"

    ```python
    from careamics import Configuration, Engine

    # create configuration
    parameters = {...} # see Configuration section
    config = Configuration(**parameters)

    # create engine
    engine = Engine(config=config)
    ```

=== "from a Configuration `.yaml`"

    ```python
    from careamics import Engine

    # create engine
    engine = Engine(config_path="path/to/file")
    ```

=== "from a Model"

    ```python
    from careamics import Engine

    # create engine
    engine = Engine(model_path="path/to/model")
    ```

## Usage

Here are a few in-depth tutorials for how to use the CAREamics engine:

- Train a model
- Predict with a model
- Export a model
- Re-train a model


## Frequently asked questions

(coming soon)
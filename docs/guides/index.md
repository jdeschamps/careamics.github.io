---
icon: octicons/repo-24
description: Guides
---

# Guides

In this section, we provide a few key examples on how to use CAREamics. The general
API is the following:

```python
# Create or modify a configuration
my_config = Configuration("path/to/config.yml")

# Instantiate an Engine to train a model
engine = Engine(config=my_config)

# Train using your data
engine.train(
    train_path="path/to/training/folder", 
    val_path="path/to/validation/folder"
)

# Save your model as a Bioimage Model Zoo model
engine.save_as_bioimage("path/to/model.bioimage.io.zip")

# After training, you can predict on new data
prediction = engine.predict(input=my_array)
```

## Categories

- [Configuration](configuration/index.md): how to configure CAREamics.
- [Engine](engine/index.md): how to train and predict with CAREamics.
- [Bioimage.io export](bmz/index.md): export and import CAREamics models.

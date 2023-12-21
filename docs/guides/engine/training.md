# Training

Training CAREamics is done via a single call to the `train` method of the `Engine`:

```python
# paths to the training and validation data
train_path = ...
val_path = ...

# train the Engine
train_stats, val_stats = engine.train(train_path=train_path, val_path=val_path)
```


## Frequently asked questions

- No validation data (train N2V on a single image)
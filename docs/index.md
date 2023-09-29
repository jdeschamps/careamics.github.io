---
icon: octicons/home-24
description: Guide and documentation.
---

<img src="assets/banner_careamics_large.png" width="400">

[![License](https://img.shields.io/pypi/l/careamics.svg?color=green)](https://github.com/CAREamics/careamics/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/careamics.svg?color=green)](https://pypi.org/project/careamics)
[![Python Version](https://img.shields.io/pypi/pyversions/careamics.svg?color=green)](https://python.org)
[![CI](https://github.com/CAREamics/careamics/actions/workflows/ci.yml/badge.svg)](https://github.com/CAREamics/careamics/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/CAREamics/careamics/branch/main/graph/badge.svg)](https://codecov.io/gh/CAREamics/careamics)

# Documentation

CAREamics is a PyTorch library aimed at simplifying the use of Noise2Void and its many
variants and cousins (N2V2, P(P)N2V, HDN etc.).

## Why CAREamics?

Noise2Void is a widely used denoising algorithm, and is readily available from the `n2v`
python package. However, n2v is based on TensorFlow and Keras and we found it 
increasingly hard to maintain. In addition, more recent methods (PPN2V, DivNoising,
HDN) are all implemented in PyTorch, but are lacking the extra features that would make
them usable by the community.

The aim of CAREamics is to provide a PyTorch library reuniting all the latest methods
in one package, while providing a simple and consistent API. In addition, we will
provide extensive documentation and tutorials on how to best apply these methods in a
scientific context.

## Getting started

Check out the following pages to get started:

- [Installation](installation.md): how to install CAREamics.
- [Guides](guides/index.md): in-depth guides on how to use CAREamics.
- [Applications](applications/index.md): full examples of CAREamics in action.
- [Algorithms](algorithms/index.md): a description of all the algorithms available in CAREamics.
- [Code reference](reference/index.md): a reference of all the functions and classes in CAREamics.

<!-- 
## Cite us -->
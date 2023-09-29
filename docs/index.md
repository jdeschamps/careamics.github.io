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


---
icon: octicons/home-24
description: Guide and documentation.
---

<img src="assets/banner_careamics_large.png" width="400">


# Documentation

CAREamics is a PyTorch library aimed at simplifying the use of Noise2Void and its many
variants and cousins (N2V2, P(P)N2V, HDN etc.).

## Yet another library?

Noise2Void is widely used denoising algorithm, and readily available from n2v python
package. However, n2v is based on TensorFlow and Keras and we found it increasingly
hard to maintain it. In addition, more recent methods (PPN2V, DivNoising, HDN) are all
implemented in PyTorch, but are lacking the extra features that would make them
effortlessly usable by the community.

The aim of CAREamics is to provide a PyTorch library reuniting all the latest methods
in one package, while providing a simple and consistent API. In addition, we will
provide extensive documentation and tutorials on how to best apply these methods in a
scientific context.

## Current state

Currently, CAREamics implements the following methods:

- N2V in 2D and 3D

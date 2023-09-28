# Noise2Void

Noise2Void (N2V) is a self-supervised denoising method. It trains by randomly masking
pixels in the input image and predicting their masked value from the surrounding pixels.

N2V relies on two fundamental hypotheses:

- The underlying structures are continuous
- The noise is pixel-wise independent

The corollory from these hypotheses is that if we consider the value of a pixel being
the sum of the true signal value and a certain amount of noise, then:

- The true signal value can be estimated from the surrounding pixels
- The noise cannot be estimated from the surrounding pixels

Therefore, in cases where the hypotheses hold, N2V can be use to estimate the true
signal and thereby removing the noise.

## Reference

Alexander Krull, Tim-Oliver Buchholz, and Florian Jug. "Noise2void-learning denoising
from single noisy images." Proceedings of the IEEE/CVF conference on Computer Vision
and Pattern Recognition. 2019.

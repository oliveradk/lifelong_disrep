# CULT: Continual Unsupervised Learning with aTpyicality-based Evironmental Selection



Inspired by [Aachille et al. 2018](https://arxiv.org/abs/1808.06508), we implement a simple continual learning framework with variational autoencoders and generative replay, where new environments are detected using the atypicality score of the latents, where atypicality is given by: 

{% raw %}
$$\alpha = D_{KL}(\mathcal{N}(\bar{\mu}_{z}, \bar{\sigma}_z)||\mathcal{N}(0,1))$$
{% endraw %}

NOTE: This repo is a work in progress - in particular the vase algorithm from Achille et al. has not properly been implemented (yet)

## Install

`pip install cult`

## Experiments

The primary experiment(s) are run in `02_core.cult.ipynb`

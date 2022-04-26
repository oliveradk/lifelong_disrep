# AUTOGENERATED! DO NOT EDIT! File to edit: 03a_core.train.ipynb (unless otherwise specified).

__all__ = ['reconstruction_loss', 'kl_div_target']

# Cell
import torch
from torch import nn
from torch.nn import functional as F
from ..config import DATA_PATH, PARAM_PATH


# Cell
def reconstruction_loss(x, x_rec):
    """Returns mean reconstruction loss across batch"""
    return torch.mean(rec_likelihood(x, x_rec))

# Cell
def kl_div_target(mu, logvar, C=0, gamma=1):
    """Returns target loss: squared difference of mean kldivergence and target C scaled by gamma"""
    return gamma * torch.mean(torch.abs((kl_div_stdnorm(mu, logvar) - C)))
#!/usr/bin/python3

__author__ = "Zhaobo Lu"

import numpy as np
import pandas as pd
import torch
import utils
from federated_learning import FederateLearning, FederatedUnlearningFeatures
from options import args_parser
import time
BATCH_SIZE = 1000


if __name__ == "__main__":
    args = args_parser()
    args.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # args.retain = True
    utils.set_random_seeds(args.seed)
    framework = FederateLearning(args)
    framework.federated_train()
    framework.finetuning()
    # framework.vertical_unlearning()
    # framework.retain()


import time
import logging

import torch
from torch.utils.data import DataLoader, TensorDataset
from torch import nn
from torch.autograd import Variable

import transformers
from transformers import GPT2Tokenizer
from transformers import GPT2LMHeadModel
from transformers import TextGenerationPipeline

from transformers import GPT2Model, GPT2Config

import pytorch_lightning as pl

import modlamp

from transformers import BertTokenizer

from datasets import load_dataset

from transformers import BigBirdModel, BertTokenizer

from torch.utils.data import DataLoader

from transformers import Trainer, TrainingArguments
# pipeline = TextGenerationPipeline(model, tokenizer)

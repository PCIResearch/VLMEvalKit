import torch
torch.set_grad_enabled(False)
torch.manual_seed(1234)
from .qwen_vl import QwenVL, QwenVLChat
from .pandagpt import PandaGPT
from .open_flamingo import OpenFlamingo
from .idefics import IDEFICS
from .llava import LLaVA
from .instructblip import InstructBLIP
from .visualglm import VisualGLM
from .minigpt4 import MiniGPT4
from .xcomposer import XComposer
from .mplug_owl2 import mPLUG_Owl2

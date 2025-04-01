import torch

use_cuda = torch.cuda.is_available()

if use_cuda:
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")
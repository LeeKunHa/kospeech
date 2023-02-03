import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import tensorflow
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())

import torch
print(torch.__version__)
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
print(torch.cuda.is_available())
print(torch.__version__)
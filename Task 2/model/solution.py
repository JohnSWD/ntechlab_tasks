import torch
import numpy as np
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models
from efficientnet_pytorch import EfficientNet
from pathlib import Path
import json

def get_model(weights: str, dev: str):
    fcls = EfficientNet.from_name('efficientnet-b3')
    fcls._fc = nn.Linear(in_features=1536, out_features=1, bias=True)

    state = torch.load(weights)
    fcls.load_state_dict(state)
    fcls.eval()
    if (dev=='gpu') and torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    fcls.to(device)
    return fcls, device

def predict(model, data_path: str, result_path: str, thr: float, device):
    transform = transforms.Compose(
        [transforms.Resize((128, 128)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.6239, 0.4606, 0.3827], [0.2218, 0.1894, 0.1748])])

    predictions, paths = [], []
    with torch.no_grad():
        for img_path in Path(data_path).glob('*.jpg'):
            paths.append(img_path.parts[-1])
            img = Image.open(img_path)
            img = transform(img).unsqueeze(0).to(device)
            output = torch.sigmoid(model(img))
            predictions.append('female') if output>0.4 else predictions.append('male')
    
    result = dict(zip(paths, predictions))

    with open(result_path, 'w') as fp:
        json.dump(result, fp)

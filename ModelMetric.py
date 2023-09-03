##计算模型的Params Flops
import torch
from timm.models import create_model
from thop import profile
model_path = ""
device = torch.device("cuda:0")
model = create_model('eva02_large_patch14_448.mim_m38m_ft_in22k_in1k', pretrained=True)
#model.load_state_dict(torch.load(model_path))
model.to(device)
input = torch.rand(8,3,448,448,device="cuda:0")
flops,params = profile(model,inputs=(input,))
print("FLOPs = " + str(flops/1000**3) + "G")
print("Params = " + str(params/1000**2) + "M")
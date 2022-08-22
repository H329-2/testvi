import pickle
import numpy as np

# f = open('onnx_out.pkl','rb')
# info_onnx = pickle.load(f)
# print(info_onnx)
with open('/home/lumos/results.pkl','rb') as f:
    info_trt = pickle.load(f)
# print(info)
runners_trt = list(info_trt.keys())
# runners_onnx = list(info_onnx.keys())

# print('onnx:', len(info_onnx.__getitem__(runners_onnx[0])[0]))
print('tensorrt:', len(info_trt.__getitem__(runners_trt[0])[0]))

# for layer in info_onnx.__getitem__(runners_onnx[0])[0]:
#     if layer in info_trt.__getitem__(runners_trt[0])[0]:    # 只分析相同名称的节点输出
#         print('--------------------------')
#         print(layer, info_onnx.__getitem__(runners_onnx[0])[0][layer].shape, info_trt.__getitem__(runners_trt[0])[0][layer].shape)
#         onnx_out = info_onnx.__getitem__(runners_onnx[0])[0][layer]
#         trt_out = info_trt.__getitem__(runners_trt[0])[0][layer]
#         np.testing.assert_allclose(onnx_out, trt_out, 0.0001, 0.0001)

for layer in info_trt.__getitem__(runners_trt[0])[0]:
    print("--------------------------------------")
    print(info_trt.__getitem__(runners_trt[0])[0][layer].shape, '\n', '*'*10)
    print(trt_out = info_trt.__getitem__(runners_trt[0])[0][layer])
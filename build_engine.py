import torch
import tensorrt as trt
from pathlib import Path
import os

# --------- USER CONFIGURABLE INPUTS ---------
ONNX_MODEL_PATH = "/mnt/wato-drive2/perception_models/traffic_signs_v3.onnx"
TENSORRT_ENGINE_PATH = "/mnt/wato-drive2/perception_models/traffic_signs.engine"
MAX_BATCH_SIZE = 1
CHANNELS = 3
HEIGHT = 1024
WIDTH = 1024
FP16 = True
INT8 = False
# --------------------------------------------

def build_engine(onnx_model_path, tensorRT_model_path, max_batch_size, channels, height, width, fp16=True, int8=False):
    logger = trt.Logger(trt.Logger.VERBOSE)
    builder = trt.Builder(logger)
    config = builder.create_builder_config()
    cache = config.create_timing_cache(b"")
    config.set_timing_cache(cache, ignore_mismatch=False)
    total_memory = torch.cuda.get_device_properties(0).total_memory
    config.set_memory_pool_limit(trt.MemoryPoolType.WORKSPACE, total_memory)
    flag = 1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)
    network = builder.create_network(flag)
    parser = trt.OnnxParser(network, logger)
    with open(onnx_model_path, "rb") as f:
        if not parser.parse(f.read()):
            print("ERROR: Cannot read ONNX FILE")
            for error in range(parser.num_errors):
                print(parser.get_error(error))
            return
    inputs = [network.get_input(i) for i in range(network.num_inputs)]
    outputs = [network.get_output(i) for i in range(network.num_outputs)]
    for input in inputs:
        print(f"Model {input.name} shape:{input.shape} {input.dtype}")
    for output in outputs:
        print(f"Model {output.name} shape: {output.shape} {output.dtype}")
    if max_batch_size > 1:
        profile = builder.create_optimization_profile()
        min_shape = [1, channels, height, width]
        opt_shape = [3, channels, height, width]
        max_shape = [max_batch_size, channels, height, width]
        for input in inputs:
            profile.set_shape(input.name, min_shape, opt_shape, max_shape)
        config.add_optimization_profile(profile)
    if fp16:
        config.set_flag(trt.BuilderFlag.FP16)
    elif int8:
        config.set_flag(trt.BuilderFlag.INT8)
    engine_bytes = builder.build_serialized_network(network, config)
    assert engine_bytes is not None, "Failed to create engine"
    print("BUILT THE ENGINE")
    with open(tensorRT_model_path, "wb") as f:
        f.write(engine_bytes)
    print(f"FINISHED WRITING: {tensorRT_model_path}")

if __name__ == "__main__":
    if not os.path.exists(ONNX_MODEL_PATH):
        print(f"ONNX model not found at {ONNX_MODEL_PATH}")
        exit(1)
    build_engine(
        ONNX_MODEL_PATH,
        TENSORRT_ENGINE_PATH,
        MAX_BATCH_SIZE,
        CHANNELS,
        HEIGHT,
        WIDTH,
        FP16,
        INT8
    )
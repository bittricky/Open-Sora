# Define dataset
dataset = dict(
    type="VariableVideoTextDataset",
    data_path=None,
    num_frames=None,
    frame_interval=3,
    image_size=(None, None, None),
    transform_name="resize_crop",
)
bucket_config = {
    "240p": {1: (1.0, 128), 16: (1.0, 4), 48: (1.0, 4), 72: (1.0, 2)},
    "360p": {1: (1.0, 1), 16: (0.5, 2), 24: (0.5, 2), 72: (0.0, None)},
    "720p": {1: (1.0, 1), 16: (0.5, 1), 72: (0.0, None)},
    "1080p": {1: (1.0, 1)},
}

# Define acceleration
num_workers = 0
dtype = "bf16"
grad_checkpoint = True
plugin = "zero2"
sp_size = 1

# Define model
model = dict(
    type="STDiT2-XL/2",
    from_pretrained="PixArt-XL-2-1024-MS.pth",
    input_sq_size=512,  # pretrained model is trained on 512x512
    enable_flashattn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
    micro_batch_size=4,
)
text_encoder = dict(
    type="t5",
    from_pretrained="DeepFloyd/t5-v1_1-xxl",
    model_max_length=120,
    shardformer=True,
)
scheduler = dict(
    type="iddpm-speed",
    timestep_respacing="",
)

# Others
seed = 42
outputs = "outputs"
wandb = False

epochs = 1000
log_every = 10
ckpt_every = 1000
load = None

batch_size = 10  # only for logging
lr = 2e-5
grad_clip = 1.0



# 1.3B config for 1x B200

out_dir = 'out-1p3B'
eval_interval = 250
log_interval = 10

eval_iters = 200
always_save_checkpoint = True

wandb_log = False

dataset = 'openwebtext'

gradient_accumulation_steps = 1
batch_size = 64
block_size = 1024

n_layer = 24
n_head = 16
n_embd = 2048

dropout = 0.1

learning_rate = 1.5e-4
max_iters = 40000
lr_decay_iters = 40000
min_lr = 3e-5

weight_decay = 0.1
beta2 = 0.95

warmup_iters = 2000

init_from = 'resume'


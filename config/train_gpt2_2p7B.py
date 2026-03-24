

# 1.3B config for 1x B200

out_dir = 'out-2p7B'
eval_interval = 250
log_interval = 10

eval_iters = 200
always_save_checkpoint = True

wandb_log = False

dataset = 'openwebtext'

gradient_accumulation_steps = 2
batch_size = 32
block_size = 1024

n_layer = 32
n_head = 20
n_embd = 2560

dropout = 0.1

learning_rate = 1e-4
max_iters = 60000
lr_decay_iters = 60000
min_lr = 1e-5

weight_decay = 0.1
beta2 = 0.95

warmup_iters = 2000

init_from = 'resume'

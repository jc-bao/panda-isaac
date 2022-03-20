import argparse

import numpy as np
import torch
from autolab_core import YamlConfig

from panda_isaac.franka_vec_env import GymFrankaBlockVecEnv
from panda_isaac.draw import draw_transforms


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--cfg', '-c', type=str, default='cfg/rearrange.yaml')
  args = parser.parse_args()
  cfg = YamlConfig(args.cfg)

  vec_env = GymFrankaBlockVecEnv(cfg)

  def custom_draws(scene):
    franka = scene.get_asset('franka')
    for env_idx in scene.env_idxs:
      ee_transform = franka.get_ee_transform(env_idx, 'franka')
      draw_transforms(scene, [env_idx], [ee_transform])

  all_obs = vec_env.reset()
  t = 0
  while True:
    all_actions = torch.rand((vec_env.n_envs, *vec_env.action_space.shape))
    all_obs, all_rews, all_dones, all_infos = vec_env.step(all_actions)
    vec_env.render(custom_draws=custom_draws)
    t += 1
    if t == 50:
      vec_env.reset()
      t = 0
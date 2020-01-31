import argparse
import json
import os
from pathlib import Path


def get_root():
	project_root = str(Path(__file__).resolve().parent.parent)
	return project_root


parser = argparse.ArgumentParser()
parser.add_argument('--gan_type', type=str, default='infoGAN', choices=['dcGAN', 'infoGAN'], help='The type of GAN')
parser.add_argument('--dataset', type=str, default='mnist',
					choices=['mnist', 'fashion-mnist', 'cifar10_2class', 'svhn'],
					help='The name of dataset')
parser.add_argument('--split', type=str, default='', help='The split flag for svhn and stl10')
parser.add_argument('--epoch', type=int, default=50, help='The number of epochs to run')
parser.add_argument('--batch_size', type=int, default=256, help='The size of batch')
parser.add_argument('--input_size', type=int, default=28, help='The size of input image')
parser.add_argument('--input_channel', type=int, default=1, help='The size of input image')
parser.add_argument('--save_dir', type=str, default='models', help='Directory name to save the model')
parser.add_argument('--result_dir', type=str, default='results', help='Directory name to save the generated images')
parser.add_argument('--project_root', type=str, default=get_root())
parser.add_argument('--model_name', type=str, default='Debugging')
parser.add_argument('--output_activation', type=str, default='tanh')
parser.add_argument('--device_id', type=int, default=0)
parser.add_argument('--data_size', type=int, default=10000)
parser.add_argument('--z_dim', type=int, default=62)
parser.add_argument('--no_classes', type=int, default=10)


def get_config():
	config = parser.parse_args()
	return config


def save_config(config):
	save_dir = os.path.join(
		config.project_root, f'results/{config.model_name}')
	os.makedirs(save_dir, exist_ok=True)

	with open(f'{save_dir}/config.json', 'w') as fp:
		json.dump(config.__dict__, fp, indent=4, sort_keys=True)

	return
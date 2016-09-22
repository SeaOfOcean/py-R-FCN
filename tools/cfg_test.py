#!/usr/bin/env python

import _init_paths
from fast_rcnn.config import __C, cfg, cfg_from_file, cfg_from_list, get_output_dir
import argparse
import sys
import pprint

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Train a Fast R-CNN network')
    parser.add_argument('--cfg', dest='cfg_file',
                        help='optional config file',
                        default=None, type=str)
    parser.add_argument('--set', dest='set_cfgs',
                        help='set config keys', default=None,
                        nargs=argparse.REMAINDER)


    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()

    print('Called with args:')
    print(args)

    if args.cfg_file is not None:
        cfg_from_file(args.cfg_file)
    if args.set_cfgs is not None:
        cfg_from_list(args.set_cfgs)


    print('Using config:')
    pprint.pprint(cfg)
    print 'PROPOSAL_METHOD: {}'.format(cfg['TRAIN']['PROPOSAL_METHOD'])

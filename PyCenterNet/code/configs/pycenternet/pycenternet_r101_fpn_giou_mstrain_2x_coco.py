_base_ = './pycenternet_r50_fpn_giou_mstrain_2x_coco.py'
model = dict(
    pretrained='../checkpoints/pretrained/resnet101-5d3b4d8f.pth',
    backbone=dict(
        type='ResNet',
        depth=101,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch'))
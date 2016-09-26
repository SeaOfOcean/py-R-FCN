time ./tools/test_net.py --gpu 5 \
  --def models/pascal_voc/ResNet-101/rfcn_end2end/test_agonistic.prototxt \
  --net data/rfcn_models/resnet101_rfcn_final.caffemodel \
  --cfg experiments/cfgs/rfcn_end2end_ohem.yml 


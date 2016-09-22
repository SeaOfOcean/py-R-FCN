time ./tools/test_net.py --gpu 7 \
  --def models/pascal_voc/ResNet-50/rfcn_end2end/test_agonistic.prototxt \
  --net output/rfcn_end2end/voc_0712_trainval/resnet50_rfcn_iter_60000.caffemodel \
  --imdb voc_2007_test \
  --cfg experiments/cfgs/rfcn_end2end.yml


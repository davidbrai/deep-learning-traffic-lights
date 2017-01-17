## Recognizing Traffic Lights with Deep Learning

This repo contains the files used to train and run the classifier described in [this blog post](https://medium.com/@davidbrai/recognizing-traffic-lights-with-deep-learning-23dae23287cc).
This was done during a [challenge](https://challenge.getnexar.com/challenge-1) by Nexar to recognize traffic lights based on images taken by their dashcam app.

### Dependencies

[Caffe](https://github.com/BVLC/caffe) with python bindings.

### Directory contents:

`/model`: contain a caffe deploy.prototxt file and three weights files. The three weights files are used together in a model ensemble.

`/testing`: has jupyter notebook files that run the model and perform the weighted average.

`/training`: contains the files needed to train the model (except the training data)

### Training the model

The images were first converted to lmdb format and resized to 256x256 using this command:

```
GLOG_logtostderr=1 ~/caffe/build/tools/convert_imageset \
    --resize_height=256 --resize_width=256 --shuffle  \
    ~/nexar/images/ \
    ~/nexar/labels_test.txt \
    ~/nexar/lmdb/test_lmdb
```

Each model has a directory in `training` with some or all of the following files:
```
solver.prototxt   caffe solver file
solver_p2.prototxt  caffe solver file with lower base learning rate
train_val.prototxt  network training file
rotation_layer.py   python caffe layer for data augmentation with rotation
```

`squeeze_net_manual_scratch__os` was training from scratch. The other two models were fine-tuning from weights trained on ImageNet. The weights file is named `squeezenet_v1.0.caffemodel`.

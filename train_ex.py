# pip install yolov4==2.1.0
from tensorflow.keras import callbacks, optimizers
from yolov4.tf import SaveWeightsCallback, YOLOv4

yolo = YOLOv4(tiny=True)

yolo.classes = "coco.names"
yolo.input_size = 640
yolo.batch_size = 2
yolo.subdivision = 1

yolo.make_model()
yolo.load_weights("yolov4-tiny.conv.29", weights_type="yolo")

train_data_set = yolo.load_dataset("data/train.txt")
val_data_set = yolo.load_dataset("data/val.txt", training=False)
# data_set = yolo.load_dataset("darknet/data/train.txt", dataset_type="yolo")
# data: ./data/images/6.png 0,0.16124031007751932,0.046511627906976716,0.8186046511627905,0.7984496124031

lr = 1e-4
epochs = 50

optimizer = optimizers.Adam(learning_rate=lr)
yolo.compile(optimizer=optimizer, loss_iou_type="ciou")

def lr_scheduler_mini(epoch):
    if epoch < 1:
        return (epoch / 1) * lr
    elif epoch < int(epochs * 0.8):
        return lr
    elif epoch < int(epochs * 0.9):
        return lr * 0.1
    else:
        return lr * 0.01

def lr_scheduler(epoch):
    if epoch < 1000:
        return (epoch / 1000) * lr
    elif epoch < int(epochs * 0.8):
        return lr
    elif epoch < int(epochs * 0.9):
        return lr * 0.1
    else:
        return lr * 0.01


yolo.fit(
    train_data_set,
    epochs=epochs,
    callbacks=[
        callbacks.LearningRateScheduler(lr_scheduler_mini),
        callbacks.TerminateOnNaN(),
        # callbacks.TensorBoard(
        #     log_dir="/logs",
        # ),
        SaveWeightsCallback(
            yolo=yolo, weights_type="yolo", epoch_per_save=1000
        ),
    ],
    validation_data=val_data_set,
    validation_steps=100,
    validation_freq=100,
)

import os
from ultralytics import YOLO
from multiprocessing import freeze_support

def main():
    path_project = os.getcwd()
    model = YOLO('yolo26l-cls.pt')
    model.train(data=fr'{path_project}\train', epochs=100, imgsz=48, device='0', augment=True, visualize=True, save=True, optimize=True, cache=True)


if __name__ == '__main__':
    freeze_support()
    main()
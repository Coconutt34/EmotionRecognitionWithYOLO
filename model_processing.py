import os
import cv2
import cvzone
import time
from ultralytics import YOLO


global project_path
project_path = os.getcwd()

def video_process(path):
    face_emotion_model = YOLO(fr'{project_path}\classification.pt')
    face_detect_model = YOLO(fr'{project_path}\detection.pt')
    cap = cv2.VideoCapture(path)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cnt_frames = 0
    fps = None
    prev_frame_time = time.perf_counter()
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (width // 2, height // 2))
        if fps is not None:
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        face_result = face_detect_model.predict(frame, conf=0.65)
        cnt_frames += 1

        for info in face_result:
            parameters = info.boxes
            for box in parameters:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                h, w = y2 - y1, x2 - x1
                crop = frame[y1:y2, x1:x2]

                label = face_emotion_model(crop)
                top1_idx = label[0].probs.top1
                class_name = label[0].names[top1_idx]
                print(f'total emotion: {class_name}')

                cvzone.cornerRect(frame, [x1, y1, w, h], l=9, rt=3)
                cv2.putText(
                    frame,
                    class_name,
                    (x1, y1 - 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 0, 255),
                    2
                )

            new_frame_time = time.perf_counter()
            if (new_frame_time - prev_frame_time) >= 1:
                fps = cnt_frames / (new_frame_time - prev_frame_time)
                prev_frame_time = new_frame_time
                cnt_frames = 0

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


def cam_process(cap):
    face_emotion_model = YOLO(fr'{project_path}\classification.pt')
    face_detect_model = YOLO(fr'{project_path}\detection.pt')

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cnt_frames = 0
    fps = None
    prev_frame_time = time.perf_counter()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (width, height))
        if fps is not None:
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        face_result = face_detect_model.predict(frame, conf=0.65)
        cnt_frames += 1

        for info in face_result:
            parameters = info.boxes
            for box in parameters:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                h, w = y2 - y1, x2 - x1
                crop = frame[y1:y2, x1:x2]

                label = face_emotion_model(crop)
                top1_idx = label[0].probs.top1
                class_name = label[0].names[top1_idx]
                print(f'total emotion: {class_name}')

                cvzone.cornerRect(frame, [x1, y1, w, h], l=9, rt=3)
                cv2.putText(
                    frame,
                    class_name,
                    (x1, y1 - 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 0, 255),
                    2
                )

            new_frame_time = time.perf_counter()
            if (new_frame_time - prev_frame_time) >= 1:
                fps = cnt_frames / (new_frame_time - prev_frame_time)
                prev_frame_time = new_frame_time
                cnt_frames = 0

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
            break
    cap.release()
    cv2.destroyAllWindows()

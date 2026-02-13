import sys
import os
import cv2
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox,
                               QFileDialog, QListWidget, QDialog, QMainWindow)

from pygrabber.dshow_graph import FilterGraph
from Appdesign import Ui_MainWindow
from model_processing import cam_process, video_process


global project_path, skobka_open, skobka_close
project_path = os.getcwd()
skobka_open, skobka_close = '{', '}'

def change_the_main_text(*args):
    '''args[0] - случай;1-выбор видео;2- выбор камеры'''
    if args[0] == 1 and args[1]:
        args[2].ui.textBrowser.setText("Запуск распознавания(Кликните на текст)")
        args[2].ui.textBrowser.setStyleSheet(f"""
            QTextBrowser {skobka_open}
            border: 2px solid rgba(80, 80, 80, 0.13);
            border-radius: 20px;
            padding: 8px;
            background-color: rgba(90, 90, 90, 0.13);
            color: rgba(20, 20, 18, 0.4);
            font-size: 16pt;
            text-decoration: underline;
            font-style: italic;
            color: blue;
            {skobka_close}
        """)
    if args[0] == 2:
        args[2].ui.textBrowser.setText("Запуск распознавания(Кликните на текст)")
        args[2].ui.textBrowser.setStyleSheet(f"""
                    QTextBrowser {skobka_open}
                    border: 2px solid rgba(80, 80, 80, 0.13);
                    border-radius: 20px;
                    padding: 8px;
                    background-color: rgba(90, 90, 90, 0.13);
                    color: rgba(20, 20, 18, 0.4);
                    font-size: 16pt;
                    text-decoration: underline;
                    font-style: italic;
                    color: blue;
                    {skobka_close}
        """)



class VideoStreamApp(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Установка заголовка и размеров окна
        # self.setWindowTitle("Video Stream Selector")
        self.ui.camButton.setStyleSheet(fr'''
        QPushButton {skobka_open}
        border: 2px solid #8f8f91;
        background-color: #d1d1d1;
        
        border-radius: 30px;
        {skobka_close}
        
        QPushButton:pressed {skobka_open} 
            background-color: #aaaaaa;
        {skobka_close}
        ''')
        #background-image: url({project_path}\webcam.png));
        self.ui.videoButton.setStyleSheet(fr'''
        QPushButton {skobka_open}
            border: 2px solid #8f8f91;
            background-color: #d1d1d1;
            border-radius: 30px;
            
        {skobka_close}
        
        QPushButton:pressed {skobka_open} 
            background-color: #aaaaaa;
        {skobka_close}
        ''')
        #image: url({project_path}\videoicon.png));
        self.ui.textBrowser.setStyleSheet(fr'''
            QTextBrowser {skobka_open}
                border: 2px solid rgba(80, 80, 80, 0.13);
                border-radius: 20px;
                background-color: white;
                padding: 8px;
                background-color: rgba(90, 90, 90, 0.13);
                color: rgba(20, 20, 18, 0.4);
            {skobka_close}
        ''')
        self.tuning_ui()

    def tuning_ui(self):

        # Основные компоненты
        #self.label = QLabel("Выберите откуда будет идти видеопоток.", self)

        #self.videoButton = QPushButton("Выбрать видео", self)
        self.ui.videoButton.clicked.connect(self.select_video)

        #self.camButton = QPushButton("Выбрать веб-камеру", self)
        self.ui.camButton.clicked.connect(self.select_camera)



        # Размещение элементов на окне
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.ui.videoButton)
        h_layout.addWidget(self.ui.camButton)
        h_layout.addStretch()
        '''v_layout = QVBoxLayout()
        v_layout.addWidget(self.theme_button)
        v_layout.addStretch()
        v_layout.addWidget(self.label)
        v_layout.addLayout(h_layout)'''

        #self.setLayout(v_layout)


    def select_video(self):
        options = QFileDialog.Options()
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите видео файл", "",
                                                   "Видео файлы (*.mp4 *.avi *.mov);;Все файлы (*)", options=options)
        change_the_main_text(1, file_path, self)

        #if file_path:
         #   QMessageBox.information(self, "Выбранный файл", f"Вы выбрали файл: {file_path}")
        print(self.ui.textBrowser.mousePressEvent)
        self.ui.textBrowser.mousePressEvent = self.on_label_click_video


    def on_label_click_video(self, event):
        video_process(file_path)
        self.ui.textBrowser.setText("Выберите откуда будет идти видеопоток.\nПри выборе веб-камеры сделайте двойной щелчок")
        self.ui.textBrowser.setStyleSheet(f"""
            QTextBrowser {skobka_open}
            border: 2px solid rgba(80, 80, 80, 0.13);
            border-radius: 20px;
            padding: 8px;
            background-color: rgba(90, 90, 90, 0.13);
            color: rgba(20, 20, 18, 0.4);
            font-size: 16pt;
            font-style: italic;
            {skobka_close}
            """)
        self.ui.textBrowser.mousePressEvent = None

    def select_camera(self):
        cameras = self.get_available_cameras()

        if not cameras:
            QMessageBox.warning(self, "Ошибка", "Нет доступных видеокамер.")
            return

        camera_dialog = CameraSelectionDialog(cameras, self)
        camera_dialog.exec()

    def get_available_cameras(self):
        camera_indices = []
        non_simplify_indices = FilterGraph().get_input_devices()
        for index, name in enumerate(non_simplify_indices):
            camera_indices.append(name)

        return camera_indices


class CameraSelectionDialog(QDialog):
    def __init__(self, cameras, other_self):
        super().__init__()
        self.other_self = other_self
        self.setWindowTitle("Выбор веб-камеры")


        layout = QVBoxLayout()

        self.camera_list_widget = QListWidget()
        for index, camera in enumerate(start=1, iterable=cameras):
            self.camera_list_widget.addItem(f"{index}:  {camera}")

        layout.addWidget(self.camera_list_widget)

        self.setLayout(layout)
        self.camera_list_widget.itemDoubleClicked.connect(self.on_camera_selected)

    def on_camera_selected(self, item):
        self.camera_index = int(item.text().split(':')[0])
        self.camera_name = str(item.text().split(':')[1])
        change_the_main_text(2, self, self.other_self)

        self.other_self.ui.textBrowser.mousePressEvent = self.on_label_click_cam
        self.close()
        #self.start_capture(camera_index, camera_name)


    def on_label_click_cam(self, event):
        self.start_capture(self.camera_index, self.camera_name)

    def start_capture(self, index, name):
        cap = cv2.VideoCapture(index - 1, cv2.CAP_DSHOW)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                #QMessageBox.information(self, "Успех", f"{name} успешно запущена!")
                cam_process(cap)

            cap.release()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось открыть камеру")
        self.other_self.ui.textBrowser.setText(
            "Выберите откуда будет идти видеопоток.\nПри выборе веб-камеры сделайте двойной щелчок")
        self.other_self.ui.textBrowser.setStyleSheet(f"""
            QTextBrowser {skobka_open}
            border: 2px solid rgba(80, 80, 80, 0.13);
            border-radius: 20px;
            padding: 8px;
            background-color: rgba(90, 90, 90, 0.13);
            color: rgba(20, 20, 18, 0.4);
            font-size: 16pt;
            font-style: italic;
            {skobka_close}
        """)
        self.other_self.ui.textBrowser.mousePressEvent = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoStreamApp()
    window.show()
    sys.exit(app.exec())
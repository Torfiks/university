"""Детекция объектов на видео с помощью YOLO — та же задача, что в ноутбуке,
оформленная отдельной программой.

Использование:
    python yolo_video_detect.py [путь_к_видео]

По умолчанию обрабатывает person-bicycle-car-detection.mp4, лежащий рядом.
"""
import sys
from collections import Counter
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO


def main():
    video_path = sys.argv[1] if len(sys.argv) > 1 else 'person-bicycle-car-detection.mp4'
    if not Path(video_path).exists():
        sys.exit(f"Файл не найден: {video_path}")

    model = YOLO('yolov8n.pt')

    # stream=True — результаты выдаются генератором кадр за кадром,
    # а не копятся в памяти (важно для длинных видео)
    frames = model.predict(
        source=video_path, stream=True, save=True,
        project='runs/detect', name='script_video',
        exist_ok=True, verbose=False,
    )

    frame_stats = [Counter(r.boxes.cls.int().tolist()) for r in frames]
    print(f"Кадров обработано: {len(frame_stats)}")

    # График «число объектов по классам по кадрам» — упрощённый трекинг
    seen = sorted({c for f in frame_stats for c in f})
    plt.figure(figsize=(11, 4))
    for cid in seen:
        plt.plot([f.get(cid, 0) for f in frame_stats], label=model.names[cid])
    plt.xlabel('Кадр')
    plt.ylabel('Число объектов')
    plt.title('Объекты по кадрам видео (yolo_video_detect.py)')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Куда сохранилось видео с рамками
    out = Path('runs/detect/script_video')
    if out.exists():
        print("Результат:", *map(str, out.iterdir()), sep='\n  ')


if __name__ == '__main__':
    main()

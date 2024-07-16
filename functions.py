import os
import cv2
import cv2.data

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def get_camera():
  while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
      break

  capture.release()
  cv2.destroyAllWindows()


def generate_negative_files():
  with open('neg.txt', 'w') as f:
    for filename in os.listdir('dataset\\negatives'):
      f.write(f'negative/{filename}\n')


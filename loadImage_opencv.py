import cv2
import numpy as np
# img = cv2.imread('C:/Users/jorda/Pictures/1488259268phpI3BoKQ.jpeg', 1)
# imgs = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
# cv2.imshow('Image', imgs)
# cv2.waitKey(0)  # wait for an infinite amount of time to wait that we press a key on the keyboard
# cv2.destroyAllWindows()  # remove the image loaded so that it doesn't run and remain at the background
# print(type(imgs))
# print(imgs.shape)
# print("*******************************")
# print(imgs)
# cv2.destroyAllWindows()


"""Computer vision tutorial 3"""
# cap = cv2.VideoCapture(0)  # you can also parse a video file as an argument
# while True:
#     ret, frame = cap.read()
#     width = int(cap.get(3))
#     height = int(cap.get(4))
#     image = np.zeros(frame.shape, np.uint8)
#     smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#     image[:height // 2, :width // 2] = smaller_frame  # top-left
#     image[height // 2:, :width // 2] = smaller_frame  # bottom left
#     image[:height // 2, width // 2:] = smaller_frame  # top-right
#     image[height // 2:, width // 2:] = smaller_frame  # bottom-left
#     cv2.imshow('frame', image)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

"""Drawing with opencv tutorial4"""
cap = cv2.VideoCapture(0)  # you can also parse a video file as an argument
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = cv2.line(frame, (0, 0), (width, height), (255,0,0), 10)
    image = cv2.line(image, (0, height), (width, 0), (0, 0, 255), 10)
    image = cv2.rectangle(image, (100, 100), (200, 200), (128, 128, 128), 5)
    image = cv2.circle(frame, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(image, 'Rufin is great!', (200, height-10), font, 1, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
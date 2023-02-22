import pytesseract
from pytesseract import Output
import PIL.Image
import cv2






"""
OCR Engiine Mode
0    Legacy engine only.
1    Neural nets LSTM engine only.
2    Legacy + LSTM engines.
3    Default, based on what is available.
"""



conf = r"--psm 6 --oem 3"

#text = pytesseract.image_to_string(PIL.Image.open("en.png"), config=conf)
#print(text)

img = cv2.imread("en.png")
height, width, _ = img.shape
boxes = pytesseract.image_to_boxes(img, config=conf)
"""for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)
"""

data = pytesseract.image_to_data(img, config=conf, output_type=dict)

amount_boxes = len(data["text"])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data["left"][i], data["top"][i], data["width"][i], data["height"][i])
        img = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
        img = cv2.putText(img, data["text"][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2,cv2.LINE_AA)


cv2.imshow("img", img)
cv2.waitKey(0)
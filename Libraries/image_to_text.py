import cv2
import pytesseract
import numpy as np
import regex as re


def provide_text(img, from_lang):
    org_text = pytesseract.image_to_string(img)
    # org_text = pytesseract.image_to_string(img, lang=from_lang)
    # To remove multiple new line characters
    processed_text = re.sub(r'\n\s*\n', '\n\n', org_text).strip()

    # To remove new line characters if they seem unnecessary
    processed_text = re.sub(r'[^.\s]\n', ' ', processed_text)

    return processed_text


def process_img(path, from_lang):
    img = cv2.imread(path)

    # Resize
    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    # Converting to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying dilation and erosion to remove the noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Applying blur
    img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255,
                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return provide_text(img, from_lang)

from flask import Flask, request, render_template
from PIL import Image
import io
import torch
from yolov5.detect import detect_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files['image'].read()
    image = Image.open(io.BytesIO(image))

    # Use YOLO to detect objects in the image
    result_image = detect_image(image)

    # Convert the result image to bytes to display in the HTML page
    img_bytes = io.BytesIO()
    result_image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    return render_template('result.html', result_img=img_bytes)

if __name__ == '__main__':
    app.run(debug=True)

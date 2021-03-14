from augmentation import *
import datetime
from PIL import Image
import numpy
import base64

# importing libraries
from flask import Flask, request, Response, jsonify, send_file
import datetime
app = Flask(__name__)
@app.route("/rotate", methods=["POST"])
def process_rotate():
    file = request.files['image']
    payload = request.form.to_dict()
    file.save('./im-received.jpg')

    if payload!={}:
        res = Augmentation.get_rotate('./im-received.jpg', int(payload['angle']))
    else:
        res = Augmentation.get_rotate('./im-received.jpg', 90)
    cv2.imwrite("res.png", res)
    with open('res.png', 'rb') as f:
        im_b64 = base64.b64encode(f.read()).decode('utf-8')
    return ({'msg': 'success', 'image': im_b64})

@app.route("/resize", methods=["POST"])
def process_resize():
    file = request.files['image']
    payload = request.form.to_dict()
    file.save('./im-received.jpg')

    if payload!={}:
        res = Augmentation.get_resize('./im-received.jpg', int(payload['lengthScale']), (int(payload['breadthScale'])))
    else:
        res = Augmentation.get_resize('./im-received.jpg', 50, 50)
    cv2.imwrite("res.png", res)
    with open('res.png', 'rb') as f:
        im_b64 = base64.b64encode(f.read()).decode('utf-8')
    return ({'msg': 'success', 'image': im_b64})


@app.route("/crop", methods=["POST"])
def process_crop():
    file = request.files['image']
    payload = request.form.to_dict()
    file.save('./im-received.jpg')
    if payload!={}:
        res = Augmentation.get_crop('./im-received.jpg', [int(payload['x']), int(payload['x1']), int(payload['y']), int(payload['y1'])])
    else:
        res = Augmentation.get_crop('./im-received.jpg', [100, 1000, 100, 1000])
    cv2.imwrite("res.png", res)
    with open('res.png', 'rb') as f:
        im_b64 = base64.b64encode(f.read()).decode('utf-8')
    return ({'msg': 'success', 'image': im_b64})

if __name__ == "__main__":
    print("testove")
    app.run(host='0.0.0.0', port=5000, debug=True)

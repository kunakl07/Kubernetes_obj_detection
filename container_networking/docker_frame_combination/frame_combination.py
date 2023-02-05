from flask import Flask, request, jsonify
import pickle
import cv2

app = Flask(__name__)
li = []
@app.route("/frame_combination", methods = ["POST"])
def receive_data():
    data_pickled = pickle.loads(request.data)
    print(data_pickled)
    # cv2.imshow('Frame', data_pickled)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()


    if cv2.waitKey(1) & 0xFF == ord('q'):
        return
    return jsonify({'status': 'success'})


if __name__ == "__main__":
    app.run(port=8082, host='0.0.0.0')



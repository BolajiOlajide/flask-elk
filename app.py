from workerA import add_nums
from workerB import sub_nums
from flask import (
   Flask,
   request,
   jsonify,
)


app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Working!!"})


@app.route("/add")
def add():
    first_num = request.args.get("first_num")
    second_num = request.args.get("second_num")
    print(request.args, first_num, second_num)
    result = add_nums.delay(first_num, second_num)
    print(dir(result), "<====", result.status, result.successful(), result.worker)
    return jsonify({"result": "result"}), 200


@app.route("/subtract")
def subtract():
    first_num = request.args.get("first_num")
    second_num = request.args.get("second_num")
    result = sub_nums.delay(first_num, second_num)
    print(result, "<====")
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, request, jsonify
import pandas as pd
import eda_utils
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow React frontend to connect


@app.route("/upload-csv/", methods=["POST"])
def upload_csv():
    try:
        # Get uploaded file
        file = request.files["file"]
        df = pd.read_csv(file)

        # Run EDA pipeline
        results = eda_utils.run_full_eda(df)

        return jsonify({"status": "success", "eda_results": results})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

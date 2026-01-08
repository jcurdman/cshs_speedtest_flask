from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000      # Mbps
    ping_result = st.results.ping

    return jsonify({
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),
        "ping": round(ping_result, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
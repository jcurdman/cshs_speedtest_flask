from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    # Get the results object
    results = st.results
    # Access the ISP name attribute
    isp_name = results.client.get('isp', 'Unknown Network')
    return render_template('index.html', isp_name=isp_name)

@app.route('/speedtest')
def run_speedtest():
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000      # Mbps
    ping_result = st.results.ping

    net_image = "static/img/good_net.jpg"
    if download_speed < 10:
        net_speed = "static/img/poor_net.jpg"

    network_result = jsonify({
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),
        "ping": round(ping_result, 2),
        "net_image": net_image
    })

    return network_result

if __name__ == '__main__':
    app.run(debug=True)
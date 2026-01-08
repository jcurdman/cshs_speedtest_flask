async function runSpeedtest() {
      document.getElementById("results").innerHTML = "Testing...";
      const response = await fetch('/speedtest');
      const data = await response.json();
      document.getElementById("results").innerHTML = `
        <span>Download Speed: ${data.download} Mbps</span>
        <span>Upload Speed: ${data.upload} Mbps</span>
        <span>Ping: ${data.ping} ms</span>
      `;
      const imageElement = document.getElementById('dynamic-image');
      imageElement.src = data.net_image;
    }
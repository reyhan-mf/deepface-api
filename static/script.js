navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        document.getElementById('video').srcObject = stream;
    })
    .catch(err => {
        console.error('Error accessing webcam:', err);
    });

const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const video = document.getElementById('video');
const resultDiv = document.getElementById('result');

function sendFrame() {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('file', blob, 'frame.jpg');

        fetch('/detect', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.textContent = `Dominant Emotion: ${data.dominant_emotion}`;
        })
        .catch(err => console.error('Error sending frame:', err));
    });
}
setInterval(sendFrame, 1000);

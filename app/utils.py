from PIL import Image
import numpy as np
from deepface import DeepFace
import io

def analyze_emotion(file):
    image = Image.open(io.BytesIO(file.read()))
    frame = np.array(image)

    try:
        result = DeepFace.analyze(frame, actions=['emotion'])
        if isinstance(result, list) and len(result) > 0:
            result = result[0]
            return result.get('dominant_emotion', 'Unknown')
        else:
            return 'Error: Result format is not as expected.'
    except Exception as e:
        return f'Exception occurred: {e}'

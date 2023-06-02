from eaxtension import jsonE
from eaxtension import LogE
import numpy as np

data = jsonE.load("../fft_data.json")

LogE.d("y data - length", len(list(data["y"])))         # TODO json에 저장된 데이터 list화 시키고 튀는 값 추출하기
LogE.d("x data - length", len(list(data["x"])))
LogE.d("data", len(data["data"]))

audio_byte = bytes(data["pyaudio"][1:], "utf-8")
LogE.d("audio to byte", audio_byte)

audio_dat = np.frombuffer(audio_byte, dtype=np.int16)

LogE.d("audio data (np frombuffer)", audio_dat)

# for i, y in enumerate(list(data["y"])):
#     if int(y) > 0:
#         LogE.d(f"index: {i}", y)
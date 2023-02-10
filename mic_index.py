import pyaudio
from eaxtension import jsonE
from eaxtension import LogE

p = pyaudio.PyAudio()

sav_text = {}

for i in range(p.get_device_count()):
    desc = p.get_device_info_by_index(i)

    if desc["maxInputChannels"] != 0:
        sav_text[desc["index"]] = desc
        LogE.d("desc index", desc["index"])
        LogE.d("desc data", desc)
        LogE.g("sav in for", sav_text)

LogE.d("sav data", sav_text)

jsonE.dumps("mic_index", sav_text)
import pyaudio
from eaxtension import jsonE
from eaxtension import LogE

p = pyaudio.PyAudio()

sav_text = {"all_input_device":{}}
i_index = []
mic_sav = {}
sav_all = sav_text["all_input_device"]

for i in range(p.get_device_count()):
    desc = p.get_device_info_by_index(i)

    if desc["maxInputChannels"] != 0:
        sav_all[desc["index"]] = desc
        i_index.append(desc["index"])

for i in i_index:
    text = sav_all[i]["name"]
    if text.find("Microphone") != -1 :
        mic_sav[i] = sav_all[i]

sav_text["only_mic"] = mic_sav

jsonE.dumps("mic_index", sav_text)

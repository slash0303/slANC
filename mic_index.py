import pyaudio


p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    desc = p.get_device_info_by_index(i)

    if desc["maxInputChannels"] != 0:
        print(desc)


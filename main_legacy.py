import sys

import pyaudio
import numpy as np
from matplotlib import pyplot as plt
import libr.osa

class audio_handler:

    def __init__(self):
        # RATE = 샘플링 주기
        self.RATE = 44100
        # CHANNELS = 채널 수
        self.CHANNELS = 1
        # FORMAT = 포맷
        self.FORMAT = pyaudio.paFloat32
        # CHUNK = frames per buffer (이건 나도 모르겠음;)
        self.CHUNK = 1024 * 2

        # p에 pyaudio 할당
        self.p = pyaudio.PyAudio()
        # documentation에서 그냥 인스턴스에 할당하지 말고 .open으로 열라고 했음. 왜 인지는 모름;
        self.stream = self.p.open(
            # 각 변수에 위에서 지정한 값들 할당
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=False,
            frames_per_buffer=self.CHUNK
        )
        self.init_plots()
        self.strt_plots()

    # 그래프 출력을 위한 initalize(초기 세팅)
    def init_plots(self):

        # x = 반열린구간 [0, 2*self.CHUNK)에서 2씩 떨어져있는 숫자들을 array로 반환
        x = np.arange(0, 2 * self.CHUNK, 2)
        # xf = 0과 self.RATE사이에 self.CHUNK개 만큼 정수를 끼워넣음
        xf = np.linspace(0, self.RATE, self.CHUNK)

        # 이건 또 무슨 코드냐
        self.fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))





handler = audio_handler()
handler.start()
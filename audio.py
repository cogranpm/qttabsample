import soundcard as sc
import numpy
import time

def test_sound_card():
    num_frames = 48000
    sample_rate = 48000
    speakers = sc.all_speakers()
    default_speaker = sc.default_speaker()
    mics = sc.all_microphones()
    default_mic = sc.default_microphone()


    #data = default_mic.record(samplerate=sample_rate, numframes=num_frames)
    #time.sleep(5)
    #print(data)
    #default_speaker.play(data/numpy.max(data), samplerate=sample_rate)

    with default_mic.recorder(samplerate=sample_rate) as mic, \
        default_speaker.player(samplerate=sample_rate) as sp:
        for _ in range(300):
            data = mic.record(numframes=1024)
            sp.play(data=data)

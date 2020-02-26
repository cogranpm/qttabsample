# soundcard lib imports
import soundcard as sc
import numpy
import time
import threading

# pyaudio imports
from array import array
from struct import pack
from sys import byteorder
import copy
import pyaudio
import wave

# pyaudio constants
THRESHOLD = 500  # audio levels not normalised.
CHUNK_SIZE = 1024
SILENT_CHUNKS = 3 * 44100 / 1024  # about 3sec
FORMAT = pyaudio.paInt16
FRAME_MAX_VALUE = 2 ** 15 - 1
NORMALIZE_MINUS_ONE_dB = 10 ** (-1.0 / 20)
RATE = 44100
CHANNELS = 1
TRIM_APPEND = RATE / 4

# soundcard constants
audio_data = []
num_frames = 48000
sample_rate = 48000

def get_default_mic():
    #speakers = sc.all_speakers()
    #mics = sc.all_microphones()
    default_mic = sc.default_microphone()
    print(default_mic.channels)
    return sc.default_microphone()

def get_default_speaker():
    default_speaker = sc.default_speaker()
    print(default_speaker)
    return default_speaker

def play_audio(default_speaker):
    with default_speaker.player(samplerate=sample_rate) as sp:
        for audio_segment in audio_data:
            sp.play(data=audio_segment)
    print("played it")

def write_audio(file_name):
    pass


def test_sound_card(dummy, default_mic, file_name):
    audio_data.clear()
    print(dummy)
    print(file_name)
    wav_file = wave.open(file_name, 'w')
    wav_file.setnchannels(default_mic.channels)
    wav_file.setsampwidth(1)
    wav_file.setframerate(sample_rate)

    t = threading.current_thread()
    with default_mic.recorder(samplerate=sample_rate) as mic:
        while getattr(t, 'do_run', True):
            data = mic.record(numframes=1024)
            audio_data.append(data)
            wav_file.writeframesraw(data)
            print(type(data)) # turns out this is a numpy array type
            print('Data:', len(data))
        #for _ in range(100):
        #    data = mic.record(numframes=1024)
            #sp.play(data=data)

    # the wav file doesn't sound right at present
    wav_file.close()
    print("done recording")
    #data = default_mic.record(samplerate=sample_rate, numframes=num_frames)
    #time.sleep(5)
    #print(data)
    #default_speaker.play(data/numpy.max(data), samplerate=sample_rate)

# pyaudio stuff
def is_silent(data_chunk):
    """Returns 'True' if below the 'silent' threshold"""
    return max(data_chunk) < THRESHOLD

def normalize(data_all):
    """Amplify the volume out to max -1dB"""
    # MAXIMUM = 16384
    normalize_factor = (float(NORMALIZE_MINUS_ONE_dB * FRAME_MAX_VALUE)
                        / max(abs(i) for i in data_all))

    r = array('h')
    for i in data_all:
        r.append(int(i * normalize_factor))
    return r

def trim(data_all):
    _from = 0
    _to = len(data_all) - 1
    for i, b in enumerate(data_all):
        if abs(b) > THRESHOLD:
            _from = max(0, i - TRIM_APPEND)
            break

    for i, b in enumerate(reversed(data_all)):
        if abs(b) > THRESHOLD:
            _to = min(len(data_all) - 1, len(data_all) - 1 - i + TRIM_APPEND)
            break

    return copy.deepcopy(data_all[_from:(_to + 1)])

def record():
    """Record a word or words from the microphone and
    return the data as an array of signed shorts."""

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)

    silent_chunks = 0
    audio_started = False
    data_all = array('h')

    while True:
        # little endian, signed short
        data_chunk = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            data_chunk.byteswap()
        data_all.extend(data_chunk)

        silent = is_silent(data_chunk)

        if audio_started:
            if silent:
                silent_chunks += 1
                if silent_chunks > SILENT_CHUNKS:
                    break
            else:
                silent_chunks = 0
        elif not silent:
            audio_started = True

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    data_all = trim(data_all)  # we trim before normalize as threshhold applies to un-normalized wave (as well as is_silent() function)
    data_all = normalize(data_all)
    return sample_width, data_all

def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h' * len(data)), *data)

    wave_file = wave.open(path, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(sample_width)
    wave_file.setframerate(RATE)
    wave_file.writeframes(data)
    wave_file.close()


def test_pyaudio():
    print('wait in silence to begin recording')
    record_to_file('demo.wav')
    print('done')

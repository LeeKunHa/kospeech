# import pathlib
# import wave

# def convert_to_wav(filepath):
#     with open(filepath, "rb") as r:
#         data = r.read()
#         with wave.open(str(filepath.with_suffix(".wav")), "wb") as w:
#             w.setparams((1, 2, 16000, 0, "NONE", "NONE"))
#             w.writeframes(data)

# path =  pathlib.Path("C:\STT_dataset\KsponSpeech_eval\eval_clean2\KsponSpeech_248001.pcm")
# #path = "C:\STT_dataset\KsponSpeech_eval\eval_clean2\KsponSpeech_E00001.pcm"
# convert_to_wav(path)

import os
file_size = os.path.getsize(r'C:\STT_dataset\KsponSpeech_01\KsponSpeech_0001\KsponSpeech_000001.pcm') 
print('File Size:', file_size, 'bytes')
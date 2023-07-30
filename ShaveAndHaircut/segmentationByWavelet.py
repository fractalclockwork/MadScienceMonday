# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # **Mad Science Monday**
#
# see also: https://musicinformationretrieval.com/peak_picking

# %%
# %matplotlib inline

# note that librosa must be loaded before matplotlib
# due to lazy_loading done in librosa
import librosa, librosa.display
import matplotlib.pyplot as plt

import IPython.display as ipd, numpy

#import stanford_mir; stanford_mir.init()

# %%
files = ['bat-shave.mp3', 'pgh-shave-and-a-haircut.mp3', 'DnShaveAndHaircut.mp3']
file = files[0]
x, sr = librosa.load(f'data/{file}')

# %%
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)

# %% [markdown]
# # **Audio Segmentation**
#
# see also:
# https://scikit-maad.github.io/_auto_examples/1_basic/plot_find_rois_simple.html

# %%
# #!pip install scikit-maad

# %%
from maad import sound
from maad.rois import find_rois_cwt
from maad.util import plot_spectrogram

Sxx, tn, fn, ext = sound.spectrogram(x, sr, nperseg=1024, noverlap=512)
plot_spectrogram(Sxx, extent=ext, db_range=60, gain=20, colorbar=False, figsize=(2.5,10))

# %%
df_trill = find_rois_cwt(x, sr, flims=(4500,8000), tlen=5, th=0, display=True, figsize=(10,6))
print(df_trill)

# %%

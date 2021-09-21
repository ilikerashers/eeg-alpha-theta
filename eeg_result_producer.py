# import matplotlib.pyplot as plt

import mne
from mne.datasets import sample
# import numpy as np
import time

from mne_realtime import RtEpochs, MockRtClient
from eeg_result_queue import PrioritizedItem

# Fiff file to simulate the realtime client
#data_path = sample.data_path()

data_path="E:/Work/eeg/mne_data/MNE-sample-data"
raw_fname = data_path + '/MEG/sample/sample_audvis_filt-0-40_raw.fif'
raw = mne.io.read_raw_fif(raw_fname, preload=True)

# print(raw.info.items())

# select gradiometers
picks = mne.pick_types(raw.info, meg='grad', eeg=True, eog=False,
                       stim=True, exclude=raw.info['bads'])

# select the right-visual condition
event_id, tmin, tmax = 3, -0.2, 0.5

# create the mock-client object
rt_client = MockRtClient(raw)

# create the real-time epochs object
rt_epochs = RtEpochs(rt_client, event_id, tmin, tmax, picks=picks,
                     decim=1)
# rt_epochs = RtEpochs(rt_client, event_id, tmin, tmax, picks=picks,
#                      decim=1, reject=dict(grad=4000e-13, eog=150e-6))



# def send_alpha_theta_ratio():
    # start the acquisition
rt_epochs.start()

# send raw buffers
rt_client.send_data(rt_epochs, picks, tmin=0, tmax=150, buffer_size=1000)

alpha_delta_ratio=0

# stuff to run always here such as class/def
def main():
    pass

def get_ratio():
    return alpha_delta_ratio

# if __name__ == "__main__":
#    # stuff only to run when not called via 'import' here

async def get_stats():
    while True:
        for ii, ev in enumerate(rt_epochs.iter_evoked()):
            print("Just got epoch %d" % (ii + 1))
            
            # Define delta lower and upper limits
            delta_low, delta_high = 0.5, 4
            alpha_low, alpha_high = 8, 12
            
            ev.pick_types(eeg=True)

            delta_psds, _ = mne.time_frequency.psd_multitaper(ev, fmin=delta_low, fmax=delta_high, n_jobs=1);
            alpha_psds, _ = mne.time_frequency.psd_multitaper(ev, fmin=alpha_low, fmax=alpha_high, n_jobs=1);
            
            delta_psds_mean = delta_psds.mean(0).mean(0)
            alpha_psds_mean = alpha_psds.mean(0).mean(0)
            print(alpha_psds_mean/delta_psds_mean)
            print("alpha/theta ratio:" + str(alpha_psds_mean/delta_psds_mean))
            alpha_delta_ratio = (alpha_psds_mean/delta_psds_mean)
            yield alpha_delta_ratio
            time.sleep(1)
        pass

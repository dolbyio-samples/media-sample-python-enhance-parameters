import time
import requests
import shutil
import os


import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile


def download_file(file_url, headers, output_path):
    args = {
        "url": file_url,
    }
    url = "https://api.dolby.com/media/output"

    # Create a request to download created file via DolbyIO Output API
    with requests.get(url, params=args, headers=headers, stream=True) as response:
        response.raise_for_status()
        response.raw.decode_content = True
        print("Downloading from {0} into {1}".format(response.url, output_path))
        with open(output_path, "wb") as output_file:
            shutil.copyfileobj(response.raw, output_file)

    return output_path


def upload_input_file(local_file_path, input_base_path, headers):
    filename = os.path.basename(local_file_path)
    cloud_file_path = '{}/{}'.format(input_base_path, filename)
    arguments = {
        "url": cloud_file_path,
    }
    url = "https://api.dolby.com/media/input"

    # Create a request to upload a file from local machine via DolbyIO Input API
    response = requests.post(url, json=arguments, headers=headers)
    response.raise_for_status()
    data = response.json()
    presigned_url = data["url"]

    # Upload your media to the pre-signed url response
    print("Uploading {0} to {1}".format(local_file_path, presigned_url))
    with open(local_file_path, "rb") as input_file:
        requests.put(presigned_url, data=input_file)

    return cloud_file_path


def convert_mp4_to_wav(mp4_file):
    # To use this function, you need to have ffmpeg installed on your computer
    wave_file = mp4_file.replace('mp4', 'wav')
    os.system('ffmpeg -i {} -ac 1 -f wav {}'.format(mp4_file, wave_file))

    return wave_file


def plot_a_waveform_and_spectrum(wave_file, title=None):
    # Create a figure object to make two plots
    fig = plt.figure(1)
    if title:
        fig.suptitle(title)

    # Plot a waveform of wav_file
    plot_waveform = plt.subplot(211)
    sample_rate, data = wavfile.read(wave_file)
    duration = len(data) / sample_rate
    time_data = np.linspace(0, duration, len(data))

    plot_waveform.plot(time_data, data)
    plot_waveform.set_xlabel('Time')
    plot_waveform.set_ylabel('Amplitude')
    ax = plt.gca()
    ax.set_xlim([0, 5])

    # Calculate and create a spectogram plot
    plot_spectrogram = plt.subplot(212)
    plot_spectrogram.specgram(data[:], Fs=sample_rate, NFFT=1024, noverlap=900)
    plot_spectrogram.set_xlabel('Time')
    plot_spectrogram.set_ylabel('Frequency')
    ax = plt.gca()
    ax.set_xlim([0, 5])

    fig.tight_layout()
    plt.savefig('{}.png'.format(wave_file))
    plt.close()


def enhance_media(input, output, params, headers):
    # Set Enhance API URL
    url = "https://api.dolby.com/media/enhance"
    body = {
        "input": input,
        "output": output
    }

    body.update(params)
    response = requests.request("POST", url, json=body, headers=headers)

    print('{} processed to: {}'.format(input, output))
    print(response.text)
    return output


def enhance_download_analyze(input_file, output_filename, output_file_base, output_local_file_base, enhance_params,
                             headers, title=None):
    output_cloud_storage = '{}/{}'.format(output_file_base, output_filename)
    output_local = '{}/{}'.format(output_local_file_base, output_filename)

    # Enhance
    enhance_media(input_file, output_cloud_storage, enhance_params, headers)

    # Download produced file to your local machine
    time.sleep(10)
    downloaded_file = download_file(output_cloud_storage, headers, output_local)
    print('Downloaded file: {}'.format(downloaded_file))
    # utils.plot_a_waveform(downloaded_file)
    wav_file = convert_mp4_to_wav(downloaded_file)
    plot_a_waveform_and_spectrum(wav_file, title)
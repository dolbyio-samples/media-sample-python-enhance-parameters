from config import *
import utils

# Part 3: "Audio SPEECH" parameter
print('\n\n\nEnhancing Part 3 - "Audio SPEECH" parameter\n')

# It doesn't need so much noise reduction
output_after_step_2 = 'NOISE_high.mp4'  # TODO: set to choosen signal's path
best_after_step_2 = '{}/{}'.format(output_file_base, output_after_step_2)

# OPTION 1 - speech: sibilance
output_speech_sibilance = 'SPEECH_sibilance.mp4'
param_speech_sibilance = {"audio": {
    "speech": {
        "sibilance": {"reduction": {
            "enable": True,
            "amount": "high"}
        }}}}

utils.enhance_download_analyze(best_after_step_2,
                               output_speech_sibilance,
                               output_file_base,
                               output_local_file_base,
                               param_speech_sibilance,
                               headers,
                               output_speech_sibilance)

# OPTION 2 - speech: plosive
output_speech_plosive = 'SPEECH_plosive.mp4'
param_speech_plosive = {"audio": {
    "speech": {
        "plosive": {"reduction": {
            "enable": True,
            "amount": "high"}
        }}}}

utils.enhance_download_analyze(best_after_step_2,
                               output_speech_plosive,
                               output_file_base,
                               output_local_file_base,
                               param_speech_plosive,
                               headers,
                               output_speech_plosive)

# OPTION 3 - speech: click
output_speech_click = 'SPEECH_click.mp4'
param_speech_click = {"audio": {
    "speech": {
        "click": {"reduction": {
            "enable": True,
            "amount": "high"}
        }}}}

utils.enhance_download_analyze(best_after_step_2,
                               output_speech_click,
                               output_file_base,
                               output_local_file_base,
                               param_speech_click,
                               headers,
                               output_speech_click)

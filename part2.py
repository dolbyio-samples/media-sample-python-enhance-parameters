from config import *
import utils

# Part 2: "Audio NOISE" parameter
print('\n\n\nEnhancing Part 2 - "Audio NOISE" parameter\n')

# Set this variable to chosen file from Part 1
output_after_step_1 = 'CONTENT_conference.mp4'  # TODO: set to choosen signal's path
best_after_step_1 = '{}/{}'.format(output_file_base, output_after_step_1)

# OPTION 1 - amount: low
output_noise_low = 'NOISE_low.mp4'
param_noise_low = {"audio": {"noise": {"reduction": {
    "enable": True,
    "amount": "low"
}
}
}}

utils.enhance_download_analyze(best_after_step_1,
                               output_noise_low,
                               output_file_base,
                               output_local_file_base,
                               param_noise_low,
                               headers,
                               output_noise_low)

# OPTION 2 - amount: high
output_noise_high = 'NOISE_high.mp4'
param_noise_high = {"audio": {
    "noise": {"reduction": {
        "enable": True,
        "amount": "high"
    }
    }
}}

utils.enhance_download_analyze(best_after_step_1,
                               output_noise_high,
                               output_file_base,
                               output_local_file_base,
                               param_noise_high,
                               headers,
                               output_noise_high)

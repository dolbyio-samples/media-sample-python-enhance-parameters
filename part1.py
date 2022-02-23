from config import *
import utils

# Upload local input file which we want to enhance
initial_input_file = utils.upload_input_file(input_file_local, input_file_base, headers)

# Part 1: "Content" parameter
print('\n\n\nEnhancing Part 1 - "Content" parameter\n')

# OPTION 1 - "conference"
output_content_conference = 'CONTENT_conference.mp4'
param_content_conference = {"content": {"type": "conference"}}

utils.enhance_download_analyze(initial_input_file,
                               output_content_conference,
                               output_file_base,
                               output_local_file_base,
                               param_content_conference,
                               headers,
                               output_content_conference)

# OPTION 2 - "meeting"
output_content_meeting = 'CONTENT_meeting.mp4'
param_content_meeting = {"content": {"type": "meeting"}}
utils.enhance_download_analyze(initial_input_file,
                               output_content_meeting,
                               output_file_base,
                               output_local_file_base,
                               param_content_meeting,
                               headers,
                               output_content_meeting)
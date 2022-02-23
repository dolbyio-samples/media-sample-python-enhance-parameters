# Set or these values to match your credentials on DolbyIO Developer account (Media API)
api_key = '<DOLBYIO_API_KEY>'

headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Set these values to have control over locations of your processed files
input_local_file_base = './INPUT'
input_file_local = '{}/seashells.wav'.format(input_local_file_base)
input_file_base = 'dlb://in/klesn_in'
output_file_base = "dlb://out/klesn_out"
output_local_file_base = "./OUTPUT"

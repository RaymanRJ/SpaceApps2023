def handler(event, context):
    # Get the body of the request
    body = json.loads(event['body'])

    # Get the numpy array from the body
    numpy_array = np.array(body['numpy_array'])

    # Convert the numpy array to a MIDI file
    midi_file = midi.numpy_to_midi(numpy_array)

    # Return the MIDI file as a base64 string
    return {
        'statusCode': 200,
        'body': json.dumps({
            'midi_file': midi_file
        })
    }
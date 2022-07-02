import json

def tern_status():
    """
    Read the tern_fig json file. Parse. Return a dictionary of status messages

    Returns:
        Dictionary of status messages
    """
    # TODO: this is ugly
    json_file = 'tern_fig.json'

    with open(json_file) as jf:
        data = json.load(jf)

        try:
            status = data["tern_status"]
        except:
            status = {"Error" : "Could not load status"}

    return status
import json

def tern_pass():
    """
    Returns the daily password from the json file. Also updates the daily password

    Returns:
        passwd
    """

    # TODO: this is ugly
    json_file = 'tern_fig.json'

    with open(json_file) as jf:
        data = json.load(jf)

        try:
            passwd = data["tern_pass"]
        except:
            passwd = "Error: Could not load password"

    return passwd


import click
import requests
import json
import os
import colored


@click.command()
def list():
    """
    Retrieves JSON object from vectordash using secret user token and displays the list of machines that the
    user is currently renting.

    """
    try:
        filename = "./vectordash_config/token.txt"
        if os.path.isfile(filename):
            with open(filename) as f:
                token = f.readline()
                full_url = "https://84119199.ngrok.io/api/list_machines/" + token

            try:
                r = requests.get(full_url)

                if r.status_code == 200:
                    data = r.json()

                    if len(data) > 0:
                        print("Your Vectordash machines:")
                        for key, value in data.items():
                            id = colored.stylize("[" + str(key) + "]", colored.fg("green"))
                            machine = id + value['name']
                            print(machine)
                    else:
                        print("You are not currently renting any machine. Go to https://vectordash.com to browse GPUs.")
                else:
                    print("Could not connect to vectordash API with provided token")

            except json.decoder.JSONDecodeError:
                print("Invalid token value. Please make sure you are using the most recently generated token.")

        else:
            print("Please make sure a valid token is stored. Run 'vectordash secret <token>'")

    except TypeError:
        print("Please make sure a valid token is stored. Run 'vectordash secret <token>'")

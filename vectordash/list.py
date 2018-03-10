import click
import requests
import json
import os

@click.command(name="list")
# @click.option('--token', help='Secret token to view your current machines.')


def list_machines():
    """Retrieves JSON object from vectordash using secret user token and displays the list."""
    try:
        filename = "./vectordash_config/secret_token.txt"
        if os.path.isfile(filename):
            with open(filename) as f:
                secret_token = f.readline()
                # print(secret_token)
                full_url = "https://84119199.ngrok.io/api/list_machines/" + secret_token
                # print(full_url)
                try:
                    r = requests.get(full_url)

                    if r.status_code == 200:
                        data = r.json()

                        for key, value in data.items():
                            machine = "[" + key + "]: " + value['name']
                            print(machine)
                    else:
                        print("Could not connect to vectordash API with provided token")

                except json.decoder.JSONDecodeError:
                    print("Invalid token value. Please make sure you are using the most recently generated token.")

        else:
            print("Please make sure a valid token is stored. Run vectordash secret <token>")

    except TypeError:
        print("Please make sure a valid token is stored. Run 'vectordash secret <token>'")



if __name__ == '__main__':
    list_machines()

import click
import requests
import json
import os

@click.command(name="list")
# @click.option('--token', help='Secret token to view your current machines.')


def list_machines():
    """Retrieves JSON object from vectordash using secret user token and displays the list."""
    try:
        if os.path.isfile('./secret_token'):
            with open('./secret_token') as f:
                secret_token = f.readline()
                # print(secret_token)
                full_url = "https://84119199.ngrok.io/api/list_machines/" + secret_token
                # print(full_url)
                try:
                    r = requests.get(full_url)
                    data = r.json()

                    for key, value in data.items():
                        machine = "[" + key + "]: " + value['name']
                        print(machine)
                except json.decoder.JSONDecodeError:
                    print("Invalid token value. Please make sure you are using the most recently generated token.")
        else:
            print("Please make sure a valid token is stored. Run vectordash secret <token>")
    except TypeError:
        print("Please make sure a valid token is stored. Run vectordash secret <token>")


if __name__ == '__main__':
    list_machines()

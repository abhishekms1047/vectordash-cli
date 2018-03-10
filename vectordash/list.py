import click
import requests
import json

@click.command(name="list")
@click.option('--token', help='Secret token to view your current machines.')


def list_machines(token):
    """Retrieves JSON object from vectordash using secret user token and displays the list."""
    try:
        full_url = "https://84119199.ngrok.io/api/list_machines/" + token

        try:
            r = requests.get(full_url)
            data = r.json()

            for key, value in data.items():
                machine = "[" + key + "]: " + value['name']
                print(machine)
        except json.decoder.JSONDecodeError:
            print("Invalid token value. Please make sure you are using the most recently generated token.")

    except TypeError:
        print("You must provide a valid token. Format: vectordash list --token XXXXXX...XXX")

if __name__ == '__main__':
    list_machines()

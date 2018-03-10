import click
import requests
import json
import os
import sys

@click.command(name="list")
@click.pass_context
# This dist function is needed for passing the context
def dist(ctx):
    ctx.invoke()


def ssh_into_machine(machine_id):
    """Retrieves JSON object from vectordash using secret user token and displays the list."""
    try:
        # retrieve the secret token from the config folder
        secret_token = "./vectordash_config/secret_token.txt"

        if os.path.isfile(secret_token):
            with open(secret_token) as f:
                secret_token = f.readline()

            try:
                # API endpoint for machine information
                full_url = "https://84119199.ngrok.io/api/list_machines/" + secret_token
                r = requests.get(full_url)

                # API connection is successful, retrieve the JSON object
                if r.status_code == 200:
                    data = r.json()

                    # machine_id provided is one this user has access to
                    if data.get(machine_id):
                        machine = (data.get(machine_id))
                        print("Machine exists. Connecting...")

                        # Machine pem
                        pem = machine['pem']

                        # name for pem key file, formatted to be stored
                        machine_name = (machine['name'].lower()).replace(" ", "")
                        key_file = "./vectordash_config/" + machine_name + "-key.pem"

                        # create new file ./vectordash_config/<key_file>.pem to write into and add the secret token
                        with open(key_file, "w") as h:
                            h.write(pem)

                        # give key file permissions for ssh
                        os.system("chmod 600 " + key_file)

                        # Port, IP address, and user information for ssh command
                        port = str(machine['port'])
                        ip = str(machine['ip'])
                        user = str(machine['user'])

                        # execute ssh command
                        ssh_command = "ssh " + user + "@" + ip + " -p " + port + " -i " + key_file
                        print(ssh_command)
                        os.system(ssh_command)

                    else:
                        print("Invalid machine id provided. Please make sure you are connecting to a valid machine")

                else:
                    print("Could not connect to vectordash API with provided token")

            except json.decoder.JSONDecodeError:
                print("Invalid token value. Please make sure you are using the most recently generated token.")

        else:
            # If token is not stored, the command will not execute
            print("Please make sure a valid token is stored. Run 'vectordash secret <token>'")

    except TypeError:
        print("There was a problem with ssh. Please ensure your command is of the format 'vectordash ssh <id>")



if __name__ == '__main__':
    # When valid command is given (i.e ONE token is provided)
    if len(sys.argv) == 2:

        # Retrieve secret token from command and store it
        machine_id = sys.argv[1]
        ssh_into_machine(machine_id)
    else:
        print("Invalid command. Please enter a token value: vectordash secret <token>")

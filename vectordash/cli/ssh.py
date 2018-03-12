import click
import requests
import json
import os


@click.command()
@click.argument('machine', required=True, nargs=1)
def ssh(machine):
    """
    Runs an ssh command to the machine with ID = @machine to allow user to connect.

    """
    try:
        # retrieve the secret token from the config folder
        token = "./vectordash_config/token.txt"

        if os.path.isfile(token):
            with open(token) as f:
                token = f.readline()

            try:
                # API endpoint for machine information
                full_url = "https://84119199.ngrok.io/api/list_machines/" + token
                r = requests.get(full_url)

                # API connection is successful, retrieve the JSON object
                if r.status_code == 200:
                    data = r.json()

                    # machine provided is one this user has access to
                    if data.get(machine):
                        machine = (data.get(machine))
                        print("Machine exists. Connecting...")

                        # Machine pem
                        pem = machine['pem']

                        # name for pem key file, formatted to be stored
                        machine_name = (machine['name'].lower()).replace(" ", "")
                        key_file = "./vectordash_config/" + machine_name + "-key.pem"

                        # create new file ./vectordash_config/<key_file>.pem to write into
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


# Run command line command vectordash ssh <machine>
# if __name__ == '__main__':
#     # When valid command is given (i.e ONE machine ID is provided)
#     if len(sys.argv) == 2:
#
#         # Retrieve machine from command and store it
#         machine = sys.argv[1]
#         ssh(machine)
#     else:
#         print("Incorrect number of arguments provided. Command should be of format 'vectordash ssh <machine>'")

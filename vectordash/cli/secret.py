import click
import sys
import os


@click.command()
@click.argument('token', required=True, nargs=1)
def secret(token):
    """
    Stores the user's secret token.

    """
    try:
        filename = "./vectordash_config/token.txt"
        # if a previous token was stored, update it
        if os.path.isdir("./vectordash_config") and os.path.isfile(filename):

            # retrieve previous token (this may be unnecessary)
            with open(filename) as f:
                lines = f.readlines()

            # change to user's new provided token
            lines[0] = token

            # update file with new token
            with open(filename, "w") as g:
                g.writelines(lines)

            print("Secret token changed and stored.")

        else:
            if not os.path.isdir("./vectordash_config"):
                os.system("mkdir ./vectordash_config")

                print("Made directory ./vectordash_config")

            # create new file ./token to write into and add the secret token
            with open(filename, "w") as h:
                h.write(token)

            print("Secret token created and stored.")

    except TypeError:
        print("Please make sure you are using the most recently generated token.")

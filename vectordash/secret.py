import click
import sys
import os


@click.command(name="secret")
@click.pass_context
# This dist function is needed for passing the context
def dist(ctx):
    ctx.invoke()

# Stores the secret token locally in ./secret_token
def store_secret(secret_token):
    """Stores the user's secret token."""
    try:
        # if a previous token was stored, update it
        if os.path.isfile("./secret_token"):

            # retrieve previous token (this may be unnecessary)
            with open("./secret_token") as f:
                lines = f.readlines()

            # change to user's new provided token
            lines[0] = secret_token

            # update file with new token
            with open("./secret_token", "w") as g:
                g.writelines(lines)

            print("Secret token changed and stored.")

        else:
            # create new file ./secret_token to write into and add the secret token
            with open("./secret_token", "w+") as h:
                h.write(secret_token)

            print("Secret token created and stored.")

    except TypeError:
        print("Please make sure you are using the most recently generated token.")

# Run command line command vectordash secret <token>
if __name__ == '__main__':
    try:
        # When valid command is given (i.e ONE token is provided)
        if len(sys.argv) == 2:

            # Retrieve secret token from command and store it
            secret_token = sys.argv[1]
            store_secret(secret_token)
        else:
            print("Invalid command. Please enter a token value: vectordash secret <token>")
    except TypeError:
        print("Invalid command. Please enter a token value: vectordash secret <token>")
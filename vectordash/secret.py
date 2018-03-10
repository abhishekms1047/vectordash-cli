import click
import sys
import os


@click.command(name="secret")
@click.pass_context
def dist(ctx, count):
    ctx.forward(test)
    ctx.invoke(test, count=42)
# @click.option('--token', help='Secret token to view your current machines.')


def store_secret(secret_token):
    """Stores the user's secret token."""
    try:
        if os.path.isfile("./secret_token"):
            print("Secret token being changed.")
            with open("./secret_token") as f:
                lines = f.readlines()

            lines[0] = secret_token
            with open("./secret_token", "w") as g:
                g.writelines(lines)

        else:
            print("Secret token being created.")
            with open("./secret_token", "w+") as h:
                h.write(secret_token)

    except TypeError:
        print("Please make sure you are using the most recently generated token.")

# Run command line command vectordash secret <token>
if __name__ == '__main__':
    try:
        # When valid command is given (i.e ONE token is provided)
        if len(sys.argv) == 2:

            # Retrieve secret token from command and store it
            secret_token = sys.argv[1]
            store_secret(secret_token + "\n")
        else:
            print("Invalid command. Please enter a token value: vectordash secret <token>")
    except TypeError:
        print("Invalid command. Please enter a token value: vectordash secret <token>")
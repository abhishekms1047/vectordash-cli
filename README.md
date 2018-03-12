# vectordash-cli
A command line tool for interacting with [Vectordash](http://vectordash.com) GPU instances.


#### Usage Examples

`vectordash secret <secret_token>` - update's the user's secret token which is used for authentication

`vectordash list` - lists the machines the user can connect to

`vectordash ssh <machine_id>` - connect the user to a machine via SSH

`vectordash push <machine_id> <from_path> <to_path>`

This uses scp to push files to the machine. If `<to_path>` is not included,
then let `scp` push it to the machine's home directory.

`vectordash pull <machine_id> <from_path> <to_path>`

Same command as above, except we're copying files from the machine to the local machine. If `<to_path>`
is not provided, then copy the files to the current directory.


#### Libraries
When you use requests, check `my_request.status == 200` after calling the API endpoint.

Use click for building the command line tool: http://click.pocoo.org/5/

#### We Are Launching on Sunday

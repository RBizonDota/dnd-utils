from dnd_utils import __app_name__
from dnd_utils.cli_client.client import CLIClient

def main():
    CLIClient().cmdloop()

if __name__ == "__main__":
    main()
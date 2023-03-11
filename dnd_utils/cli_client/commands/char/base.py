import cmd
from tabulate import tabulate

from dnd_utils import TextManager, Character
from dnd_utils.cli_client.commands.base import BaseCommand


class CharCommand(BaseCommand):    
    
    def _print_chars_table(self):
        char_attrs = [TextManager(ch).get_short_info() for ch in self._party]
        print(
            tabulate(
                char_attrs,
                headers=["Name", "Class", "Level", "Alignment"],
                tablefmt="orgtbl",
            ),
            f"\n\n Total: {len(self._party)} characters"
        )
    
    def do_ls(self, line: str):
        self._print_chars_table()
    
    def do_add(self, line: str):
        args = line.split()
        self._add_chars(*args)

    def _add_chars(self, *args):
        if not len(args):
            print("At least one path must be provided")
        chars = []
        try:
            for file_path in args:
                ch = Character.from_file(file_path)
                self.logger.debug(f"Got char {ch}")
                print(f"Character '{ch.name}' successfully imported")
                chars.append(ch)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        self._party.extend(chars)
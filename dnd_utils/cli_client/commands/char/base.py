import cmd
from builtins import all
from tabulate import tabulate

from dnd_utils import TextManager, Character
from dnd_utils.cli_client.commands.base import BaseCommand


class CharCommand(BaseCommand):
    def do_ls(self, line: str):
        char_attrs = [[i+1, *TextManager(ch).get_short_info()] for i,ch in enumerate(self._party)]
        print(
            tabulate(
                char_attrs,
                headers=["ID", "Name", "Class", "Level", "Alignment"],
                tablefmt="orgtbl",
            ),
            f"\n\n Total: {len(self._party)} characters"
        )
    
    def do_add(self, line: str):
        args = line.split()
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
    
    def do_rm(self, line: str):
        args = line.strip().split()
        if not (len(args)==1 and all([i.isdigit() for i in args])):
            print("Argument must be digit")
            return
        if int(args[0])>len(self._party):
            print("Argument must be valid char ID")
            return
        
        el_to_rm = self._party[int(args[0])]
        self._party.remove(el_to_rm)
        print(f"Character {el_to_rm.name} successfully removed")

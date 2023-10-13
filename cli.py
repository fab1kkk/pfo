import argparse

from pfo import PFO
from config import ALLOWED_MODES

def run_cli():
    parser = argparse.ArgumentParser(description="Python File Organizer - organize, manage & more.")
    parser.add_argument("mode", choices=ALLOWED_MODES, help="The mode to run")
    args = parser.parse_args()
    
    pfo = PFO()
    pfo.init_mode(args.mode)
    pfo.run()
"""
Michael Patel
November 2019

Initialize the 'NBA teams' package

The subpackages are the 2 NBA Conferences:
    - East
    - West

The sub-subpackages are the 6 NBA Divisions:
    - Atlantic
    - Central
    - Southeast
    - Northwest
    - Pacific
    - Southwest

"""
########################################################
# Imports

from os.path import dirname, basename, isfile, join
import glob


########################################################


modules = glob.glob("*/*.py", recursive=True)
print(modules)

__all__ = [basename(f) for f in modules if isfile(f)]
print(__all__)

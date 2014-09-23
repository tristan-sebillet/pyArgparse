import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nom_playlist")
parser.add_argument("temps")
args = parser.parse_args()

print(args.nom_playlist)
print"Votre playlist a pour duree: "+(args.temps)

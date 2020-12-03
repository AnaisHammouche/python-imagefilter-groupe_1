import sys

args = sys.argv

print(args)


if args[1] in ('-h', '---help'):
    print(f'{args[1]}')
else:
    print('Commande inconnu')

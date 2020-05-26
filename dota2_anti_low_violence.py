filename = 'dota 2 beta/game/dota/gameinfo.gi'
with open(filename, 'r') as fin:
    lines = fin.readlines()

with open(filename, 'w') as fout:
    for line in lines:
        if line.strip().startswith('Game_LowViolence'):
            fout.writelines('//' + line)
        else:
            fout.writelines(line)
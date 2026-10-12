import html

RAW_ASCII = """
0000000KK0000Okkd:,'....'',;;::cllodxxkkkkOOOkxxxkkkkkkkkkkkkkkkkkkkkkkkkkkkxxxx
kkkkkkkkkkkkkxdl:''',,''',,,;;::clllodxkkkkOOdc::::::::::;;;;;;;;;;;;;;;,,,,,,,,
''''''',,'''''....',,,,,;;::ccllloolloodxddxxl'.                                
'''''''''',''''',,,;;;;:::cclllolllllcccc::;;;,..................'''',,,,,,,,,,,
lllllllllllllcc::::ccccccllllllllcc;'........',;,,,,,,,,,,,,,,,,,;:::ccccccccccc
oooooooooollllc:;:clllllllllllllc:,... ......''',,,,;;,''''''''',;:ccccccc:ccccl
llllllllllllllc;,:cllllllllcc:::;'...   .  .....,,.',,''''''....',:ccccccccc::::
lllllllllclllcc::ccllllccc:;,,,,'.. .         ................',;:lllllllloloc';
llllllllllllllccccccc:::;,'...'''....            ...............':looooooooodc'l
ooooollllllllc:;;;;:;,'''.........                  .............';ccccccccll:'l
cclllccccllll:;,,'.'''.....   ............              ...........',,,'',,;:;'o
''''',,,,:cc:;;,''........       ..   ....   .. ...       ..  ..............''.l
......'..'''.'''.....                  ...   ........          ................l
:::::;;,..........                      ..................      .  .........'..l
ooddoc,'..........                       ....................      .........'''c
ooddo:............                  .................''',;,''......,,.. .......c
ooooc;............                   .............''',,;:::::;;;;::cc:,....';;.c
ooolc;....      .             .  .......'''''''',,;;::ccclllllccclllll:,.';:oc'c
ooool:...                    ........',,,,,,,,,,,,,,,,,,,;;clloooooddoc;,:loxl,l
oooooc'..                 ........',;;;;;;;;,,,,,,,''.......';clooooddoloddxxl,l
oollol;. .            ..........';:ccccccc::ccllcc:::;,,,,,,,,:loll:;',;ldddxo',
llllolc'.            ...........,clllllllllooolc:;,'.....,;:cccclc:,'...'lddxo'.
ooooool;..    ..,;;'...........':loooooooooolc;,'';'......,:clllc:,'.',::oxxkd,.
ooooooo:'.   .,ldxxdc,..'......,:loooooooollc::;;::;'.....';:cool;.....;okkkOd,.
ddddoooc'..  'clodxxdoc:c:'....;cooooooooooollllcc::;,'''',;:looddc'',,:dkkkOx,.
dddddddl,.. .;lcoxdllodooo;....;coddooooooooooooolcc:::;:ccllooodkOdlcldkkkkOd,.
ddddddddo:. .,cldolcclooooc'...,:lddddddddddddddddoollllooolloodxkO0OkkkkkkkOx,.
kkkkkxxxkkl'..coc:clccododo,...';lodddddxxxxxddddddddddddollodxkxxkkkkOOOkkOOx,.
000000OO0K0Oo':olclolccoddd:....,:loodddddxxxxxxdddddddddlcoxdc;;cooodxO0OOOOx;.
KKKKKKKKXXXNXklloloddolodddc'..'',;:clloooddxxxxxxxxdddoollll;...':l::d0KKKKX0c.
XXKKKXXXXXXXNN0doodxddooooo:....'',,;:cccllodddxxdddoollc::;'....''',lkKNNNNNXo.
XXKKKKKKKKKXXXXKo,;oxdxxool;.....',,,,;::ccclllooooolc;,'............;xKNNWNXKxc
XXK0OOOO0000KKKXKl';oxxxdoc,.....',,',,;;;;;;::cclll:'...''',,'''',...lKNXK00OkO
K00OkkkOO00000KXXKo;lxxddl;'.''..',,''',,,,'',;;:clc;'..'.''''''','...:0NKkxkkxx
0OOkkkkkO00000KXNNKxloxdo:'..'''''',,''''...''',:cc:;;;::;;;;::;;;;,.'dKNXK0OOdd
0OkkxkkOOOOO00KXXXX0xdddo:,....''',,'''.....'''';;:::ccllc::;,,,,,;c;cOXNXNNNKoo
K0OkkkkOOO0000KXKKK0Okdddl:'.....''''.'.....'''',;::cccccc:;'......;:o0NNNNNNKoo
K0OOkkOOOO00KKXXKKK0kdddol:,.....''........''''',;:::ccccc:;'.....,cxXNNNNNN0ll
0OOkkkOOOO00KKXXNXXKK0xdddol:;,'................'',,,,;;:::;,'....,:d0NNNNNXNNkc
0OOOOOOOO0KKKXXXNXXXX0xdddoolc:;'......................''',,'......'lKNNXNNXNNXK
0OOOO0000KKXXXXNNXXXX0xddddooolc:,''......'.........................:ONXXNNNNXNN
0OOOO00KKKXXNNNNNXKKK0xdddddoooolc:::;,,,,''........................;kXXXXXXXXXX
OOOO00000KXXNNNNNXXXX0xdddddddoooollccccc:;,,'.......... ... ... ..'l0XXXXXXXXXX
O000000000KKXXXXK00KKOdoddxxddoooooolllcccc:;;,'''.......':c;,;:;;lx0XXXNXXXXXXX
0KXXXKKKKKKKXXXXK0O00kdodddxxddddoooooolllc:;;;,''...'',;lxO00000KXXNXXXXXXXXNNX
KXNNNNNNNNNNNWWNNXXXKOdddddddddddddddooollc::;;;;,,,,,;;:ccoooxxlcdOKK0KXNNNNNNX
XXNNNNNNNNNNWWWWWNNNXkddddddddddddddddoolllcc::::;;;;::;:;:lcclc'...,,,,codxxxkO
XXNNNNXXXXNNNNNNXXXX0xddddddddddddoooooollllcccc:;;;;;;;;;;::;,................'
KXXXXXXXKXXNXXXXXK00kddddddddddddoooooollllllcccc::;;;,,,,'.....................
KXXXXKKKKXXNNNXOdodxdodxdddddddddooooooollllllcccc:;;,,'...    .................
KKKKKKKXNWNX0dc:ldxxddxxdddddddddooooooooooollccc:;,'...     ...................
KKKKKKKX0koc,',lxxxxxxxdxxdddddddoooooooooollc::;'...      .    ................
KKKK0koc,'''.'cddxxxxddxdddddddddoloolllllc:;,....              ................
0Oxl:;''''''..,:codxxxdddddddddddlllc::;,,....                   ...............
c;'',,,,,'......';codxdddddddoool:;,....                         ...............
""".strip().splitlines()

num_rows = len(RAW_ASCII)

# Tight dimensions matching the exact terminal frame
svg_width = 370
line_height = 8.8
font_size = 7.2
svg_height = int(num_rows * line_height + 8)

pad_x = 8
usable_width = svg_width - (pad_x * 2)

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">',
    '  <style>',
    f'    .term {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: {font_size}px; font-weight: 600; fill: #adbac7; }}',
    '  </style>',
    f'  <rect width="{svg_width}" height="{svg_height}" fill="#0d1117" rx="6" stroke="#30363d" stroke-width="1" />',
    '  <g class="term">'
]

duration = 1.6
step = duration / max(num_rows, 1)

for i, line in enumerate(RAW_ASCII):
    escaped = html.escape(line)
    y_pos = int(8 + (i * line_height))
    delay = i * step
    clip_id = f"c_{i}"

    svg.append(f'    <clipPath id="{clip_id}">')
    svg.append(f'      <rect x="{pad_x}" y="{y_pos - font_size}" width="0" height="{line_height + 1}">')
    svg.append(f'        <animate attributeName="width" from="0" to="{usable_width + 10}" dur="0.08s" begin="{delay:.2f}s" fill="freeze" />')
    svg.append('      </rect>')
    svg.append('    </clipPath>')
    svg.append(f'    <text x="{pad_x}" y="{y_pos}" textLength="{usable_width}" lengthAdjust="spacingAndGlyphs" clip-path="url(#{clip_id})">{escaped}</text>')

svg.append('  </g>')
svg.append('</svg>')

with open("om-ascii.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg))
print(f"[+] om-ascii.svg calibrated: flush to all borders ({svg_width}px x {svg_height}px)")

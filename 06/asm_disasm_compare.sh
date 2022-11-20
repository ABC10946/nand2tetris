#!/bin/bash
# this test script enable only non symbol

# remove assembled hack files
rm Add/Add.hack max/Max.hack max/MaxL.hack pong/Pong.hack pong/PongL.hack rect/Rect.hack rect/RectL.hack 2> /dev/null

# remove disassembled asm files
rm Add/Add.disas.asm max/Max.disas.asm max/MaxL.disas.asm pong/Pong.disas.asm pong/PongL.disas.asm rect/Rect.disas.asm rect/RectL.disas.asm 2> /dev/null

# ---- add ----
# assemble add
python3 assembler.py < add/Add.asm > add/Add.hack

# disassemble assembled add
python3 disassembler.py < add/Add.hack > add/Add.disas.asm

# compare original asm and disassembled asm
diff --strip-trailing-cr -Bbw -I '//.*' add/Add.asm add/Add.disas.asm


# ---- max ----
# assemble max
python3 assembler.py < max/MaxL.asm > max/MaxL.hack

# disassemble assembled max
python3 disassembler.py < max/MaxL.hack > max/MaxL.disas.asm

# compare original asm and disassembled asm
diff --strip-trailing-cr -Bbw -I '//.*' max/MaxL.asm max/MaxL.disas.asm


# ---- pong ----
# assemble PongL
python3 assembler.py < pong/PongL.asm > pong/PongL.hack

# disassmble assembled PongL
python3 disassembler.py < pong/PongL.hack > pong/PongL.disas.asm

# compare original asm and disassembled asm
diff --strip-trailing-cr -Bbw  -I '//.*' pong/PongL.asm pong/PongL.disas.asm


# ---- rect ----
python3 assembler.py < rect/rectL.asm > rect/rectL.hack

# disassmble assembled rectL
python3 disassembler.py < rect/rectL.hack > rect/rectL.disas.asm

# compare original asm and disassembled asm
diff --strip-trailing-cr -Bbw -I '//.*' rect/rectL.asm rect/rectL.disas.asm
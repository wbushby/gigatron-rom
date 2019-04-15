import asm

asm.defun('@globals')
asm.glob('ht')
asm.dw(0)
asm.glob('ha')
asm.dw(0)
asm.glob('pvpc')
asm.dw('vPC')
asm.glob('sp')
asm.dw(0x0700)
asm.glob('thunk0')
asm.dw('@thunk0')
asm.glob('thunk1')
asm.dw('@thunk1')
asm.glob('thunk2')
asm.dw('@thunk2')
asm.glob('enter')
asm.dw('@enter')
asm.glob('leave')
asm.dw('@leave')
asm.glob('ldloc')
asm.dw('@ldloc')
asm.glob('stloc')
asm.dw('@stloc')
asm.glob('pusha')
asm.dw(0)
asm.glob('lsh')
asm.dw(0)
asm.glob('rsh')
asm.dw(0)
asm.glob('mul')
asm.dw(0)
asm.glob('mod')
asm.dw(0)
asm.glob('div')
asm.dw(0)

# TODO: use static data for RT vars
asm.defun('@start')
asm.ldwi('_main')
asm.call('vAC')
asm.label('halt')
asm.ldwi('halt')
asm.jr()

asm.defun('@ldloc')
asm.addw('sp')
asm.deek()
asm.ret()

asm.defun('@stloc')
asm.addw('sp')
asm.stw('ht')
asm.ldw('ha')
asm.doke('ht')
asm.ret()

asm.defun('@thunk0')
asm.stw('ht')
asm.inc('vLRH')
asm.ldi(0)
asm.st('vLR')
asm.ldw('ht')
asm.ret()

asm.defun('@thunk1')
asm.stw('ht')
asm.inc('vLRH')
asm.ldi(0xa0)
asm.st('vLR')
asm.ldw('ht')
asm.ret()

asm.defun('@thunk2')
asm.stw('ht')
asm.ldwi(0x08a0)
asm.stw('vLR')
asm.ldw('ht')
asm.ret()

# vAC = bitmask of registers to save. The highest-order bit represents r15.
asm.defun('@enter')
asm.stw('ha')
asm.ldi('r1')
asm.stw('ht')
asm.ldw('ha')
asm.label('loop')
asm.jeq('done')
asm.jgt('next')
asm.ldw('sp')
asm.subi(2)
asm.stw('sp')
asm.ldw('ht')
asm.deek()
asm.doke('sp')
asm.label('next')
asm.inc('ht')
asm.ldw('ha')
asm.addw('ha')
asm.stw('ha')
asm.ldwi('loop')
asm.jr()
asm.label('done')
asm.ret()

# vAC = bitmask of registers to restore. The highest-order bit represents r1.
asm.defun('@leave')
asm.stw('ha')
asm.ldi('r15')
asm.stw('ht')
asm.ldw('ha')
asm.label('loop')
asm.jeq('done')
asm.jgt('next')
asm.ldw('sp')
asm.deek()
asm.doke('ht')
asm.ldw('sp')
asm.addi(2)
asm.stw('sp')
asm.label('next')
asm.ldw('ht')
asm.subi(1)
asm.stw('ht')
asm.ldw('ha')
asm.addw('ha')
asm.stw('ha')
asm.ldwi('loop')
asm.jr()
asm.label('done')
asm.ret()

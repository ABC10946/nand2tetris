// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
    // initialize answer register
    @0     // R2を0で初期化する
    D=A
    @2
    M=D

    @0     // R0が0であればENDにジャンプする
    D=M
    @END
    D;JEQ

(LOOP)
    @1     // R1が0であればENDにジャンプする
    D=M
    @END
    D;JEQ

    @1     // R1を1減らす
    M=M-1

    @0     // R2にR0を足し込む
    D=M
    @2
    M=M+D

    @LOOP  // LOOPにジャンプする
    0;JMP
(END)
    @END
    0;JMP
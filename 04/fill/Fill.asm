// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// test ***
// max 24543 = SCREEN + 254 * 32 + 496/16
//     @24543
//     M=-1
// 
//     @END
//     0;JMP
// test ***

// (SCREEN_WRITE) // SCREEN_CLEARの全体版は同様のコードでSCREEN RAMに0を書き込むようにして実装する
// MAIN ROUTINE
//     @254
//     D=A
//     @height
//     M=D
// (SCREEN_VERTICAL_LOOP)
//     @height
//     D=M
//     @END
//     D;JEQ
// 
//     @31  // 512 / 16
//     D=A
//     @width
//     M=D
// 
//     (SCREEN_HORIZONTAL_LOOP)
//         @width
//         D=M
//         @SCREEN_VERTICAL_LOOP
//         D;JEQ
// 
//         // compute screen ram
//         // screenram = SCREEN + widthslide + heightslide * 32
// 
//         // heightslide * 32
//         @32 // r0 = 32
//         D=A
//         @0
//         M=D
// 
//         @height // r1 = heightslide
//         D=M
//         @1
//         M=D
// 
//         @MULT // r0 * r1 = r2
//         0;JMP
//         (RETBASE)
// 
//         @SCREEN
//         D=A
//         @width
//         D=D+M
//         @2
//         A=D+M
//         M=-1
// 
//         // @32
//         // D=A
//         // @SCREEN
//         // A=A+D   // SCREEN + 32
//         // M=-1   // SCREEN
//         
//         @width
//         M=M-1
// 
//         @SCREEN_HORIZONTAL_LOOP
//         0;JMP
// 
// 
//     @height
//     M=M-1
// 
//     @SCREEN_VERTICAL_LOOP
//     0;JMP
// 
// 
// (END)
//     @END
//     0;JMP
// 
// 
// // MULT SUBROUTINE
// (MULT)
//     @0
//     D=A
//     @2
//     M=D
// (LOOP)
//     @0
//     D=M
//     @RET
//     D;JEQ
// 
//     @1
//     D=M
//     @RET
//     D;JEQ
// 
//     @1
//     M=M-1
//     @0
//     D=M
//     @2
//     M=M+D
//     @LOOP
//     0;JMP
// (RET)
//     @RETBASE
//     0;JMP


// MAIN ROUTINE // 全体書き込みを行うと時間がかかるため一部の表示だけで実装
(EVENT_GET)
    @24576
    D=M
    @SCREEN_WRITE
    D;JNE
    @SCREEN_CLEAR
    D;JEQ

(SCREEN_WRITE)
    @SCREEN
    M=-1
    @EVENT_GET
    0;JMP

(SCREEN_CLEAR)
    @SCREEN
    M=0
    @EVENT_GET
    0;JMP

(END)
    @END
    0;JMP
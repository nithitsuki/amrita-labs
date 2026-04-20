.global _start

_start:
    mov r1, #0
    mov r2, #0 //initialize r2 too
    b loop

loop:
    add r2, r2, #10 // R2 = R2 + 10

    add r1, r1, #1 //r1++
    cmp r1, #7 
    beq exit // if(r1 == 7) {goto exit;}
    b loop // else { goto loop;}
    
exit:
    mov r0, #0
    mv r7, #1
    svc #0

@ print star triangle
.global _start

.text
_start:
    mov r5, #1              @ current row
    mov r6, #5              @ number of rows

row_loop:
    cmp r5, r6
    bgt end

    mov r4, #0              @ stars printed in this row

star_loop:
    cmp r4, r5
    bge print_newline

    mov r0, #1              @ stdout
    ldr r1, =asterisk       @ message address
    mov r2, #1              @ message length
    mov r7, #4              @ sys_write
    swi #0

    add r4, r4, #1
    b star_loop

print_newline:
    mov r0, #1              @ stdout
    ldr r1, =newline        @ newline address
    mov r2, #1              @ message length
    mov r7, #4              @ sys_write
    swi #0

    add r5, r5, #1
    b row_loop

end:
    mov r0, #0
    mov r7, #1              @ sys_exit
    swi #0

.data
asterisk:
    .ascii "*"
newline:
    .ascii "\n"

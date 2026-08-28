@ find ones complement of r1
.global _start

.text
_start:
    mov r1, #00000
    mvn r1, r1              @ find ones complement
    mov r7, #1              @ sys_exit
    swi #0

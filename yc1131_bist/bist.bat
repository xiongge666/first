e p
e p 
e p 

e p
e p 
e p 

e pr
e pr
e pr
e pr

rem write romcrc
rem 3122AA   e f8558 7505
rem 3122AB   e f8558 2881
rem 1131TA   e f8558 8d43
rem 1131AA   e f8558 e890
e f8558 e890
e f8558l4

rem cpuclk
rem e f8410 000008

rem ahb
rem e f8414 11010000

rem open dac clk
rem e f841c 50505858
rem e f840e df
rem dac ctrl.bit1 =1
e fb900 02

rem open rsa clk
e f840d 74

rem open rv clk
e d0100 0a
e d0101 0a
e e0000 bc
e e0001 ff
e e0000l

rem open qspi3(bit19)
e f840e 08

rem open rgb clk(bit30)
e f840f 81

rem dvdd
rem call lpm.bat
rem e fa801 d0

e d0eed 00

rem ramdisdis 1131TA:d0040 1131AA:d0080
e d0080 0

rem ocpsel
rem e fa800 41


rem bist test
e f853d 0
e f8518l8
timeout 1
e f853d 5
timeout 1 
e f853d 7
timeout 1

rem read bist result
e f8518l8

rem get bist result (1131TA:d0050 1131AA:d0090)
e a
e d0090l30 
REM e f853d 00


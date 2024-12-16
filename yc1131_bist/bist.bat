e p

rem write romcrc
rem 3122AA   e f8558 7505
rem 3122AB   e f8558 2881
rem 1131TA   e f8558 8d43
rem 1131AA   e f8558 e890
e f8558 e890

rem cpuclk
e f8410 000008
rem ahb
e f8414 11010000
rem open dac clk
e f841c 50505858
e f840e df
rem dac ctrl.bit1 =1
e fb900 02

rem open rsa clk
e f840d 74

rem open rv clk
e d0100 0a
e d0101 0a
e e0000 bc
e e0001 ff

rem open qspi3(bit19)
e f840e 08

rem open rgb clk(bit30)
e f840f 81

rem dvdd
rem call lpm.bat
e fa801 d0

e d0eed 00

rem ramdisdis 1131TA:d0040 1131AA:d0080
e d0080 0

rem ocpsel
e fa800 41


rem bist test
e f853d 1
e f853d 5
delay 5 us
e f853d 7
rem 41.6M 10ms -- >192M  2.2ms
rem timeout 1
delay 5ms

rem read bist result
e f8518l8
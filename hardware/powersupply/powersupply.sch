EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:SDRsymbols
LIBS:powersupply-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "2016-10-10"
Rev "r0"
Comp "FHNW | Technik"
Comment1 "Francesco Rovelli"
Comment2 "Noah Hüsser"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L BNC P2
U 1 1 57FB6F69
P 8750 4350
F 0 "P2" H 8760 4470 50  0000 C CNN
F 1 "OUT" V 8860 4290 50  0000 C CNN
F 2 "SDRfootprints:1-1337543-0" H 8750 4350 50  0001 C CNN
F 3 "" H 8750 4350 50  0000 C CNN
	1    8750 4350
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X02 P?
U 1 1 5813B800
P 4225 4350
F 0 "P?" H 4225 4500 50  0000 C CNN
F 1 "CONN_01X02" V 4325 4350 50  0000 C CNN
F 2 "" H 4225 4350 50  0000 C CNN
F 3 "" H 4225 4350 50  0000 C CNN
	1    4225 4350
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR?
U 1 1 5813B8D5
P 4500 4450
F 0 "#PWR?" H 4500 4200 50  0001 C CNN
F 1 "GND" H 4500 4300 50  0000 C CNN
F 2 "" H 4500 4450 50  0000 C CNN
F 3 "" H 4500 4450 50  0000 C CNN
	1    4500 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	4425 4400 4500 4400
Wire Wire Line
	4500 4400 4500 4450
$Comp
L +5V #PWR?
U 1 1 5813B95B
P 4500 4250
F 0 "#PWR?" H 4500 4100 50  0001 C CNN
F 1 "+5V" H 4500 4390 50  0000 C CNN
F 2 "" H 4500 4250 50  0000 C CNN
F 3 "" H 4500 4250 50  0000 C CNN
	1    4500 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4425 4300 4500 4300
Wire Wire Line
	4500 4300 4500 4250
$Comp
L GND #PWR?
U 1 1 5813BAA7
P 8750 4625
F 0 "#PWR?" H 8750 4375 50  0001 C CNN
F 1 "GND" H 8750 4475 50  0000 C CNN
F 2 "" H 8750 4625 50  0000 C CNN
F 3 "" H 8750 4625 50  0000 C CNN
	1    8750 4625
	1    0    0    -1  
$EndComp
Wire Wire Line
	8750 4550 8750 4625
$Comp
L +3.3V #PWR?
U 1 1 5813BAFA
P 8525 4275
F 0 "#PWR?" H 8525 4125 50  0001 C CNN
F 1 "+3.3V" H 8525 4415 50  0000 C CNN
F 2 "" H 8525 4275 50  0000 C CNN
F 3 "" H 8525 4275 50  0000 C CNN
	1    8525 4275
	1    0    0    -1  
$EndComp
Wire Wire Line
	8525 4275 8525 4350
Wire Wire Line
	8525 4350 8600 4350
$Comp
L LP38798 IC?
U 1 1 5813BBBD
P 6450 4675
F 0 "IC?" H 6700 4675 60  0000 C CNN
F 1 "LP38798" H 6300 5475 60  0000 C CNN
F 2 "" H 6450 4675 60  0001 C CNN
F 3 "" H 6450 4675 60  0001 C CNN
	1    6450 4675
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 4225 5850 4225
Wire Wire Line
	5750 3925 5750 4025
Wire Wire Line
	5750 4025 5750 4125
Wire Wire Line
	5750 4125 5750 4225
Wire Wire Line
	5750 4225 5750 4425
Wire Wire Line
	5750 4025 5850 4025
Wire Wire Line
	5850 4125 5750 4125
Connection ~ 5750 4125
Wire Wire Line
	5750 4425 5850 4425
Connection ~ 5750 4225
Wire Wire Line
	7100 4225 7000 4225
Wire Wire Line
	7100 4025 7000 4025
Wire Wire Line
	7100 4125 7000 4125
Wire Wire Line
	7100 3925 7100 4025
Wire Wire Line
	7100 4025 7100 4125
Wire Wire Line
	7100 4125 7100 4225
Connection ~ 7100 4125
$Comp
L GND #PWR?
U 1 1 5813BD8A
P 5750 4775
F 0 "#PWR?" H 5750 4525 50  0001 C CNN
F 1 "GND" H 5750 4625 50  0000 C CNN
F 2 "" H 5750 4775 50  0000 C CNN
F 3 "" H 5750 4775 50  0000 C CNN
	1    5750 4775
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 4525 5750 4725
Wire Wire Line
	5750 4725 5750 4775
Wire Wire Line
	5425 4725 5750 4725
Wire Wire Line
	5750 4725 6450 4725
Wire Wire Line
	6450 4725 7100 4725
Wire Wire Line
	7100 4725 7325 4725
Wire Wire Line
	6450 4725 6450 4675
Wire Wire Line
	5850 4525 5750 4525
Connection ~ 5750 4725
Wire Wire Line
	7100 4725 7100 4525
Wire Wire Line
	7100 4525 7000 4525
Connection ~ 6450 4725
$Comp
L +5V #PWR?
U 1 1 5813BE56
P 5750 3925
F 0 "#PWR?" H 5750 3775 50  0001 C CNN
F 1 "+5V" H 5750 4065 50  0000 C CNN
F 2 "" H 5750 3925 50  0000 C CNN
F 3 "" H 5750 3925 50  0000 C CNN
	1    5750 3925
	1    0    0    -1  
$EndComp
Connection ~ 5750 4025
$Comp
L +3.3V #PWR?
U 1 1 5813BE91
P 7100 3925
F 0 "#PWR?" H 7100 3775 50  0001 C CNN
F 1 "+3.3V" H 7100 4065 50  0000 C CNN
F 2 "" H 7100 3925 50  0000 C CNN
F 3 "" H 7100 3925 50  0000 C CNN
	1    7100 3925
	1    0    0    -1  
$EndComp
Connection ~ 7100 4025
$Comp
L C_Small C?
U 1 1 5813BF88
P 5425 4500
F 0 "C?" H 5435 4570 50  0000 L CNN
F 1 "10n" H 5435 4420 50  0000 L CNN
F 2 "" H 5425 4500 50  0000 C CNN
F 3 "" H 5425 4500 50  0000 C CNN
	1    5425 4500
	1    0    0    -1  
$EndComp
$Comp
L C_Small C?
U 1 1 5813BFBF
P 7775 4425
F 0 "C?" H 7785 4495 50  0000 L CNN
F 1 "10u" H 7785 4345 50  0000 L CNN
F 2 "" H 7775 4425 50  0000 C CNN
F 3 "" H 7775 4425 50  0000 C CNN
	1    7775 4425
	1    0    0    -1  
$EndComp
Wire Wire Line
	5850 4325 5425 4325
Wire Wire Line
	5425 4325 5425 4400
Wire Wire Line
	5425 4600 5425 4725
Wire Wire Line
	7775 4175 7775 4325
$Comp
L GND #PWR?
U 1 1 5813C081
P 7775 4600
F 0 "#PWR?" H 7775 4350 50  0001 C CNN
F 1 "GND" H 7775 4450 50  0000 C CNN
F 2 "" H 7775 4600 50  0000 C CNN
F 3 "" H 7775 4600 50  0000 C CNN
	1    7775 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	7775 4600 7775 4525
$Comp
L R_Small R?
U 1 1 5813C0D0
P 7175 4325
F 0 "R?" H 7205 4345 50  0000 L CNN
F 1 "23k2" H 7205 4285 50  0000 L CNN
F 2 "" H 7175 4325 50  0000 C CNN
F 3 "" H 7175 4325 50  0000 C CNN
	1    7175 4325
	0    1    1    0   
$EndComp
$Comp
L R_Small R?
U 1 1 5813C120
P 7325 4600
F 0 "R?" H 7355 4620 50  0000 L CNN
F 1 "13k3" H 7355 4560 50  0000 L CNN
F 2 "" H 7325 4600 50  0000 C CNN
F 3 "" H 7325 4600 50  0000 C CNN
	1    7325 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 4325 7075 4325
Wire Wire Line
	7000 4425 7325 4425
Wire Wire Line
	7325 4325 7325 4425
Wire Wire Line
	7325 4425 7325 4500
Wire Wire Line
	7325 4325 7275 4325
Connection ~ 7325 4425
Wire Wire Line
	7325 4725 7325 4700
Connection ~ 7100 4725
$Comp
L C_Small C?
U 1 1 5813C31B
P 5025 4425
F 0 "C?" H 5035 4495 50  0000 L CNN
F 1 "10u" H 5035 4345 50  0000 L CNN
F 2 "" H 5025 4425 50  0000 C CNN
F 3 "" H 5025 4425 50  0000 C CNN
	1    5025 4425
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 5813C321
P 5025 4175
F 0 "#PWR?" H 5025 4025 50  0001 C CNN
F 1 "+5V" H 5025 4315 50  0000 C CNN
F 2 "" H 5025 4175 50  0000 C CNN
F 3 "" H 5025 4175 50  0000 C CNN
	1    5025 4175
	1    0    0    -1  
$EndComp
Wire Wire Line
	5025 4325 5025 4175
$Comp
L GND #PWR?
U 1 1 5813C328
P 5025 4650
F 0 "#PWR?" H 5025 4400 50  0001 C CNN
F 1 "GND" H 5025 4500 50  0000 C CNN
F 2 "" H 5025 4650 50  0000 C CNN
F 3 "" H 5025 4650 50  0000 C CNN
	1    5025 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	5025 4650 5025 4525
$Comp
L +3.3V #PWR?
U 1 1 5813C342
P 7775 4175
F 0 "#PWR?" H 7775 4025 50  0001 C CNN
F 1 "+3.3V" H 7775 4315 50  0000 C CNN
F 2 "" H 7775 4175 50  0000 C CNN
F 3 "" H 7775 4175 50  0000 C CNN
	1    7775 4175
	1    0    0    -1  
$EndComp
$EndSCHEMATC

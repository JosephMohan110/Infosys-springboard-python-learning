#    BITWISE OPERATERS...   &,|,^,~,<<,>>

#Bitwise operators work on numbers at the binary level (0s and 1s).
# these work on bites..binary ..


#    & (AND) operater...
a=5        
b=4
print(a&b)  # "&" it for bitwise operater (and)..  "a" and "b want to convert into binary.. this binary want to convert into decimal ...decimal will be output..
               #  a= 0101..... b= 0100 and bitwise "and" operation will done.. binary and operation will done(0100) then it converted in to decimal..4
               # if both are 1 then 1.. otherwise 0...
               #
               #   1    1 = 1
               #   1    0 = 0
               #   0    0 = 0


#   | (OR) operater

a=5
b=9
print(a|b)         # it will converted into binary then it converted it into decimal...


     # if any of them are one the out will one..
     #  1    1  = 1
     #  1    0  = 1
     #  0    1  = 1
     #  0    0  = 0



#    ^ (XOR) BITWISE OPERATION

A=2
B=4
print(A^B)    # it will converted into xor binary then it converted into decimal


     # if both bit is same then out is 0..if both are different then one..

     #  1    1  = 0
     #  1    0  = 1
     #  0    0  = 0




#   ~  (NEGITION... NOT)(COMPLEMENT) BITWISE OPERATION
       
       #    1   =   0
       #    0   =   1

a= 5
b=4
print(~a)   # binary of a mean 5.. its binary is '0101'  it negation or reverse is "1010" and 1010 is "-6" -6 is stored as by taking 2's complenent
            # 2's(2's complement)= 1's+1..
            # so, 1's complenent 
            # for storeing -6 we take 6 ..6 binary is "0110" and 6's 1 complement is, reverse the the bite,1001.. for 2's complenent add "1" with "1oo1"
            #  1001  +  (binary addition)
            #     1
            #--------
            #  1010...
            # now 2's complenent of 6's is 1010... and 1010 is nedition of 5 ...1010 is converted into into binary...we get -6

            # if we want to find a negition of a number we we can use equation = -(n+1)....n = input number




#     LEFT SHEFT <<   .....


A=5
print(A<<1)
print(A<<2)   # instread of 2 we can wrote any number..and it move to left side as our input..
              # binary of 5 is "0101" and '01' will move to leftside 2 bit.. for that we will add 2 zero(00) in rightside "010100"..we will not discard the values
              #   1011 leftbit 2 then 101100
              #   0011 leftbit 3 then 0011000 if more zero came infront we can discard 0,  1 cant discard..
              #   00000101  leftbit 2, then 0000010100 it can also write as 00010100
              #  after leftbit binary will converted into decimal...
              # LEFT BIT WE WILLL GAIN BIT



  #    RIGHT SHIFT >>  ...

a=5
print(a>>2)
print(a>>3)   # if right shift is 2 bit then rightside bit will move 2 bit to right..
              # 5 binary is 0101 last(2 bit) 01 will move to wright side.. and 2 zero will add in left side ..
              # 5 is, 0101 rightshift(2) 0001..01 ,and after rightshift binary is "0001" and output will 1..
              # IN  RIGHT SHIFE WE WILL DISCARD OR LOSS THE BIT.
              # AND IF IT 3  then 5 binary = 0101...rightshift..= "0000"...101...,,0000 is out put it is converted into decimal

            





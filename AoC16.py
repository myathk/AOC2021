with open('AoC16input.txt') as f:
    line = f.readline()

def hex_to_binary(hex):
    binary = ''

    for each in hex:
        if each == '0':
            binary+= '0000'
        elif each == '1':
            binary += '0001'
        elif each == '2':
            binary += '0010'
        elif each == '3':
            binary += '0011'
        elif each == '4':
            binary += '0100'
        elif each == '5':
            binary += '0101'
        elif each == '6':
            binary += '0110'
        elif each == '7':
            binary += '0111'
        elif each == '8':
            binary += '1000'
        elif each == '9':
            binary += '1001'
        elif each == 'A':
            binary += '1010'
        elif each == 'B':
            binary += '1011'
        elif each == 'C':
            binary += '1100'
        elif each == 'D':
            binary += '1101'
        elif each == 'E':
            binary += '1110'
        else: 
            binary += '1111'

    return binary




hex_str = "9C0141080250320F1802104A08"
binary =  hex_to_binary(hex_str)
pointer = 0
versions = 0
stack = []


def decipher_binary(stack):
    global versions
    global pointer

    ver = ''
    IDtype = ''
    ptr_copy = pointer

    if ptr_copy == len(binary):
        return stack

    for i in range(ptr_copy, ptr_copy + 3):
        ver += binary[i]

    ptr_copy += 3
    ver = int(ver, 2)

    for i in range(ptr_copy, ptr_copy + 3):
        IDtype += binary[i]

    IDtype = int(IDtype, 2)
    ptr_copy += 3
    versions += ver


    if IDtype == 4:
        literal_value = ''
        print("lit")

        while int(binary[ptr_copy]) == 1:
            next_four = ''
            ptr_copy+=1

            for i in range(ptr_copy, ptr_copy + 4):
                next_four += binary[i]  

            literal_value += next_four
            ptr_copy += 4

        #here, pointer points to binary value 0
        next_four = ''
        ptr_copy+=1
        for i in range(ptr_copy, ptr_copy + 4):
            next_four += binary[i]  

        literal_value += next_four  
        ptr_copy += 4

        literal_value = int(literal_value, 2)
        stack.append(literal_value)
        print(stack, 'literals')

        while  len(binary) - 8 < ptr_copy < len(binary) and int(binary[ptr_copy]) == 0:
            ptr_copy += 1

        pointer = ptr_copy
        return decipher_binary(stack)

    else:

        length_type_ID = int(binary[ptr_copy])
        print("op")
        if length_type_ID == 0:

            next_fifteen = ''
            ptr_copy+=1

            for i in range(ptr_copy, ptr_copy + 15):
                next_fifteen += binary[i]  
            ptr_copy += 15

            sub_packet_length = int(next_fifteen, 2)

            pointer = ptr_copy
            decipher_binary(stack)

        else:
            next_eleven = ''
            ptr_copy+=1

            for i in range(ptr_copy, ptr_copy + 11):
                next_eleven += binary[i]  
            ptr_copy += 11

            sub_packet_count = int(next_eleven, 2)

            pointer = ptr_copy
            decipher_binary(stack)

        if IDtype == 0:

            sum = 0
            length = len(stack)
            for i in range(0, length):
                curr = stack.pop()
                sum += curr

            stack.append(sum)
            print(stack, 'after sum')
           
        elif IDtype == 1:

            prod = 1
            length = len(stack)
            for i in range(0, length):
                    
                curr = stack.pop()
                prod *= curr

            stack.append(prod)
            print(stack, 'after prod')
            
        elif IDtype == 2 or IDtype == 3:

            all_arr = []
            length = len(stack)
            for i in range(0, length):
                    
                curr = stack.pop()
                all_arr.append(curr)

            if IDtype == 2:
                stack.append(min(all_arr))
            else:
                stack.append(max(all_arr))

            print(stack, 'after min max')

        else:
            second = stack.pop()
            first = stack.pop()
                
            if IDtype == 5:
                if first > second:
                    stack.append(1)
                else:
                    stack.append(0)
            elif IDtype == 6:
                if first < second:
                    stack.append(1)
                else:
                    stack.append(0)
            else:
                if first == second:
                    stack.append(1)
                else:
                    stack.append(0)
                
            print(stack, 'after comparison')

        return stack

decipher_binary(stack)
print(stack, "final")
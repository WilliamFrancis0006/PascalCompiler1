'''
William Francis Complier 1

PROF:  Jean Gourd
CLASS: CSC 330-001
DATE:  1/11/20

(Modifications made are clearly labeled in the code below)
'''

import sys       

norw = 22        # number of reserved words (22 for complier 1)
txmax = 100      # length of identifier table
nmax = 14        # max number of digits in number
al = 10          # length of identifiers

a = []
chars = []
rword = []
table = []

global infile, outfile, ch, sym, id, num, linlen, kk, line, errorFlag, linelen

class tableValue():                     # some values in sym table
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

def error(num):
    global errorFlag;
    errorFlag = 1
    
    print
    if num == 1: 
        print >>outfile, "Use = instead of :=", sym                                      # WILLS MOD added sym output
    elif num ==2: 
        print >>outfile, "= must be followed by a number.", sym                          # WILLS MOD added sym output
    elif num ==3: 
        print >>outfile, "Identifier must be followed by =", sym                         # WILLS MOD added sym output
    elif num ==4: 
        print >>outfile, "Const, Var, Procedure must be followed by an identifier.", sym # WILLS MOD added sym output
    elif num ==5: 
        print >>outfile, "Semicolon or comman missing", sym                              # WILLS MOD added sym output
    elif num == 6: 
        print >>outfile, "Incorrect symbol after procedure declaration.", sym            # WILLS MOD added sym output
    elif num == 7:  
        print >>outfile, "Statement expected.", sym                                      # WILLS MOD added sym output
    elif num == 8:
        print >>outfile, "Incorrect symbol after statment part in block.", sym           # WILLS MOD added sym output
    elif num == 9:
        print >>outfile, "Period expected.", sym                                         # WILLS MOD added sym output
    elif num == 10: 
        print >>outfile, "Semicolon between statements is missing.", sym                 # WILLS MOD added sym output
    elif num == 11:  
        print >>outfile, "Undeclard identifier", sym                                     # WILLS MOD added sym output 
    elif num == 12:
        print >>outfile, "Assignment to a constant or procedure is not allowed.", sym    # WILLS MOD added sym output
    elif num == 13:
        print >>outfile, "Assignment operator := expected.", sym                         # WILLS MOD added sym output
    elif num == 14: 
        print >>outfile, "call must be followed by an identifier", sym                   # WILLS MOD added sym output
    elif num == 15:  
        print >>outfile, "Call of a constant or a variable is meaningless.", sym         # WILLS MOD added sym output
    elif num == 16:
        print >>outfile, "Then expected", sym                                            # WILLS MOD added sym output
    elif num == 17:
        print >>outfile, "Semicolon or end expected. ", sym                              # WILLS MOD added sym output
    elif num == 18: 
        print >>outfile, "DO expected", sym                                              # WILLS MOD added sym output
    elif num == 19:  
        print >>outfile, "Incorrect symbol following statement", sym                     # WILLS MOD added sym output
    elif num == 20:
        print >>outfile, "Relational operator expected.", sym                            # WILLS MOD added sym output
    elif num == 21:
        print >>outfile, "Expression must not contain a procedure identifier", sym       # WILLS MOD added sym output
    elif num == 22: 
        print >>outfile, "Right parenthesis missing", sym                                # WILLS MOD added sym output
    elif num == 23:  
        print >>outfile, "The preceding factor cannot be followed by this symbol.", sym  # WILLS MOD added sym output
    elif num == 24:
        print >>outfile, "An expression cannot begin with this symbol.", sym             # WILLS MOD added sym output
    elif num ==25:
        print >>outfile, "Constant or Number is expected.", sym                          # WILLS MOD added sym output
    elif num == 26: 
        print >>outfile, "This number is too large.", sym                                # WILLS MOD added sym output



#############################################################################################
######################## BEGIN WILL'S MOD (New Errors) ######################################
#############################################################################################

    elif num == 27:
        print >>outfile, "Left parenthesis expected", sym                                # WILLS MOD added sym output
    elif num == 28:
        print >>outfile, "UNTIL expected", sym                                           # WILLS MOD added sym output
    elif num == 29:
        print >>outfile, "OF expected", sym                                              # WILLS MOD added sym output
    elif num == 30:
        print >>outfile, "CEND expected", sym                                            # WILLS MOD added sym output
    elif num == 31:
        print >>outfile, "Semicolon expected", sym                                       # WILLS MOD added sym output
    elif num == 32:
        print >>outfile, "Colon expected", sym                                           # WILLS MOD added sym output
    elif num == 33:
        print >>outfile, "Identifier expected", sym                                      # WILLS MOD added sym output
    elif num == 34:
        print >>outfile, "TO or DOWNTO expected", sym                                    # WILLS MOD added sym output

##############################################################################################
######################## END WILL'S MOD (New Errors) #########################################
##############################################################################################

    exit(0)
    
def getch():
    global  whichChar, ch, linelen, line;
    if whichChar == linelen:             # if at end of line
        whichChar = 0
        line = infile.readline()         # get next line
        linelen = len(line)
        sys.stdout.write(line)
    if linelen != 0:
        ch = line[whichChar]
        whichChar += 1
    return ch
        
def getsym():
    global charcnt, ch, al, a, norw, rword, sym, nmax, id
    while ch == " " or ch == "\n" or ch == "\r":
        getch()
    a = []
    if ch.isalpha():
        k = 0
        while True:
            a.append(ch)
            getch()
            if not ch.isalnum():
                break
        id = "".join(a)
        flag = 0
        for i in range(0, norw):
            if rword[i] == id:
                sym = rword[i]
                flag = 1
        if  flag == 0:     # sym is not a reserved word
            sym = "ident"
            
    elif ch.isdigit():
        k=0
        num=0
        sym = "number"
        while True:
            a.append(ch)
            k += 1
            getch()
            if not ch.isdigit():
                break
        if k>nmax:
            error(30)
        else:
            id = "".join(a)
    
    elif ch == ':':
        getch()
        if ch == '=':
            sym = "becomes"
            getch()
        else:
            sym = "colon"
    
    elif ch == '>':
        getch()
        if ch == '=':
            sym = "geq"
            getch()
        else:
            sym = "gtr"
    
    elif ch == '<':
        getch()
        if ch == '=':
            sym = "leq"
            getch()
        elif ch == '>':
            sym = "neq"
            getch()
        else:
            sym = "lss"
    else:
        sym = ssym[ch]
        getch()
        
#--------------POSITION FUNCTION----------------------------

def position(tx, k):
    global  table;
    table[0] = tableValue(k, "TEST")
    i = tx
    while table[i].name != k:
        i=i-1
    return i

#---------------ENTER PROCEDURE-------------------------------

def enter(tx, k):   # enters something in procedure
    global id; 
    tx[0] += 1
    while (len(table) > tx[0]):
      table.pop()
    x = tableValue(id, k)
    table.append(x)

#--------------CONST DECLARATION---------------------------

def constdeclaration(tx):
    global sym, id;  
    if sym=="ident":
        temp = id
        getsym()
        if sym == "eql":
            getsym()
            if sym == "number":
                id = temp
                enter(tx, "const")
                getsym()
            else:
                error(2)
        else:
            error(3)
    else:
        error(4)

#-------------VARIABLE DECLARATION-----------------------------------

def vardeclaration(tx):
    global sym;
    if sym=="ident":
        enter(tx, "variable")
        getsym()
    else:
        error(4)
    
#-------------BLOCK------------------------------------------------

def block(tableIndex):
    tx = [1]
    tx[0] = tableIndex
    global sym, id;

#######################################################################################################
############################ BEGIN WILL'S MODS (Restricted Globals) ################################### 
#######################################################################################################

    while sym == "CONST" or sym == "VAR" or sym == "PROCEDURE":   # This while loop enables restricted globals (while sym == const var procedure)
        if sym == "CONST":
            while True:               # makeshift do while in python
                getsym()
                constdeclaration(tx)
                if sym != "comma":
                    break
            if sym != "semicolon":
                error(10);
            getsym()
    
        if sym == "VAR":
            while True:
                getsym()
                vardeclaration(tx)
                if sym != "comma":
                    break
            if sym != "semicolon":
                error(10)
            getsym()
    
        while sym == "PROCEDURE":
            getsym()
            if sym == "ident":
                enter(tx, "procedure")
                getsym()
            else:
                error(4)
            if sym != "semicolon":
                error(10)
            getsym()
            block(tx[0])
        
            if sym != "semicolon":
                error(10)
            getsym()
    
########################################################################################################
####################### END WILL'S MODS (Restricted Globals) ###########################################
########################################################################################################

    statement(tx[0])


#--------------STATEMENT----------------------------------------

def statement(tx):
    global sym, id;
    if sym == "ident":
        i = position(tx, id)
        if i==0:
            sys.stdout.write('SYM HERE: ' + sym)
            error(11)     ### ERRORS HERE
        elif table[i].kind != "variable":
            error(12)
        getsym()
        if sym != "becomes":
            error(13)
        getsym()
        expression(tx)
        
    elif sym == "CALL":
        getsym()
        if sym != "ident":
            error(14)
        i = position(tx, id)
        if i==0:
            error(11)
        if table[i].kind != "procedure":
            error(15)
        getsym()
    
    elif sym == "IF":
        getsym()
        condition(tx)
        if sym != "THEN":
            error(16)
        getsym()
        statement(tx)

####################################################################
#################### BEGIN WILL's MODS (ELSE) ######################
####################################################################

        if sym == "ELSE":
            getsym()
            statement(tx)

#####################################################################
#################### END WILL's MODS (ELSE) #########################
#####################################################################


    elif sym == "BEGIN":
        while True:
            getsym()
            statement(tx)
            if sym != "semicolon":
                break
        if sym != "END":
            error(17)
        getsym()
    
    elif sym == "WHILE":
        getsym()
        condition(tx)
        if sym != "DO":
            error(18)
        getsym()
        statement(tx)



######################################################################################
################## BEGIN WILL'S MODS (WRITE AND WRITELN) #############################
######################################################################################

    elif sym == "WRITE" or sym == "WRITELN":

        getsym()
        if sym != "lparen":
            error(27) # Lparen expected error
        getsym()
        expression(tx)
        while sym == "comma":
            getsym()
            expression(tx)
        if sym != "rparen":
            error(22) # Rparen expected error
        getsym()

#############################################################################################
######################### END WILL'S MODS (WRITE AND WRITELN) ###############################
#############################################################################################



############################################################################################
######################## BEGIN WILL'S MODS (REPEAT-UNTIL) ##################################
############################################################################################

    elif sym == "REPEAT":
        
        getsym()
        statement(tx)
        
        while sym == "semicolon":
            getsym()
            statement(tx)

        
        if sym != "UNTIL":
            error(28) # UNTIL expected error

        getsym()
        condition(tx)

###########################################################################################
####################### END WILL'S MODS (REPEAT-UNTIL) ####################################
###########################################################################################



###########################################################################################
####################### BEGIN WILL'S MODS (CASE-OF-CEND) ##################################
###########################################################################################

    elif sym == "CASE":
        getsym()
        expression(tx)
        if sym != "OF":
            error(29) # OF expected error
        getsym()
        while sym == "ident" or sym == "number":
            if sym == "ident":
                i = position(tx, id)
                if i==0:
                    error(11)
                if table[i].kind != "const":
                    error(25) # constant error
                    
            getsym()
            if sym != "colon":
                error(32) # Colon expected error
            getsym()
            statement(tx)
            if sym != "semicolon":
                error(31) # Semicolon expected error
            getsym()
        if sym != "CEND":
            error(30) # CEND expected error
        getsym()

###########################################################################################
####################### END WILL'S MODS (CASE-OF-CEND) ####################################
###########################################################################################





###########################################################################################
###################### BEGIN WILL'S MODS (FOR-TO-DOWNTO-DO) ###############################
###########################################################################################

    elif sym == "FOR":
        getsym()
        if sym != "ident":
            error(33)   # IDENT expected error
        i = position(tx, id)
        if i==0:
            error(11) 
        elif table[i].kind != "variable":
            error(12) # variable error
        getsym()
        if sym != "becomes":
            error(13)
        getsym()
        expression(tx)
        if sym != "TO" and sym != "DOWNTO":
            error(34)
        getsym()
        expression(tx)
        if sym != "DO":
            error(18)
        getsym()
        statement(tx)

###########################################################################################
################### END WILL'S MODS (FOR-TO-DOWNTO-DO) ####################################
###########################################################################################



#--------------EXPRESSION--------------------------------------

def expression(tx):
    global sym;
    if sym == "plus" or sym == "minus":
        getsym()
        term(tx)
    else:
        term(tx)
    
    while sym == "plus" or sym == "minus":
        getsym()
        term(tx)

#-------------TERM----------------------------------------------------

def term(tx):
    global sym;
    factor(tx)
    while sym=="times" or sym=="slash":
        getsym()
        factor(tx)

#-------------FACTOR--------------------------------------------------

def factor(tx):
    global sym;
    if sym == "ident":
        i = position(tx, id)
        if i==0:
            error(11)
        getsym()
    
    elif sym == "number":
        getsym()
    
    elif sym == "lparen":
        getsym()
        expression(tx)
        if sym != "rparen":
            error(22)
        getsym()
    
    else:
#        print "sym here is: ", sym
        error(24)

#-----------CONDITION-------------------------------------------------

def condition(tx):
    global sym;
    if sym == "ODD":
        getsym()
        expression(tx)
    
    else:
        expression(tx)
        if not (sym in ["eql","neq","lss","leq","gtr","geq"]):
            error(20)
        else:
            getsym()
            expression(tx)
    
#-------------------MAIN PROGRAM------------------------------------------------------------#

rword.append('BEGIN')
rword.append('CALL')
rword.append('CASE') # <----- WILL'S MOD 1
rword.append('CEND') # <----- WILL'S MOD 2
rword.append('CONST')
rword.append('DO')
rword.append('DOWNTO') # <--- WILL'S MOD 3
rword.append("ELSE") # <----- WILL'S MOD 4
rword.append('END')
rword.append('FOR') # <------ WILL'S MOD 5
rword.append('IF')
rword.append('ODD')
rword.append('OF') # <------- WILL'S MOD 6
rword.append('PROCEDURE')
rword.append('REPEAT') # <--- WILL'S MOD 7
rword.append('THEN')
rword.append('TO') # <------- WILL'S MOD 8
rword.append('VAR')
rword.append('UNTIL') # <---- WILL'S MOD 9
rword.append('WHILE')
rword.append('WRITE') # <---- WILL'S MOD 10
rword.append('WRITELN') # <-- WILL'S MOD 11


ssym = {'+' : "plus",
             '-' : "minus",
             '*' : "times",       
             '/' : "slash",
             '(' : "lparen",
             ')' : "rparen",
             '=' : "eql",
             ',' : "comma",
             '.' : "period",
             '#' : "neq",
             '<' : "lss",
             '>' : "gtr",
             '"' : "leq",
             '@' : "geq",
             ';' : "semicolon",
             ':' : "colon",}
              

charcnt = 0
whichChar = 0
linelen = 0
ch = ' '
kk = al                
a = []
id= '     '
errorFlag = 0
table.append(0)          # making the first position in the symbol table empty
sym = ' '            

infile =    sys.stdin    # path to input file
outfile =  sys.stdout    # path to output file, will create if doesn't already exist

getsym()                 # get first symbol
block(0)                 # call block initializing with a table index of zero

if sym != "period":      # period expected after block is completed
    error(9)
   
print >> outfile
if errorFlag == 0:
    print >>outfile, "Successful compilation!"

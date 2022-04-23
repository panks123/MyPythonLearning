#regular expressions

import  re

def display(matches):
    for match in matches:
        print(match)
    print("------------------------------------")


#raw string is used so that it ignores baackslash
pat=re.compile(r'[aA,.]')
mystr="Aye, said Mr. Gibenson Stark"
matches=pat.finditer(mystr)
display(matches)

pat1=re.compile(r'^s')   #checks if mystr starts with 's'
mystr="said Mr. Gibenson Stark and said good bye suddenly she gave a sudden answer"
matches1=pat1.finditer(mystr)
display(matches1)

pat=re.compile(r'ark$') #checks if mystr ends with 'ark'
mystr="Aye, said Mr. Gibenson Stark"
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'he..o') #checks for 'he'any_character''any_character'o'
mystr="hello , said Mr. Gibenson Stark hekko hetto hecco heccm"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'o?') #checks for 'he'any_character''any_character'o'
mystr="hello ooossoso"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'he..o') #checks for 'he'any_character''any_character'o'
mystr="hello , said Mr. Gibenson Stark hekko hetto hecco heccm"
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'[a-e]|S...')
mystr="hello , Said Mr. Gibenson Stark heko hetto heco heccm"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'[a-e]|S...')
mystr="hello , Said Mr. Gibenson Stark heko hetto heco heccm"
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'he*')  #checks for 'h'occurrence of e 0 or more times''
mystr="hello , Said Mr. Gibenson Stark heko heeeeeeeeeetto heheco heccm"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'(he)*')  #checks for occurrence of 'he' 0 or more times''
mystr="hello , Said Mr. Gibenson Stark heko heeeeeeeeeetto heheco heccm"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'(he)+')  #checks for occurrence of 'he' 1 or more times''
mystr="hello , Said Mr. Gibenson Stark heko heeeeeeeeeetto heheco heccm"
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'(he){2}|e{3}')  #checks for occurrence of 'he' 2 or occurrence of e 3 times''
mystr="hello , Said Mr. Gibenson Stark heko heheheheeeeeeeeeetto heheco heccm"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'\d')
mystr="hello , Said Mr. 456 Stark 012 heeeeeeeeeetto heheco 123"
matches=pat.finditer(mystr)
display(matches)
pat=re.compile(r'[0-9]')  # so r'\d' and r'[0-9]' are equivalent
mystr="hello , Said Mr. 456 Stark 012 heeeeeeeeeetto heheco 123"
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'\D')
mystr="hello , Said Mr. 456 Stark 012"
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'\s')
mystr="hello , Said Mr. 456 Stark 012 heeeeeeeeeetto heheco 123"
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'\S')
mystr="hello , Said Mr. 456 "
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'\w')
mystr="hello , Said Mr. 456@#$%#%#%!) "
matches=pat.finditer(mystr)
display(matches)

pat=re.compile(r'\W')
mystr="hello , Said Mr. 456@#$%#%#%!) "
matches=pat.finditer(mystr)
display(matches)


pat=re.compile(r'\d{5}-\d{4}')
mystr="hello , Said Mr. 45612-1234 ansn  cskd jasndwkd jdnasnd 32233-4546 qkdk " \
      " ewyvsb7 nadahdb6ngdh h hdqd 89893-9090 "
matches=pat.finditer(mystr)
display(matches)
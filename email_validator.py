
'''
This is an email verification function
start with CheckEmailValid(), pass a string argument of an email to function
it will call the rest of the functions

to use, import the module
then use problem6.CheckEmailValid(), pass a string argument of an email to function
returns a string that declares whether Valid Email, or why it is an Invalid Email, with different descriptions

Rules:
- Only 1 @
- Recipient name, Domain name, Top-level domain non-empty
- Recipient name acceptable values: [A-Z, a-z, 0-9, +, -, +, _]
- Recipient name multiple special character allowed, but cannot start or end with them
- Recipient name max 64 characters
- Domain Name acceptable values: [A-Z, a-z, 0.9]
- Domain Name, one hyphen, one period allowed (so one subdomain allowed)
- Domain name max 253 characters
- Top Level Domain (TLD) has restricted range, common ones allowed
- full range:
where "\." = .
and | = or 
\.ac|\.ad|\.ae|\.af|\.ag|\.ai|\.al|\.am|\.ao|\.aq|\.ar|\.as|\.at|\.au|\.aw|\.ax|\.az|\.ba|\.bb|\.be|\.bf|\.bg|\.bh|\.bi|\.bj|\.bm|\.bn|\.bo|\.bq|\.br|\.ca|\.ch|\.cn|\.de|\.es|\.eu|\.fi|\.fr|\.gf|\.gp|\.hk|\.hu|\.id|\.ie|\.il|\.in|\.iq|\.ir|\.is|\.it|\.jp|\.kr|\.lb|\.li|\.ma|\.mc|\.mo|\.mq|\.my|\.mx|\.mv|\.nl|\.no|\.nz|\.pa|\.pe|\.ph|\.pl|\.pk|\.pm|\.pn|\.pr|\.ps|\.pt|\.qa|\.ro|\.rs|\.ru|\.sa|\.sd|\.se|\.sg|\.si|\.sk|\.sl|\.sy|\.tw|\.us|\.uy|\.va|\.ve|\.vn|\.zm|\.zw

can run test_suite, named test_problem6.py
'''

import re
import pdb

#checks there is 1 @
def Checkforat(email_input):
  counter = 0
  position = 0

  for i in range(len(email_input)):
    if email_input[i] == "@":
        counter += 1
        position = i
  
  if counter == 1:
    return True
  
  if counter > 1:
    return 0
  

  return False  

#multiple special characters allowed
def CheckRecipientName(email_input):

  xy = email_input.split("@")
  recipientname = xy[0]

  if recipientname == "":
    return("No Recipient name")
  
  if len(recipientname) > 64:
    return("Recipient name length too long") 

  #cannot start or end with special character
  
  if recipientname[0] == "." or recipientname[-1] ==".":
    return("Invalid Recipient name")
  
  if recipientname[0] == "+" or recipientname[-1] =="+":
    return("Invalid Recipient name")
  
  if recipientname[0] == "_" or recipientname[-1] =="_":
    return("Invalid Recipient name")
  
  if recipientname[0] == "-" or recipientname[-1] =="-":
    return("Invalid Recipient name")

  #defines regex of unacceptable range
  unacceptablerange = re.compile(r'[^a-zA-Z0-9\.\+_-]')

  xx = unacceptablerange.findall(recipientname)

  if xx != []:
    return("Illegal characters in recipient name")
  
  return True


#verifies domain name
def CheckDomainName(email_input):
  xy = email_input.split("@")
  
  endbit = xy[1]

  #no empty Domain Name
  if endbit == "":
    return("No Domain name")

  #counters
  counter = 0
  counter2 = 0
  position = 0
  position2 = 0
  global top_level
  
  #counting number of periods
  for i in range(len(endbit)):
    if endbit[i] == ".":
        counter += 1
        if counter ==1:
          position = i
        if counter ==2:
          position2 = i
    
    if endbit[i] == "." and endbit[i-1] == ".":
      counter += 3
  
  #must have a period
  if counter == 0:
    return("Invalid Email")

  #case of one period
  if counter == 1:
    twobits = endbit.split('.')
    domainbit = twobits[0]

    if domainbit == "":
      return("No Domain name")

    if endbit[0] == "-" or domainbit[-1] == "-":
      return("Invalid Domain Name")
    
    if endbit[0] == "." or domainbit[-1] == ".":
      return("Invalid Domain Name")
    

    if len(domainbit) > 253:
      return("Invalid Domain Name")

    unacceptablerangex = re.compile(r'[^a-zA-Z0-9\.-]')

    xx = unacceptablerangex.findall(domainbit)

    if xx != []:
      return("Illegal characters in domain name")

    for i in domainbit:
      if i == "-":
        counter2 += 1
    
    if counter2 > 1:
      return("Invalid Domain Name")
    
    #set top level, with slice
    top_level = endbit[position:]
    return 0

  #case of 2 periods
  if counter == 2:
    domainbit = endbit[:position2]
    
    if len(domainbit) > 253:
      return("Invalid Domain Name")
    
    unacceptablerangex = re.compile(r'[^a-zA-Z0-9\.-]')

    xx = unacceptablerangex.findall(domainbit)

    if xx != []:
      return("Illegal characters in domain name")

    if domainbit[0] == "-" or domainbit[-1] == "-":
      return("Invalid Domain Name")
    
    for i in domainbit:
      if i == "-":
        counter2 += 1
    
    if counter2 > 1:
      return("Invalid Domain Name")
    
    #cannot start or end with hyphen, domain name
    if domainbit[0] == "-" or domainbit[-1] == "-":
      return("Invalid Domain Name")
    

    top_level = endbit[position2:]
    return 0

  #case of more than 3 periods, illegal
  if counter > 2:
    return("Invalid Email")

  return 0

#verifies top level
def Checktoplevel(top_level_input):

  #only alpha numeral
  unacceptablerange = re.compile(r'[^a-zA-Z0-9\.]')

  xx = unacceptablerange.findall(top_level_input)

  if xx != []:
    return("Illegal characters in top level")
  
  #only accept common ones, only accept exact matches, assume if not a common one, can have user submit a petition for review, or surmise that uncommon ones have dubious security
  acceptabletoplevel = re.compile(r'^\.com$|^\.org$|^\.ru$|^\.edu$|^\.net$|^\.info$|^\.biz$|^\.online$|^\.int$|^\.gov$|^\.mil$|^\.uk$|^\.ac$|^\.ad$|^\.ae$|^\.af$|^\.ag$|^\.ai$|^\.al$|^\.am$|^\.ao$|^\.aq$|^\.ar$|^\.as$|^\.at$|^\.au$|^\.aw$|^\.ax$|^\.az$|^\.ba$|^\.bb$|^\.be$|^\.bf$|^\.bg$|^\.bh$|^\.bi$|^\.bj$|^\.bm$|^\.bn$|^\.bo$|^\.bq$|^\.br$|^\.ca$|^\.ch$|^\.cn$|^\.de$|^\.es$|^\.eu$|^\.fi$|^\.fr$|^\.gf$|^\.gp$|^\.hk$|^\.hu$|^\.id$|^\.ie$|^\.il$|^\.in$|^\.iq$|^\.ir$|^\.is$|^\.it$|^\.jp$|^\.kr$|^\.lb$|^\.li$|^\.ma$|^\.mc$|^\.mo$|^\.mq$|^\.my$|^\.mx$|^\.mv$|^\.nl$|^\.no$|^\.nz$|^\.pa$|^\.pe$|^\.ph$|^\.pl$|^\.pk$|^\.pm$|^\.pn$|^\.pr$|^\.ps$|^\.pt$|^\.qa$|^\.ro$|^\.rs$|^\.ru$|^\.sa$|^\.sd$|^\.se$|^\.sg$|^\.si$|^\.sk$|^\.sl$|^\.sy$|^\.tw$|^\.us$|^\.uy$|^\.va$|^\.ve$|^\.vn$|^\.zm$|^\.zw$')
   
  yy = acceptabletoplevel.findall(top_level_input)

  if yy == []:
    return("Invalid top level domain")

  return 0

#main function, calling other functions, center for providing return values
def CheckEmailValid(email_input):

  #makes sure string input
  try:
    target = str(email_input)
  except (ValueError, TypeError):
    print("Please provide valid email")
  
  #different conditions, to test return values, to determine whether email is valid
  if Checkforat(target) != True:
    return("Invalid email")
  
  if CheckRecipientName(target) != True:
    return(CheckRecipientName(target))
  
  global top_level
  top_level=""
  
  if CheckDomainName(target) != 0:
    return(CheckDomainName(target))


  if Checktoplevel(top_level) !=0:
    return(Checktoplevel(top_level))
  
  return("This is a valid email")


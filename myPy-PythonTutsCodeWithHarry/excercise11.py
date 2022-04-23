#excercise 11---email extractor

import re
str='''foo barok ideler.dennis@gmail.com sup hey... user+123@example.com,
wydhello world!
RESCHEDULE 2'OCLOCK WITH JEFF@AMAZON.COM 
FOR TOMORROW@3pm
for more consult jdoe@example.com
 
All Companies HR E-Mail Idssrmeenak@in.ibm.com, rita.shetty@symphonysv.com, jobs@signatrix.in, sstanly@quinnox.com, 
freshers@citagus.com,gsrprasad@7hillsbiz.com, hr@7hillsbiz.com, jobs@astergatesolutions.com,freshers@lntinfotech.com, 
vsresume@visteon.com,consultant@miracleindia.com, resumes@bestvisionindia.com,careers@picopeta.com, 
hr@imageil.com,harish@dynproindia.com, ksantra@wdc.in,smita.kandiraju@ge.com, Careers@aricent.com,careers@iteamic.co.in, 
jobs@vcu.in, jobs@webyog.com,lakshmiprasad@hrmcindia.com,martina.mokal@cgi.com ,'''
pat=re.compile(r'[a-zA-Z0-9!.+_=*&$]+@[a-zA-Z0-9!.+_=*&$]+[.][a-zA-Z.0-9]+')

emails=re.findall(pat,str)
for email in emails:
    print(email)
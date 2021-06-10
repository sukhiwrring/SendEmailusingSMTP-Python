import sys
import requests

from datetime import datetime


from send_mail import send_mail

#This function will format the message with name and org arguments
def format_msg(my_name="Sukh", my_org="rotatract club"):
	my_msg = """Hi  {name},
	Thank you for taking part in this survey at {org}. We will be sending you instructions soon.
	""".format(name=my_name,org=my_org)  
	return my_msg

#Takes arguments from main function for name,to_email and org
#This function also calls send_mail function which utilizes smtp library to send message to gmail
def send(name, org=None,to_email=None, verbose=False):
    assert to_email !=None
    if org != None:
        msg = format_msg(my_name=name, my_org=org)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, org, to_email)
    # send the message
    try:
        send_mail(text=msg, to_emails= [to_email], html=None)
        sent = True
    except:
        sent = False
    return sent
 
if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    org= "aba"
    email= "taranharry@gmail.com"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, org, to_email= email,  verbose=False)
    print(response)
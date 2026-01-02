import pywhatkit as pwk
# this code is for sending whatsapp message using pywhatkit library 
#Define the recipient's phome number (with country code) and the message
phone_number = "+91 8328668266"
message = "Hello, this is a test message sent using laptop coding! 8:11 pm"
time_hour = "0" #when should be sent
time_min = "0"  #when should be sent
#Send the WhatsApp message immediately
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=False)  
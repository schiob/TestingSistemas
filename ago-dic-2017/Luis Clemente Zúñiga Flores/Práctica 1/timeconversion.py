"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM  on a 12-hour clock, and 00:00:00 on a 24-hour
clock. Noon is 12:00:00PM on a 24-hour clock, and 12:00:00 on a 24-hour clock.

Input Format
A single string containing a time in 12-hour clock format (i.e.:hh:mm:ssAM  or hh:mm:ssPM), where 
01<=hh<=12 and 00<=mm,ss<=59.
Output Format

Convert and print the given time in 24-hour format, where 00<= hh <= 23.

Sample Input

07:05:45PM
Sample Output

19:05:45
"""
def timeConversion(entrada):   
	    
    hora_dict = {"hora": entrada[0:2],"min": entrada[3:5], "seg": entrada[6:8],"part":entrada[8:]}

    if hora_dict["part"] == "AM":
        if int(hora_dict["hora"])== 12:
            hora_dict["hora"]='00'
    elif hora_dict["part"]== "PM":  
        if int(hora_dict["hora"])== 1:
            hora_dict["hora"]=13
        elif int(hora_dict["hora"])== 2:
            hora_dict["hora"]=14            
        elif int(hora_dict["hora"])== 3:
            hora_dict["hora"]=15
        elif int(hora_dict["hora"])== 4:
            hora_dict["hora"]=16
        elif int(hora_dict["hora"])== 5:
            hora_dict["hora"]=17
        elif int(hora_dict["hora"])== 6:
            hora_dict["hora"]=18
        elif int(hora_dict["hora"])== 7:
            hora_dict["hora"]=19
        elif int(hora_dict["hora"])== 8:
            hora_dict["hora"]=20
        elif int(hora_dict["hora"])== 9:
            hora_dict["hora"]=21
        elif int(hora_dict["hora"])== 10:
            hora_dict["hora"]=22
        elif int(hora_dict["hora"])== 11:
            hora_dict["hora"]=23
    hora = "%s:%s:%s" % (hora_dict["hora"],hora_dict["min"],hora_dict["seg"])   
)
    return hora


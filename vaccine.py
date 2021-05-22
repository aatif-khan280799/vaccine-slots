import requests
import  time
from datetime import datetime, timedelta
# plese import these packages first using pip command





#************ Edit here ONLY *************

person_age = 52                          #enter your age
area_pincode = ["411014"]                #enter your pincode

#****************************************




total_days=1
print_flag = 'Y'

print("searching for vaccination slot")

current = datetime.today()
form = [current +timedelta(days = i) for i in range(total_days)]

correct_date = [i.strftime("%d-%m-%y") for i in form]

while True:
    i=0
    for find_code in area_pincode:
        for enter_date in correct_date:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(find_code,enter_date)
            requirements = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            final_op = requests.get(url,headers=requirements)
            if final_op.ok:
                file_json = final_op.json()
                flag = False
                if file_json["centers"]:
                    if (print_flag.lower()=='y'):
                        for place in file_json["centers"]:
                            for availability in place["sessions"]:
                                if(availability["min_age_limit"]<=person_age and availability["available_capacity"]>0):
                                    print("hospital name :",place["name"])
                                    print("block",place["block_name"])
                                    print("price",place["fee_type"])
                                    print("status",availability["available_capacity"])

                                    if(availability["vaccine"] != ''):
                                        print("type of vaccine is",availability["vaccine"])
                                    i=i+1
                                else:
                                    pass
                else:
                    pass
            else:
                pass
        else:
            print("sorry there is No Response .Try later")

    if(i==0):
        print("no slot available")
    else:
        print("searching is finish")

    date_now = datetime.now()+timedelta(minutes=1)

    while datetime.now()<date_now:
        time.sleep(1)

#END OF PROGRAM
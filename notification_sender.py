from database import DB
from twilio.rest import Client
import threading
account_sid = 'AC454b7467e17210f09fb9d769cfe12683'
auth_token = '68b46ec666568b003fafa1ff4746d8d0'
client = Client(account_sid, auth_token)
# start=time.time()


class sender(DB):
    def __init__(self):
        super(sender,self).__init__()
        self.thread_list=[]

    def send_notification(self,api_dict):
        for i in api_dict:
            for key,item in i.items():
                t=threading.Thread(target=self.msg_formatter,args=[key,item])
                t.start()
                self.thread_list.append(t)
        for thread in self.thread_list:
            thread.join()

    def msg_formatter(self,key,item):
        sub_thread=[]
        # print(key,item)
        txt=f"""
Vaccine SLots Are Available At\n
--------------------------------------------------------------------
    Name : {item['name']}\n
    Address : {item['address']}\n
    State Name : {item["state_name"]}\n
    District : {item["district_name"]}\n
    Block Name : {item["block_name"]}\n
    Pincode : {item["pincode"]}\n
    From : {item["from"]}\n
    To : {item["to"]}\n
    Fee Type : {item["fee_type"]}\n
    Date : {item["date"]}\n
    Available Capacity : {item["available_capacity"]}\n
    Fee : {item["fee"]}\n
    Vaccine Name : {item["vaccine"]}\n
--------------------------------------------------------------------
        """
        # # print(key)
        phone_list = self.get_collection_info(str(key))
        for phone in phone_list:
            if(len(phone['age'])==4):
                if (phone['age']=='both'):
                    t=threading.Thread(target=self.main_message,args=[str(phone['_id']),txt])
                    t.start()
                    sub_thread.append(t)

            elif(len(phone['age'])==2):
                    if(int(phone["age"])>=item['min_age_limit']):
                        t=threading.Thread(target=self.main_message,args=[str(phone["_id"]),txt])
                        t.start()
                        sub_thread.append(t)
        for thread in sub_thread:
            thread.join()

    def main_message(self,number,txt):
        message = client.messages \
            .create(
            from_='whatsapp:+14155238886',
            body=txt,
            to=f'whatsapp:+{number}'
        )





        # print(phone_list)



# if __name__=='__main__':
#     y=sender()
#     m=[{400705: {'center_id': 716342, 'name': 'Cloudnine Hospital Navimumbai', 'address': 'Plot No 17 Phase 2 Sector 19D Vashi Navi Mumbai Maharashtra India', 'state_name': 'Maharashtra', 'district_name': 'Thane', 'block_name': 'Navi Mumbai Municipal Corporation', 'pincode': 400705, 'from': '09:00:00', 'to': '18:00:00', 'lat': 19, 'long': 73, 'fee_type': 'Paid', 'session_id': 'a6ce9ec6-c561-4598-8388-3c7df19263ca', 'date': '03-06-2021', 'available_capacity_dose1': 0, 'available_capacity_dose2': 1, 'available_capacity': 1, 'fee': '850', 'min_age_limit': 18, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-06:00PM']}}, {400705: {'center_id': 608233, 'name': 'MPCT Hospital Navi Mumbai', 'address': 'C7 Budhyadev Mandir Marg Sector 4 Sanpada Navi Mumbai', 'state_name': 'Maharashtra', 'district_name': 'Thane', 'block_name': 'Navi Mumbai Municipal Corporation', 'pincode': 400705, 'from': '09:00:00', 'to': '15:30:00', 'lat': 19, 'long': 73, 'fee_type': 'Paid', 'session_id': 'ca416aa4-3384-46a4-9d1f-a948dda6a6d1', 'date': '03-06-2021', 'available_capacity_dose1': 0, 'available_capacity_dose2': 13, 'available_capacity': 13, 'fee': '900', 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-10:00AM', '10:00AM-11:00AM', '11:00AM-12:00PM', '12:00PM-03:30PM']}}]
#


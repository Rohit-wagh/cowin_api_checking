import aiohttp
import asyncio
import datetime
from notification_sender import sender

send=sender()

def clean(lst):
    message = []
    lst=list(filter(None.__ne__,lst))

    for session in lst:
        for info in session['sessions']:
            if(info['available_capacity']>0):
               message.append({info['pincode']:info})
    if(len(message)>0):
        send.send_notification(message)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks=[]
        for pin in send.get_collection_name():
            task= asyncio.ensure_future(get_call(session,pin))
            tasks.append(task)
        final = await asyncio.gather(*tasks)
    clean(final)


async def get_call(session,pincode):
    url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={datetime.datetime.today().strftime('%d-%m-%Y')}"

    async with session.get(url) as responce :
        result_data = await responce.json()
        for i in result_data['sessions']:
           if(i['available_capacity']>0):
               return result_data
        # return result_data
        # print("len is ",len(result_data['sessions']))
        # print(len(result_data))
        # if(len(result_data['sessions'])>0):
        #     # print(result_data)
        #     return result_data
            # if(result_data['sessions']['available_capacity']>0):
            #     return result_data
asyncio.run(main())


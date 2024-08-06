import asyncio


async def sms(phone_number):
    await asyncio.sleep(0.2)


def get_phone_number(national_id):
    return f'quera{national_id}'

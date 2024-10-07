import flet as ft
from flet import Page, Text, ElevatedButton, TextField
import phonenumbers
from phonenumbers import carrier, geocoder

lang = 'ru'
page = None

def phone(phquery):
    try:
        ph = phonenumbers.parse(phquery)
        ph1 = phonenumbers.is_valid_number(ph)
        ph2 = phonenumbers.number_type(ph)
        phone_types = {
            0: 'fixed_line',
            1: 'mobile',
            2: 'fixed_line_or_mobile',
            3: 'toll_free',
            4: 'premium_rate',
            5: 'TSoIP',
            7: 'personal_number',
            8: 'universal_or_company_number'
        }
        ph2 = phone_types.get(ph2, 'error')
        ph3 = phonenumbers.format_number(ph, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        ph4 = phonenumbers.format_number(ph, phonenumbers.PhoneNumberFormat.NATIONAL)
        ph5 = geocoder.country_name_for_number(ph, lang)
        ph6 = geocoder.description_for_number(ph, lang)
        ph7 = carrier.name_for_number(ph, lang)
        return {
            'is_valid': ph1,
            'type': ph2,
            'international': ph3,
            'national': ph4,
            'country': ph5,
            'description': ph6,
            'carrier': ph7
        }
    except phonenumbers.phonenumberutil.NumberParseException:
        return {'error': 'Invalid phone number'}

def on_phone_submit(e):
    phone_info = phone(phone_text_field.value)
    phone_info_text.value = str(phone_info)
    global page
    page.update()

def main(p: Page):
    
    global phone_info_text, phone_text_field, page
    page = p

    phone_text_field = TextField(label="INPUT PHONE NUMBER")
    phone_info_text = Text()
    button = ElevatedButton("Check Phone", on_click=on_phone_submit)
    page.add(phone_text_field)
    page.add(phone_info_text)
    page.add(button)
    page.update()

ft.app(target=main)

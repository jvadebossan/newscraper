import requests

def main(title, text):
    key = 'Co3hRoiZimbWBR2ZVCn0VIPbfdR0deNM'
    text = f'"""\n{text}"""'
    t_title = title

    login_data = {
        'api_dev_key': key,
        'api_user_name': 'newscraper',
        'api_user_password': 'newscraperdojv'
    }
    data = {
        'api_option': 'paste',
        'api_dev_key': key,
        'api_paste_code': text,
        'api_paste_name': t_title,
        'api_paste_expire_date': '1D',
        'api_user_key': None,
        'api_paste_format': 'python'
    }

    login = requests.post(
        "https://pastebin.com/api/api_login.php", data=login_data)


    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    return r.text
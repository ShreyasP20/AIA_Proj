import requests
from bs4 import BeautifulSoup

url = 'https://indiansignlanguage.org/about/'  

headers = {
    'authority': 'indiansignlanguage.org',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'cf_chl_3=3971c0a0e0546d8; cf_clearance=e9u.bW6gNgCTrW6J.w1Tf4sFaOg42noRpcRATDl5gPw-1705776001-1-AYluUimNezZd0DIQgPnHQQvgts0mucYUyPeCf7RA56A2qLhqR4PAN76PTXnh4ZGXGij4hpYLYCVoyOKbpTQFet0=',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    iframe_tag = soup.find('iframe')

    if iframe_tag:
        embedded_link = iframe_tag.get('src')

        if embedded_link:
            print(f'Embedded Link: {embedded_link}')
        else:
            print('No src attribute found in the <iframe> tag.')
    else:
        print('No <iframe> tag found on the page.')
else:
    print(f'Request failed with status code: {response.status_code}')

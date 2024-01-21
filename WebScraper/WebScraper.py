import requests
from bs4 import BeautifulSoup

url = 'https://indiansignlanguage.org/banana/'  

headers = {
    'authority': 'indiansignlanguage.org',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'cf_clearance=EXzTe2rD64gokncMRDGNq4122s32Hzz6dsJSOjGLNs0-1705814540-1-Aca+Hs50Kx9JLMc0KJLt9tFYLnDXGXYzhdDamFgQnWapPMm1ivJ7H+Q9h1L8UKCvo3en4X0p6ORwPq9qDugi0Ag=',
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

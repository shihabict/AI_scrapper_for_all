import selenium.webdriver as webdriver
from bs4 import BeautifulSoup


def scrape_url(web_url):
    print('Start scrapping the website')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # service = Service(chrome_driver_path)
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(web_url)
        # get the page source
        page_source = driver.page_source
    except Exception as e:
        print(f"Error getting page source: {str(e)}")
        page_source = None
    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error closing driver: {str(e)}")

    return page_source

def extract_body_content(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    #extract the text
    cleaned_text = soup.get_text(separator='\n', strip=True)
    cleaned_content = '\n'.join([line.strip() for line in cleaned_text.split('\n') if line.strip()])

    return cleaned_content

def split_dom_into_sections(dom_content,max_tokens=6000):
    return [dom_content[i:i+max_tokens] for i in range(0,len(dom_content),max_tokens)]


import pandas as pd
import bs4
import requests

doc_df = pd.read_csv('excel_file.csv')

urls = doc_df['URL'].dropna(axis = 0)

url_list = list(urls)

from selenium.webdriver.common.by import By

def head_body(url_list):
    heading = []
    body = []
    for i in range(len(url_list)):
        path_ = "D:\Text Analysis\chromedriver.exe"
        wd = webdriver.Chrome(executable_path=path_)
        try:
            wd.get(url_list[i])
            heading1 = wd.find_element(By.TAG_NAME, "h1").text
            heading.append(heading1)

            body1 = wd.find_element(By.CLASS_NAME, 'td-post-content').text
            body1 = body1.split("\n")
            body1 = "".join(body1)
            body.append(body1)
        except:
            heading.append(-1)
            body.append(-1)

    d = {'heading': heading, 'body': body}
    df = pd.DataFrame(data=d)
    return df

df = head_body(url_list)
df.to_csv('extraction_output')
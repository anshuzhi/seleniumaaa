cookies={
    "BA_HECTOR":"aha024al8g840ka4nu1g14ka80q",
    "H_PS_PSSID":"33425_33514_33401_33272_31253_33336_33321_33568",
    "__yjs_duid":"1_96ba0b97bc08a5568dc9428b27f6f9b71611800907586",
    "delPer":"0",
    "BDORZ":"B490B5EBF6F3CD402E515D22BCDA1598",
    "BAIDUID": "CE128AD6A2948710238D2382CFB0ECC7:FG=1",
    "PSTM": "1606473283",
    "BIDUPSID": "A1A5E7FE6D8C888D5A4F14C4B546567A",
    "PSINO": "2",
    "__l": "r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DIMsEbBe-kmTRYuKGfNwLhopBcT7-oOEHGuQfT6rf1oWSSmRn-5A29VudpfE_Lnw1%26wd%3D%26eqid%3D96e9edee0005e0ae0000000260124d54&l=%2Fwww.zhipin.com%2Fzhengzhou%2F&s=1&g=&s=3&friend_source=0",
    "_bl_uid": "C6kpjjaI70FwO81qRssR7Owj8t5e",
    "__zp_seo_uuid__": "c931fbf9-04f5-4cac-b75d-abdfebe4d344",
    "BDRCVFR[k2U9xfnuVt6]": "mk3SLVN4HKm",
    "BAIDUID_BFESS": "CE128AD6A2948710238D2382CFB0ECC7:FG=1",
    "wt2": "dGaxKbb5rhqFl7Ch",
# "HMACCOUNT_BFESS": "8DC35678E9BFBB30",
    # "__c": "1611812187",
    # "Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a": "1611813859",
    # "__a": "79191964.1607772421.1611800959.1611812187.42.6.14.17",
    # "__zp_stoken__": "19babaWd1UQpkBV5iPwgmIFVcV2oxUhQiRm48E2suFmc8Nn5mbQwQexAFGlFgbQo6BRxKLiAGHDMMeDYkY2cKNGhcNCg2HDA2NAtzQ10CVGxLEFlJTUItEzJTVXROSQUAA01AFzt9Rxt8BQlHeg%3D%3D",
    # "lastCity": "101180100",
    # "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a": "1609752227,1611800957,1611803513,1611812187",
    # "__g": "-",
}
from selenium import webdriver
import time,re
url="https://www.zhipin.com/c101210100/?ka=sel-city-101210100"
driver = webdriver.Chrome() #  代码在执行的时候回自行去寻找chromedriver.exe(在python目录下寻找)，不再需要制定chromedriver.exe路径
# driver.add_cookie(cookie_dict=cookies)
driver.get(url)
for name,value in cookies.items():
    cookie={
        'name':name,
        'value':value,
    }
    driver.add_cookie(cookie)

driver.get(url)
time.sleep(3)
data=driver.page_source
# print(data)
res='<span class="job-name">.*?>(.*?)</a></span>'
datas=re.findall(res,data)
print(datas)
# driver.quit()
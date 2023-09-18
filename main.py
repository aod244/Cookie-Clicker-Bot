from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, value="cookie")
start = time.time()
end_time = time.time()

while time.time() < end_time + 300:
    cookie_button.click()
    if time.time() > start + 5:
        upgrades = driver.find_element(By.ID, value="store").text.split("\n")
        upgrades_prices = []
        upgrades_name = []
        updates_dict = {}

        for upgrade in upgrades:
            if " - " in upgrade:
                new = upgrade.split(" - ")
                upgrades_name.append(new[0])
                upgrades_prices.append(int(new[1].replace(",", "")))
            else:
                continue

        for i in range(len(upgrades_prices)):
            updates_dict[i] = {'UpgradeName': upgrades_name[i], 'Price': upgrades_prices[i]}

        money = driver.find_element(By.XPATH, value='//*[@id="money"]').text
        money_int = int(money.replace(",", ""))
        for upgrade in reversed(updates_dict):
            if money_int >= updates_dict[upgrade]['Price']:
                if updates_dict[upgrade]['UpgradeName']:
                    click_upgrade = driver.find_element(By.ID, value=f"buy{updates_dict[upgrade]['UpgradeName']}")
                    try:
                        click_upgrade.click()
                        break
                    except:
                        print("no cookies")
            else:
                pass
        start = time.time()

cookies_per_sec = driver.find_element(By.ID, value="cps").text
print(f"after 5 minutes {cookies_per_sec}")
driver.quit()

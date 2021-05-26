from selenium import webdriver

celsius = float(101.54)
fahrenheit = str((celsius * 9 / 5) + 32)
tmp=fahrenheit.rfind('.')
fahrenheit=fahrenheit[0:(tmp+2)]




driver = webdriver.Chrome(executable_path="W:\\Proga\\Projects\\DjangProjects\\testTaskForAuto\\chromedriver\\chromedriver.exe")
url = "https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm"

try:
    driver.get(url=url)

    celsius_input = driver.find_element_by_id("argumentConv")
    celsius_input.clear()
    celsius_input.send_keys(str(celsius))
    fahrenheit_result = driver.find_element_by_id("answer").text

    tmp1=fahrenheit_result.find('=')
    tmp2=fahrenheit_result.rfind('.')
    fahrenheit_result = fahrenheit_result[(tmp1+2):(tmp2+2)]


    if fahrenheit_result == fahrenheit:
        print("OK")
        print(fahrenheit, '-', fahrenheit_result)
    else:
        print("BUG")
        print(fahrenheit, '-', fahrenheit_result)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()


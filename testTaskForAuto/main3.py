from selenium import webdriver
import time
input_value = float(5242)


grams = input_value*28.34952
my_result = str(grams.__round__(1))



driver = webdriver.Chrome(executable_path="W:\\Proga\\Projects\\DjangProjects\\testTaskForAuto\\chromedriver\\chromedriver.exe")
url = "https://www.metric-conversions.org/ru/weight/ounces-to-grams.htm"

try:
    driver.get(url=url)

    c_input = driver.find_element_by_id("argumentConv")
    c_input.clear()
    c_input.send_keys(str(input_value))
    ft_result = driver.find_element_by_id("answer").text
    time.sleep(3)
    tmp1=ft_result.find('=')
    tmp2=ft_result.rfind('g')
    ft_result = ft_result[(tmp1+2):(tmp2)]


    if ft_result == my_result:
        print("OK")
        print(my_result, '-', ft_result)
    else:
        print("BUG")
        print(my_result, '-', ft_result)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()


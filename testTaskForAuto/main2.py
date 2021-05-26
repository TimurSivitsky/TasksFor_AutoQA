from selenium import webdriver
import time
input_value = float(101.12)




meters_in_ft = int(input_value // .3048)
inches = input_value / .3048 % 1 * 12
my_result = str(meters_in_ft) +"ft " + str(inches.__round__(1))



driver = webdriver.Chrome(executable_path="W:\\Proga\\Projects\\DjangProjects\\testTaskForAuto\\chromedriver\\chromedriver.exe")
url = "https://www.metric-conversions.org/length/meters-to-feet.htm"

try:
    driver.get(url=url)

    celsius_input = driver.find_element_by_id("argumentConv")
    celsius_input.clear()
    celsius_input.send_keys(str(input_value))
    ft_result = driver.find_element_by_id("answer").text
    time.sleep(3)
    tmp1=ft_result.find('=')
    tmp2=ft_result.rfind('.')
    ft_result = ft_result[(tmp1+2):(tmp2+2)]


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


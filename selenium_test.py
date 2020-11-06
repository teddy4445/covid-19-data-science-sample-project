import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def run():
    driver = webdriver.Chrome()
    sentence_codes = ["2092039"]
    texts = []
    for sentence_code in sentence_codes:
        driver.get("https://tatoeba.org/eng/sentences/show/{}".format(sentence_code))
        check_elements = driver.find_elements_by_class_name("text")
        for element in check_elements:
            if element.get_attribute("lang") == "en":
                texts.append(element.text)
                break
        driver.close()


def run2():
    driver = webdriver.Chrome()
    iso = []
    country = []
    data_entery = []
    driver.get("https://genderize.io/our-data")
    left_elements = []
    right_elements = []
    while len(left_elements) == 0:
        left_elements = driver.find_elements_by_class_name("MuiTableCell-alignLeft")
        right_elements = driver.find_elements_by_class_name("MuiTableCell-alignRight")
        time.sleep(1)
    index_left = 2
    index_right = 1
    while index_right < len(right_elements):
        try:
            iso.append(left_elements[index_left].text)
            index_left += 1
            country.append(left_elements[index_left].text)
            index_left += 1
            data_entery.append(right_elements[index_right].text)
            index_right += 1
            print("Finish with {}".format(index_right))
        except:
            break
    print(iso)
    print(country)
    print(data_entery)
    driver.close()


if __name__ == '__main__':
    run2()

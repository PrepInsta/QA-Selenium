from navigation import Navigation
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def handle_browser_alerts(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "alertButton"))
    clk_btn.click()
    time.sleep(3)
    print(mydriver.switch_to.alert.text)
    mydriver.switch_to.alert.accept()
    time.sleep(3)


def delayed_alert(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "timerAlertButton"))
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    time.sleep(3)
    mydriver.switch_to.alert.accept()


def handle_cancelok_alerts(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "confirmButton"))
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    time.sleep(3)
    mydriver.switch_to.alert.accept()
    conf_res = n.get_element((By.ID, "confirmResult"))
    print(conf_res.text)
    time.sleep(3)
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    mydriver.switch_to.alert.dismiss()
    time.sleep(3)
    print(conf_res.text)


def handle_text_alerts(mydriver):
    n.goto_toolsqa_page("alerts")
    clk_btn = n.get_element((By.ID, "promtButton"))
    clk_btn.click()
    WebDriverWait(mydriver, 10).until(EC.alert_is_present())
    print(mydriver.switch_to.alert.text)
    mydriver.switch_to.alert.send_keys("Prepinsta")
    time.sleep(3)
    mydriver.switch_to.alert.accept()
    enter_txt = n.get_element((By.ID, "promptResult"))
    print(enter_txt.text)


def handle_new_window(mydriver):
    n.goto_toolsqa_page("browser-windows")
    clk_btn = n.get_element((By.ID, "tabButton"))
    clk_btn.click()
    time.sleep(3)
    parent = mydriver.current_window_handle
    WebDriverWait(mydriver, 10).until(EC.number_of_windows_to_be(2))
    child = mydriver.window_handles[1]
    mydriver.switch_to.window(child)
    time.sleep(3)
    heading = n.get_element((By.ID, "sampleHeading"))
    print(heading.text)
    mydriver.switch_to.window(parent)
    time.sleep(3)
    print(mydriver.title)


def handle_iframes(mydriver):
    n.goto_toolsqa_page("nestedframes")
    parent = n.get_element((By.ID, "frame1"))
    mydriver.switch_to.frame(parent)
    child = n.get_element((By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']"))
    parent_txt = n.get_element((By.XPATH, "/html/body"))
    print(parent_txt.text)
    time.sleep(3)
    mydriver.switch_to.frame(child)
    child_txt = n.get_element((By.XPATH, "/html/body/p"))
    print(child_txt.text)
    time.sleep(3)
    mydriver.switch_to.default_content()
    default_content_txt = n.get_element((By.XPATH, "//div[@class='main-header']"))
    print(default_content_txt.text)


def handle_download_upload(mydriver):
    n.goto_toolsqa_page("upload-download")
    dwnld_btn = n.get_element((By.ID, "downloadButton"))
    upld_btn = n.get_element((By.ID, "uploadFile"))
    dwnld_btn.click()
    time.sleep(5)
    upld_btn.send_keys("/Users/viraj/Desktop/upload.txt")
    time.sleep(3)
    upld_file_path = n.get_element((By.ID, "uploadedFilePath"))
    print(upld_file_path.text)


def handle_old_dropdown(mydriver, colour):
    n.goto_toolsqa_page("select-menu")
    select = Select(n.get_element((By.ID, "oldSelectMenu")))
    options = select.options

    for i in options:
        print(i.text)

    select.select_by_visible_text(colour)
    time.sleep(3)


def handle_new_dropdowns(mydriver, title):
    n.goto_toolsqa_page("select-menu")
    drop = n.get_element((By.ID, "selectOne"))
    drop.click()
    time.sleep(3)
    title_xpath = "//div[@id='selectOne']//div[@id='react-select-3-option-0-0']/../div[contains(.,'{0}')]".format(title)
    clk_title = n.get_element((By.XPATH,title_xpath))
    clk_title.click()
    time.sleep(3)

def handle_tooltips(mydriver):
    n.goto_toolsqa_page("tool-tips")
    hover_ele= n.get_element((By.ID,"toolTipButton"))
    actions= ActionChains(mydriver)
    actions.move_to_element(hover_ele).perform()
    tool_tip= n.get_element((By.XPATH,"//div[@id='buttonToolTip']/div[@class='tooltip-inner']"))
    print(tool_tip.text)
    time.sleep(3)

def handle_drag_drop(mydriver):
    n.goto_toolsqa_page("droppable")
    draggable= n.get_element((By.ID,"draggable"))
    droppable = n.get_element((By.ID,"droppable"))
    print(droppable.text)
    actions= ActionChains(mydriver)
    # actions.click_and_hold(draggable).move_to_element(droppable).release(draggable).perform()
    # actions.drag_and_drop_by_offset(draggable,250,80).perform()
    actions.drag_and_drop(draggable,droppable).perform()
    print(droppable.text)
    time.sleep(3)

def handle_slider(mydriver,val):
    n.goto_toolsqa_page("slider")
    slider= n.get_element((By.XPATH,"//input[@type='range']"))
    actions= ActionChains(mydriver)
    target=-200
    actions.move_to_element_with_offset(slider,target,1)
    actions.click().perform()
    while slider.get_attribute("value") != str(val):
        actions.click().drag_and_drop_by_offset(slider,target,0).perform()
        target+=1
        print(str(target) + ":" + slider.get_attribute("value"))
    time.sleep(5)


if __name__ == '__main__':
    try:
        n = Navigation()
        driver = n.get_driver()
        # handle_browser_alerts(driver)
        # delayed_alert(driver)
        # handle_cancelok_alerts(driver)
        # handle_text_alerts(driver)
        # handle_new_window(driver)
        # handle_iframes(driver)
        # handle_download_upload(driver)
        # handle_old_dropdown(driver, "Green")
        # handle_new_dropdowns(driver, 'Prof.')
        # handle_tooltips(driver)
        # handle_drag_drop(driver)
        handle_slider(driver,8)
    finally:
        driver.close()
        driver.quit()

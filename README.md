# toolsf_for_webscraping_and_navigation
Using Selenium for Web scraping and Navigation.

Common Error:-
#Do not name your file selenium.py

requirements:-
-->pip install selenium
-->pip install PyUserInput


Navigating
The first thing you’ll want to do with WebDriver is navigate to a link. The normal way to do this is by calling get method:

driver.get("http://www.google.com")
WebDriver will wait until the page has fully loaded (that is, the onload event has fired) before returning control to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded. If you need to ensure such pages are fully loaded then you can use waits.

3.1. Interacting with the page
Just being able to go to places isn’t terribly useful. What we’d really like to do is to interact with the pages, or, more specifically, the HTML elements within a page. First of all, we need to find one. WebDriver offers a number of ways to find elements. For example, given an element defined as:

<input type="text" name="passwd" id="passwd-id" />
you could find it using any of:

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")
You can also look for a link by its text, but be careful! The text must be an exact match! You should also be careful when using XPATH in WebDriver. If there’s more than one element that matches the query, then only the first will be returned. If nothing can be found, a NoSuchElementException will be raised.

WebDriver has an “Object-based” API; we represent all types of elements using the same interface. This means that although you may see a lot of possible methods you could invoke when you hit your IDE’s auto-complete key combination, not all of them will make sense or be valid. Don’t worry! WebDriver will attempt to do the Right Thing, and if you call a method that makes no sense (“setSelected()” on a “meta” tag, for example) an exception will be raised.

So, you’ve got an element. What can you do with it? First of all, you may want to enter some text into a text field:

element.send_keys("some text")
You can simulate pressing the arrow keys by using the “Keys” class:

element.send_keys(" and some", Keys.ARROW_DOWN)
It is possible to call send_keys on any element, which makes it possible to test keyboard shortcuts such as those used on GMail. A side-effect of this is that typing something into a text field won’t automatically clear it. Instead, what you type will be appended to what’s already there. You can easily clear the contents of a text field or textarea with the clear method:

element.clear()
3.2. Filling in forms
We’ve already seen how to enter text into a textarea or text field, but what about the other elements? You can “toggle” the state of the drop down, and you can use “setSelected” to set something like an OPTION tag selected. Dealing with SELECT tags isn’t too bad:

element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
This will find the first “SELECT” element on the page, and cycle through each of its OPTIONs in turn, printing out their values, and selecting each in turn.

As you can see, this isn’t the most efficient way of dealing with SELECT elements. WebDriver’s support classes include one called a “Select”, which provides useful methods for interacting with these:

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
WebDriver also provides features for deselecting all the selected options:

select = Select(driver.find_element_by_id('id'))
select.deselect_all()
This will deselect all OPTIONs from that particular SELECT on the page.

Suppose in a test, we need the list of all default selected options, Select class provides a property method that returns a list:

select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options
To get all available options:

options = select.options
Once you’ve finished filling out the form, you probably want to submit it. One way to do this would be to find the “submit” button and click it:

# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()
Alternatively, WebDriver has the convenience method “submit” on every element. If you call this on an element within a form, WebDriver will walk up the DOM until it finds the enclosing form and then calls submit on that. If the element isn’t in a form, then the NoSuchElementException will be raised:

element.submit()
3.3. Drag and drop
You can use drag and drop, either moving an element by a certain amount, or on to another element:

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
3.4. Moving between windows and frames
It’s rare for a modern web application not to have any frames or to be constrained to a single window. WebDriver supports moving between named windows using the “switch_to_window” method:

driver.switch_to_window("windowName")
All calls to driver will now be interpreted as being directed to the particular window. But how do you know the window’s name? Take a look at the javascript or link that opened it:

<a href="somewhere.html" target="windowName">Click here to open a new window</a>
Alternatively, you can pass a “window handle” to the “switch_to_window()” method. Knowing this, it’s possible to iterate over every open window like so:

for handle in driver.window_handles:
    driver.switch_to_window(handle)
You can also swing from frame to frame (or into iframes):

driver.switch_to_frame("frameName")
It’s possible to access subframes by separating the path with a dot, and you can specify the frame by its index too. That is:

driver.switch_to_frame("frameName.0.child")
would go to the frame named “child” of the first subframe of the frame called “frameName”. All frames are evaluated as if from *top*.

Once we are done with working on frames, we will have to come back to the parent frame which can be done using:

driver.switch_to_default_content()
3.5. Popup dialogs
Selenium WebDriver has built-in support for handling popup dialog boxes. After you’ve triggered action that would open a popup, you can access the alert with the following:

alert = driver.switch_to.alert
This will return the currently open alert object. With this object, you can now accept, dismiss, read its contents or even type into a prompt. This interface works equally well on alerts, confirms, prompts. Refer to the API documentation for more information.

3.6. Navigation: history and location
Earlier, we covered navigating to a page using the “get” command ( driver.get("http://www.example.com")). As you’ve seen, WebDriver has a number of smaller, task-focused interfaces, and navigation is a useful task. To navigate to a page, you can use get method:

driver.get("http://www.example.com")
To move backward and forward in your browser’s history:

driver.forward()
driver.back()
Please be aware that this functionality depends entirely on the underlying driver. It’s just possible that something unexpected may happen when you call these methods if you’re used to the behavior of one browser over another.

3.7. Cookies
Before moving to the next section of the tutorial, you may be interested in understanding how to use cookies. First of all, you need to be on the domain that the cookie will be valid for:

# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()


*********************************************************************************************************************************************************************************

 Explicit Waits
An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. There are some convenience methods provided that help you write code that will wait only as long as required. WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
In the code above, Selenium will wait for a maximum of 10 seconds for an element matching the given criteria to be found. If no element is found in that time, a TimeoutException is thrown. By default, WebDriverWait calls the ExpectedCondition every 500 milliseconds until it returns success. ExpectedCondition will return true (Boolean) in case of success or not null if it fails to locate an element.

Expected Conditions

There are some common conditions that are frequently of use when automating web browsers. Listed below are the names of each. Selenium Python binding provides some convenience methods so you don’t have to code an expected_condition class yourself or create your own utility package for them.

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
The expected_conditions module contains a set of predefined conditions to use with WebDriverWait.

Custom Wait Conditions

You can also create custom wait conditions when none of the previous convenience methods fit your requirements. A custom wait condition can be created using a class with __call__ method which returns False when the condition doesn’t match.

class element_has_css_class(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False

# Wait until an element with id='myNewInput' has class 'myCSSClass'
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
Note
polling2 Library

You may also consider using polling2 library which you need to install separately.

5.2. Implicit Waits
An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")

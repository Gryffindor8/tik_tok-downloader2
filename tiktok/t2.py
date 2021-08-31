from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

runDriver = sys.argv[1]
sessionId = sys.argv[2]

def setBrowser():
    if eval(runDriver):
        webdriver = w.Remote(command_executor='http://localhost:4444/wd/hub',
                     desired_capabilities=DesiredCapabilities.CHROME,
                     )
    else:
        webdriver = w.Remote(command_executor='http://localhost:4444/wd/hub',
                             desired_capabilities=DesiredCapabilities.CHROME,
                             session_id=sessionId)

    url = webdriver.command_executor._url
    session_id = webdriver.session_id
    print (url)
    print (session_id)
    return webdriver
setBrowser()

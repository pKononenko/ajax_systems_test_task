
DEVICE_CAPS_ANDROID_TEMPLATE = {
     'autoGrantPermissions': True,
     'automationName': 'uiautomator2',
     'newCommandTimeout': 500,
     'noSign': True,
     'platformName': 'Android',
     'platformVersion': '10',
     "DeviceName": "Redmi Note 8T",
     'resetKeyboard': True,
     'systemPort': 8301,
     'takesScreenshot': True,
     'udid': '93786076',
     'appPackage': 'com.ajaxsystems',
     "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
}


def android_get_desired_cap():
    return DEVICE_CAPS_ANDROID_TEMPLATE

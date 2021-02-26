import json
import time
import allure
import requests
import pytest
from selenium import webdriver
from classes.Browser import Browser
from classes.AdminPage import AdminPage


@allure.step("Waiting for resource availability {url}")
def url_data(url, timeout=10):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="browser", default="chrome")
    parser.addoption("--url", default="http://192.168.0.13", help="This is request url")
    parser.addoption("--bversion", action="store", required=False, default=87.0)
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=False)
    parser.addoption("--executor", action="store", default="192.168.0.13")


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "screenResolution": "1280x720",
        "name": "Tanya",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video,
            "enableLog": logs,
        }
    }

    wd = webdriver.Remote(command_executor=executor_url,
                          desired_capabilities=caps)
    wd.maximize_window()
    allure.attach(
        name=wd.session_id,
        body=json.dumps(wd.desired_capabilities),
        attachment_type=allure.attachment_type.JSON)

    def finalizer():
        log_url = f"{executor}/logs/{wd.session_id}.log"
        video_url = f"http://{executor}:8080/video/{wd.session_id}.mp4"
        wd.quit()

        if request.node.status != 'passed':
            if logs:
                allure.attach(
                    name="selenoid_log_" + wd.session_id,
                    body=url_data(log_url),
                    attachment_type=allure.attachment_type.TEXT)
            if video:
                allure.attach(
                    body=url_data(video_url),
                    name="video_for_" + wd.session_id,
                    attachment_type=allure.attachment_type.MP4)

        # Clear videos and logs from selenoid
        if video and url_data(video_url): requests.delete(url=video_url)
        if logs and url_data(log_url): requests.delete(url=log_url)

        # Add environment info to allure-result
        with open("allure-result/environment.xml", "w+") as file:
            file.write(f"""<environment>
                <parameter>
                    <key>Browser</key>
                    <value>{browser}</value>
                </parameter>
                <parameter>
                    <key>Browser.Version</key>
                    <value>{version}</value>
                </parameter>
                <parameter>
                    <key>Executor</key>
                    <value>{executor_url}</value>
                </parameter>
            </environment>
            """)

    request.addfinalizer(finalizer)
    wd.get(url)
    return wd


# фикстура для HomePage
@pytest.fixture()
def admin_page(remote):
    home = AdminPage(remote)
    return home

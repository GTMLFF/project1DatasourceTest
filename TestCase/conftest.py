# -*-conding:utf-8-*-
import sys
sys.path.append('D:\\Users\\tina.gong\\Pycharmprojects\\untitled')#否则在命令行中执行会报错，找不到common包
import pytest
from config import Config

@pytest.fixture(scope="function")
def setNetworkTimeUrl():
    config = Config.Config()
    add=config.get_value("ip_port","tencentCloud")
    addr = config.get_value("addr", "tencentCloudNetworkTime")
    url = "http://" + add + addr
    yield url



@pytest.fixture(scope="function")
def setStatusUrl():
    config = Config.Config()
    add=config.get_value("ip_port","tencentCloud")
    addr = config.get_value("addr", "tencentCloudStatus")
    url = "http://" + add + addr
    yield url

@pytest.fixture(scope="function")
def setApplySiNanUrl():
    config = Config.Config()
    add=config.get_value("ip_port","tianChuang")
    addr = config.get_value("addr", "tianChuangApplySiNan")
    url = "http://" + add + addr
    yield url

@pytest.fixture(scope="function")
def setWuJianSiNanUrl():
    config = Config.Config()
    add=config.get_value("ip_port","tianChuang")
    addr = config.get_value("addr", "tianChuangWuJianSiNan")
    url = "http://" + add + addr
    yield url

@pytest.fixture(scope="function")
def setCreditSiNanUrl():
    config = Config.Config()
    add=config.get_value("ip_port","tianChuang")
    addr = config.get_value("addr", "tianChuangCreditSiNan")
    url = "http://" + add + addr
    yield url


@pytest.fixture(scope="function")
def setiAudienceV5Url():
    config = Config.Config()
    add=config.get_value("ip_port","jiGuang")
    addr = config.get_value("addr", "jiGuangiAudienceV5")
    url = "http://" + add + addr
    yield url


@pytest.fixture(scope="function")
def setConsumSiNanUrl():
    config = Config.Config()
    add=config.get_value("ip_port","tianChuang")
    addr = config.get_value("addr", "tianChuangConsumSiNan")
    url = "http://" + add + addr
    yield url

@pytest.fixture(scope="function")
def setMicroFinanceScoreV2Url():
    config = Config.Config()
    add=config.get_value("ip_port","tianChuang")
    addr = config.get_value("addr", "tianChuangMicroFinanceScore")
    url = "http://" + add + addr
    yield url


@pytest.fixture(scope="function")
def setCreditSmallScoreV1Url():
    config = Config.Config()
    add=config.get_value("ip_port","tianChuang")
    addr = config.get_value("addr", "tianChuangCreditSmallScore")
    url = "http://" + add + addr
    yield url

@pytest.fixture(scope="function")
def setCreditMiddleBigScoreUrl():
    config = Config.Config()
    add = config.get_value("ip_port", "tianChuang")
    addr = config.get_value("addr", "tianChuangCreditMiddleBigScore")
    url = "http://" + add + addr
    yield url



@pytest.fixture(scope="function")
def setCommerceInfoUrl():
    config = Config.Config()
    add = config.get_value("ip_port", "tianChuang")
    addr = config.get_value("addr", "tianChuangCommerceInfo")
    url = "http://" + add + addr
    yield url

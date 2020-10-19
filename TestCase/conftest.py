# -*-conding:utf-8-*-
import sys
sys.path.append('E:\\TEST\\DataSourceTest')#否则在命令行中执行会报错，找不到common包
import pytest
from config import Config

@pytest.fixture(scope="function")
def setabcUrl():
    config = Config.Config()
    add=config.get_value("ip_port","abc")
    addr = config.get_value("addr", "abc")
    url = "http://" + add + addr
    yield url


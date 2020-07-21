# -*-conding:utf-8-*-


blank_test_data = [
    {'swiftNo': '',               'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202005210001', 'channel': '',           'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202005210002', 'channel': '数据源测试', 'project': '',           'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202005210003', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'idcard': '',                      'mobile': '13000000001'},
    {'swiftNo': '202005210004', 'channel': '数据源测试', 'project': '数据源测试', 'name':'陈田','idcard':'43112120041017640X','mobile': ''}
]

missing_test_data = [
    {'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202005210005', 'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202005210006', 'channel': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202005210007', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'mobile': '13000000001'},
    {'swiftNo': '202005210008', 'channel': '数据源测试', 'project': '数据源测试', 'name':'陈田','idcard':'43112120041017640X'}
]

success_test_data = [
    {'swiftNo': '202005210009', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田','idcard': '43112120041017640X', 'mobile': '13000000001'},
    # {'swiftNo': '2020052100011', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'idcard': '340101198108119852','mobile': '18689262776'}

]

history_test_data = [
    {'swiftNo': '2020052100010', 'channel': '数据源测试', 'project': '数据源测试','name': '陈田','idcard': '43112120041017640X', 'mobile': '13000000001'},
    # {'swiftNo': '2020052100012', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'idcard': '340101198108119852','mobile': '18689262776'}

]


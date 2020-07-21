# -*-conding:utf-8-*-


blank_test_data = [
    {'swiftNo': '',               'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240001', 'channel': '',           'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240002', 'channel': '数据源测试', 'project': '',           'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240003', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'idcard': '',                      'mobile': '13000000001'},
    {'swiftNo': '202004240004', 'channel': '数据源测试', 'project': '数据源测试', 'name':'陈田','idcard':'43112120041017640X','mobile': ''}
]

missing_test_data = [
    {'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240001', 'project': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240002', 'channel': '数据源测试', 'name': '陈田', 'idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240003', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'mobile': '13000000001'},
    {'swiftNo': '202004240004', 'channel': '数据源测试', 'project': '数据源测试', 'name':'陈田','idcard':'43112120041017640X'}
]

success_test_data = [
    # {'swiftNo': '202004240005', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田','idcard': '43112120041017640X', 'mobile': '13000000001'},
    # {'swiftNo': '202004240006', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'idcard': '420000199410171234','mobile': '13000000000'},
    # {'swiftNo': '202004240008', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'idcard': '420000199410171234','mobile': '13000000001'}

]

history_test_data = [
    # {'swiftNo': '202004240006', 'channel': '数据源测试', 'project': '数据源测试','name': '陈田','idcard': '43112120041017640X', 'mobile': '13000000001'},
    {'swiftNo': '202004240007', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'idcard': '420000199410171234','mobile': '13000000000'}

]


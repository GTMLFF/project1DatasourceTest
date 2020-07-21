# -*-conding:utf-8-*-


blank_test_data = [
    {'swiftNo': '',   'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13000000001'},
    {'swiftNo': '202004150001', 'channel': '',           'projectName': '数据源测试', 'mobile': '13000000001'},
    {'swiftNo': '202004150002', 'channel': '数据源测试', 'projectName': '',           'mobile': '13000000001'},
    {'swiftNo': '202004150003', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': ''}
]

missing_test_data = [
    {'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13000000001'},
    {'swiftNo': '202004150004',         'projectName': '数据源测试', 'mobile': '13000000001'} ,
    {'swiftNo': '202004150005',         'channel': '数据源测试',      'mobile': '13000000001'} ,
    {'swiftNo': '202004150006',         'channel': '数据源测试',      'projectName': '数据源测试', } ,
]

success_test_data = [
    # {'swiftNo': '202004150007', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13000010001'} ,
    # {'swiftNo': '202004150008', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13500010001'},
    # {'swiftNo': '202004150009', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13300010001'},
# {'swiftNo': '202004150009', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '17727993685'},
]

history_test_data = [
    # {'swiftNo': '202004150010', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13000010001'} ,
    # {'swiftNo': '202004150011', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13500010001'},
    {'swiftNo': '202004150012', 'channel': '数据源测试', 'projectName': '数据源测试', 'mobile': '13300010001'},
]


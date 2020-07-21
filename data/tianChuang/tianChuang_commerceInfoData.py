# -*-conding:utf-8-*-


blank_test_data = [
    {'swiftNo': '',               'channel': '数据源测试', 'project': '数据源测试', 'companyName': '陈田', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240001', 'channel': '',           'project': '数据源测试', 'companyName': '陈田', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240002', 'channel': '数据源测试', 'project': '',           'companyName': '陈田', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240003', 'channel': '数据源测试', 'project': '数据源测试', 'companyName': '', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240004', 'channel': '数据源测试', 'project': '数据源测试', 'companyName':'陈田','uniformCreditCode':''}
]

missing_test_data = [
    {'channel': '数据源测试', 'project': '数据源测试', 'companyName': '陈田', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240001', 'project': '数据源测试', 'companyName': '陈田', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240002', 'channel': '数据源测试', 'companyName': '陈田', 'uniformCreditCode': '43112120041017640X'},
    {'swiftNo': '202004240003', 'channel': '数据源测试', 'project': '数据源测试', 'uniformCreditCode':'43112120041017640X'},
    {'swiftNo': '202004240004', 'channel': '数据源测试', 'project': '数据源测试', 'companyName':'陈田'}
]

success_test_data = [
    {'swiftNo': '202004240005', 'channel': '数据源测试', 'project': '数据源测试', 'companyName': '朗新一诺(苏州)信息科技有限公司','uniformCreditCode': '913205940662962116'}
]

history_test_data = [
    {'swiftNo': '202004240006', 'channel': '数据源测试', 'project': '数据源测试','companyName': '朗新一诺(苏州)信息科技有限公司','uniformCreditCode': '913205940662962116'},
]


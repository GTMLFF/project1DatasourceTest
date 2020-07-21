# -*-conding:utf-8-*-


blank_test_data = [
    {'swiftNo': '',               'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '43112120041017640X'},
    {'swiftNo': '202005200001', 'channel': '',           'project': '数据源测试', 'name': '陈田', 'id_number': '43112120041017640X'},
    {'swiftNo': '202005200002', 'channel': '数据源测试', 'project': '',           'name': '陈田', 'id_number': '43112120041017640X'},
    {'swiftNo': '202005200003', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '', "phone_md5": ""},
    {'swiftNo': '202005200004', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '', "phone": ""},
    {'swiftNo': '202005200005', 'channel': '数据源测试', 'project': '数据源测试', 'name': '', 'id_number': '', "phone": "13000000000"},
    {'swiftNo': '202005200006', 'channel': '数据源测试', 'project': '数据源测试', 'name': '', 'id_number': '',"phone_md5": "2e65029dcb7a861b3f7d1098da6004be"},
    {'swiftNo': '202005200007', 'channel': '数据源测试', 'project': '数据源测试', 'name':'陈田','id_number':'',"phone": "13000000000"},
    {'swiftNo': '202005200008', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '',"phone_md5": "2e65029dcb7a861b3f7d1098da6004be"}
]

missing_test_data = [
    { 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '43112120041017640X'},
    {'swiftNo': '202005200001', 'project': '数据源测试', 'name': '陈田', 'id_number': '43112120041017640X'},
    {'swiftNo': '202005200002', 'channel': '数据源测试',  'name': '陈田', 'id_number': '43112120041017640X'},
    {'swiftNo': '202005200003', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', },
    {'swiftNo': '202005200004', 'channel': '数据源测试', 'project': '数据源测试', 'name': '', 'id_number': '', "phone_md5": ""},
    {'swiftNo': '202005200005', 'channel': '数据源测试', 'project': '数据源测试', 'name': '', 'id_number': '',"phone": "13000000000"},
    {'swiftNo': '202005200006', 'channel': '数据源测试', 'project': '数据源测试', 'name': '', 'id_number': '',"phone_md5": "2e65029dcb7a861b3f7d1098da6004be"},
    {'swiftNo': '202005200007', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '',"phone": "13000000000"},
    {'swiftNo': '202005200008', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田', 'id_number': '',"phone_md5": "2e65029dcb7a861b3f7d1098da6004be"}

]

success_test_data = [
    # {'swiftNo': '202005200009', 'channel': '数据源测试', 'project': '数据源测试', 'name': '陈田','id_number': '43112120041017640X',"phone": "13000000000"},
    # {'swiftNo': '2020052000010', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'id_number': '350505196203119156',"phone_md5": "2e65029dcb7a861b3f7d1098da6004be"},
]

history_test_data = [
    # {'swiftNo': '2020052000011', 'channel': '数据源测试', 'project': '数据源测试','name': '陈田','id_number': '43112120041017640X',"phone": "13000000000"},
    # {'swiftNo': '2020052000012', 'channel': '数据源测试', 'project': '数据源测试', 'name': '艾草', 'id_number': '350505196203119156',"phone_md5": "2e65029dcb7a861b3f7d1098da6004be"},
]

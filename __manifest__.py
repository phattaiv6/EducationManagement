{
    'name': "education_management",
    'summary': """Quản lý  học sinh""",
    'description': """Quản lý thông tin học sinh""",
    'author': "phattai",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'views/student_views.xml',
        'views/parent_views.xml',
        'views/class_education.xml',
        'views/teacher_views.xml',
        'views/fee_views.xml',
        'views/marksheet_views.xml',
         'views/course_views.xml'


    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
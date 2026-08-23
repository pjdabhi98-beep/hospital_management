{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Healthcare',
    'description': """
        Hospital Management System
        Manage patients, doctors, departments,
        appointments, prescriptions and medical history.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/department_views.xml',
    ],
    'installable': True,
    'application': True,
}
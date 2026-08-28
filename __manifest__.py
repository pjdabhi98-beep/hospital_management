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
        'data/sequence.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'views/department_views.xml',
        'views/prescription_views.xml',
        'views/history_views.xml',
        'views/billing_views.xml',
        'views/consultation_views.xml',

    ],
    'installable': True,
    'application': True,
}
{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Healthcare',
    'description': """
        Hospital Management System
        Manage patients, doctors, appointments,
        prescriptions and medical history.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
    ],
    'installable': True,
    'application': True,
}
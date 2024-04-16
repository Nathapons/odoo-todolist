{
    'name': 'Hospital Management System',
    'author': 'Odoo Mates',
    'summary': 'Odoo 16 Development',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        
        'report/hospital_patient_report.xml',
        'report/hospital_patient_template.xml',
    ],
}

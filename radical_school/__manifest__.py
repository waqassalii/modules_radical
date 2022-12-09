# -*- coding: utf-8 -*-
{
    'name': "radical_school",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        # 'data/admission_form_serial.xml',

        'views/views.xml',
        'views/admission_form.xml',
        'views/teachers.xml',
        'views/radical_resume.xml',
        'views/templates.xml',
        'views/special_class.xml',
        'views/website_special_class.xml',
        'views/website_radical_resume.xml',
        # 'views/teachers.xml',
        # 'views/class_ten.xml',
        # 'views/duplicate_admission_form.xml',
        # 'views/school_classes.xml',
        # 'views/class_students.xml',
        # 'views/templates.xml',
        #
        # 'wizard/class_ten_wizard.xml',

        # 'reports/customise_header.xml',
        # 'reports/radical_school.xml',
        # 'reports/admission_from_report.xml',
        # 'reports/teachers_report.xml',
        # 'reports/class_ten_report.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

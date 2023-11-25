# -*- coding: utf-8 -*- 


{
 'name': 'Manufacturing Work Order dependency management',
 'author': 'Soft-integration',
 'application': False,
 'installable': True,
 'auto_install': False,
 'qweb': [],
 'description': False,
 'images': [],
 'version': '1.0.1',
 'category': 'Manufacturing/Manufacturing',
 'demo': [],
 'depends': ['mrp'],
 'data': [
     'security/mrp_workorder_dependency_security.xml',
     'views/res_config_settings_views.xml',
     'views/mrp_bom_views.xml',
     'views/mrp_routing_views.xml'
    ],
 'license': 'LGPL-3',
 }
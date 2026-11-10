{
    'name':'Smart Purchase',
    'version':'19.0.1.0.0',
    'summary':'Reorder alerts and supplier comparison on top of purchase',
    'category':'Inventory/Purchase',
    'depends':[
            'purchase',
            'stock'
    ],
    'data':[

        'data/cron.xml',
        'views/product_views.xml',
        'views/supplierinfo_views.xml',
        'views/order_warning_views.xml',
        'views/menu.xml'
    ],
    'application':False,
    'installable':True,
    'license': 'LGPL-3',
}
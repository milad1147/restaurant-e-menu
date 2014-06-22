Ext.define('itemsStore', {
    extend: 'Ext.data.Store',
    model: 'Item',
    proxy: {
         type: 'ajax',
         url: '/cgi-bin/dispatcher.py',
         reader: {
             type: 'json',
             root: 'data'
         },
         extraParams: {
            controllerClass: 'admin',
            method: 'getAllItems',
         }
     },
     autoLoad: true

});
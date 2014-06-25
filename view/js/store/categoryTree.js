Ext.define('CategoryTreeStore', {
    extend: 'Ext.data.TreeStore',
    model: 'Category',
    proxy: {
        type: 'ajax',
         url: '/cgi-bin/dispatcher.py',
         reader: {
             type: 'json',
             root: 'data'
         },
         extraParams: {
            controllerClass: 'admin',
            method: 'getCategories',
         }
    },
    folderSort: true,
    autoLoad: false
});
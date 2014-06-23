Ext.define('CategoryTreeStore', {
    extend: 'Ext.data.TreeStore',
    fields: [
        {name: 'catName', type: 'string'},
        {name: 'itemsCount', type: 'int'},
    ],
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
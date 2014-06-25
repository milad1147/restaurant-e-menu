Ext.define('Category', {
    extend: 'Ext.data.Model',
    fields: [
        {name: 'id', type: 'int'},
        {name: 'catName', type: 'string'},
        {name: 'description', type: 'string'},
        {name: 'parent', type: 'int'},
    ]
});
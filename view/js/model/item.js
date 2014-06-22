Ext.define('Item', {
    extend: 'Ext.data.Model',
    fields: [
        {name: 'id', type: 'int'},
        {name: 'name', type: 'string'},
        {name: 'description', type: 'string'},
        {name: 'shortDescription', type: 'string', mapping: 'short_description'},
        {name: 'price', type: 'float'}
    ]
});
Ext.define('ItemsList', {
    extend: 'Ext.container.Container',
    layout: 'border',
    alias: 'widget.itemsList',
        items: [{
            xtype: 'grid',
            region: 'center',
            store: Ext.create('itemsStore'),
            columns: [
                { text: 'Id',  dataIndex: 'id' },
                { text: 'Name', dataIndex: 'name', flex: 1 },
                { text: 'Short Descrition', dataIndex: 'shortDescription', flex: 1 },
                { text: 'Price', dataIndex: 'price' }
            ]
        }]
});
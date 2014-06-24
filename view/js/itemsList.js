Ext.define('ItemsList', {
    extend: 'Ext.panel.Panel',
    layout: 'border',
    alias: 'widget.itemsList',
        items: [{
            xtype: 'grid',
            title: 'Items',
            region: 'center',
            store: Ext.create('itemsStore'),
            columns: [
                { text: 'Id',  dataIndex: 'id' },
                { text: 'Name', dataIndex: 'name', flex: 1 },
                { text: 'Short Descrition', dataIndex: 'shortDescription', flex: 1 },
                { text: 'Price', dataIndex: 'price' },
            {
                text: 'Edit',
                width: 40,
                menuDisabled: true,
                xtype: 'actioncolumn',
                tooltip: 'Edit category',
                align: 'center',
                icon: 'img/edit.png',
                handler: function(grid, rowIndex, colIndex, actionItem, event, record, row) {
                    Ext.Msg.alert('Editing' , record.get('name'));
                },
            }, {
                text: 'Delete',
                width: 40,
                menuDisabled: true,
                xtype: 'actioncolumn',
                tooltip: 'Delete category',
                align: 'center',
                icon: 'img/bin.png',
                handler: function(grid, rowIndex, colIndex, actionItem, event, record, row) {
                    Ext.Msg.alert('Deleting', record.get('name'));
                }
            }]
        }, {
            itemid: 'categories',
            xtype: 'treepanel',
            region: 'west',
            store: Ext.create('CategoryTreeStore'),
            width: 320,
            rootVisible: false,
            title: 'Categories',
            useArrows: true,

            columns: [{
                xtype: 'treecolumn',
                text: 'Name',
                width: 200,
                dataIndex: 'catName',
            }, {
                text: 'Items',
                width: 40,
                dataIndex: 'itemsCount',
            }, {
                text: 'Edit',
                width: 40,
                menuDisabled: true,
                xtype: 'actioncolumn',
                tooltip: 'Edit category',
                align: 'center',
                icon: 'img/edit.png',
                handler: function(grid, rowIndex, colIndex, actionItem, event, record, row) {
                    Ext.Msg.alert('Editing', record.get('catName'));
                },
            }, {
                text: 'Delete',
                width: 40,
                menuDisabled: true,
                xtype: 'actioncolumn',
                tooltip: 'Delete category',
                align: 'center',
                icon: 'img/bin.png',
                handler: function(grid, rowIndex, colIndex, actionItem, event, record, row) {
                    Ext.Msg.alert('Deleting', record.get('catName'));
                },
                isDisabled: function(view, rowIdx, colIdx, item, record) {
                    return !record.data.leaf;
                }
            }]
        }]
});
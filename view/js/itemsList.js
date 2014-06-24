Ext.define('ItemsList', {
    extend: 'Ext.panel.Panel',
    layout: 'border',
    alias: 'widget.itemsList',
        items: [{
            xtype: 'grid',
            id: 'itemsListGrid',
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
            id: 'categories',
            xtype: 'treepanel',
            region: 'west',
            store: Ext.create('CategoryTreeStore'),
            width: 320,
            rootVisible: false,
            title: 'Categories',
            useArrows: true,
            currentCategory: 0,
            listeners: {
                'select': function( grid, record, index, eOpts ){
                        viewport.down('#itemsListGrid').getStore().reload({
                            params: {category_id: record.get('id')}
                        });
                        grid.currentCategory = record.get('id');
                }
            },
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
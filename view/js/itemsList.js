Ext.define('ItemsList', {
    extend: 'Ext.panel.Panel',
    layout: 'border',
    alias: 'widget.itemsList',
        items: [{
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
                text: 'ID',
                width: 40,
                dataIndex: 'id',
            }, {
                xtype: 'treecolumn',
                text: 'Name',
                width: 200,
                dataIndex: 'catName',
            }, {
                text: 'Edit',
                width: 40,
                menuDisabled: true,
                xtype: 'actioncolumn',
                tooltip: 'Edit category',
                align: 'center',
                icon: 'img/edit.png',
                handler: function(grid, rowIndex, colIndex, actionItem, event, record, row) {
                    viewport.down('#categoryEdit').getForm().loadRecord(record);
                    viewport.getLayout().setActiveItem('categoryEdit');
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
            }],
            dockedItems: [{
                xtype: 'toolbar',
                dock: 'top',
                items: [{
                    xtype: 'button',
                    text : 'Add category',
                    icon: 'img/add.png',
                    handler: function() {
                        var newRecord = Ext.create('Category');
                        viewport.down('#categoryEdit').getForm().loadRecord(newRecord);
                        viewport.getLayout().setActiveItem('categoryEdit');
                    },
                }]
            }]
        }, {
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
                    viewport.getLayout().setActiveItem('categoryEdit');
                    viewport.down('#categoryEdit').getForm().loadRecord(record);
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
        }]
});
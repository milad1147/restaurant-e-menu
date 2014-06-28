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
                dataIndex: 'name',
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
                    Ext.Ajax.request({
                        url: '/cgi-bin/dispatcher.py?controllerClass=admin&method=deleteCategory',
                        params: {
                            id: record.get('id')
                        },
                        success: function(response){
                            Ext.Msg.alert('Success', 'Deleted ' + record.get('name'));
                            viewport.down('#categories').getStore().reload();
                        },
                        failure: function(response, opts) {
                            Ext.Msg.alert('Error', 'Failed to delete ' + record.get('name'));
                        }
                    });
                },
                isDisabled: function(view, rowIdx, colIdx, item, record) {
                    return !record.data.leaf;
                }
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
                    Ext.Ajax.request({
                        url: '/cgi-bin/dispatcher.py?controllerClass=admin&method=deleteItem',
                        params: {
                            id: record.get('id')
                        },
                        success: function(response){
                            Ext.Msg.alert('Success', 'Deleted ' + record.get('name'));
                        },
                        failure: function(response, opts) {
                            Ext.Msg.alert('Error', 'Failed to delete ' + record.get('name'));
                        }
                    });
                }
            }]
        }]
});
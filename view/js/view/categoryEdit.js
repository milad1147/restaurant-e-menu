Ext.define('CategoryEdit', {
    extend: 'Ext.form.Panel',
    alias: 'widget.CategoryEdit',
    itemid: 'categoryEdit',

    defaults: {
        padding: '5px 0 0 150px',
    },
    items: [{
        xtype: 'hiddenfield',
        name: 'id',
    }, {
        xtype: 'textfield',
        fieldLabel: 'Category name',
        name: 'name',
        padding: '100px 0 0 150px',
        allowBlank: false
    }, {
        xtype: 'textareafield',
        fieldLabel: 'description',
        name: 'description',
    }, {
        xtype: 'numberfield',
        fieldLabel: 'Parent',
        name: 'parent',
        allowBlank: false
    }],
    buttons: [{
        text: 'Cancel',
        handler: function() {
            this.up('form').getForm().reset();
            viewport.getLayout().setActiveItem('itemsList');
        }
    }, {
        text: 'Save',
        formBind: true,
        disabled: true,

        handler: function() {
            var form = this.up('form').getForm();
            record = form.getRecord();
            if (record.phantom){
                form.url =  '/cgi-bin/dispatcher.py?controllerClass=admin&method=addCategory';
            }
            else{
                form.url =  '/cgi-bin/dispatcher.py?controllerClass=admin&method=updateCategory';
            }
            if (form.isValid()) {
                form.submit({
                    success: function(form, action) {
                       viewport.getLayout().setActiveItem('itemsList');
                       viewport.down('#categories').getStore().reload();
                    },
                    failure: function(form, action) {
                        Ext.Msg.alert('Failed', action.result.message);
                    }
                });
            }
        }
    }],
});
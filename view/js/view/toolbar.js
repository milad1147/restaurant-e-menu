Ext.define('MainToolBar', {
    extend: 'Ext.toolbar.Toolbar',
    alias: 'widget.maintoolbar',
    items: [{
        xtype: 'button',
        text : 'Add category',
        icon: 'img/add.png',
        handler: function() {
            var newRecord = Ext.create('Category');
            viewport.down('#categoryEdit').getForm().loadRecord(newRecord);
            viewport.getLayout().setActiveItem('categoryEdit');
        },
    }, {
        xtype: 'button',
        text : 'Log out',
        handler: function() {
            Ext.Ajax.request({
                url: '/cgi-bin/dispatcher.py',
                params: {
                    controllerClass: 'login',
                    method: 'logOut',
                },
                success: function(response){
                    var r = JSON.parse(response.responseText);
                    if (r.success){
                        viewport.getLayout().setActiveItem('logIn');
                    }
                }
            });
        },
    }]

});
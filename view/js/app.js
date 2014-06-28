/*
Ext.Loader.setConfig({
    enabled: true
});Ext.Loader.setPath('Ext.ux', '../ux');
*/

sessionId = null; 

Ext.onReady(function(){
    viewport = Ext.create('Ext.container.Viewport', {
        itemid: 'maincontainer',
        layout: 'card',
        defaults: {
            dockedItems: [{
                xtype: 'maintoolbar',
                dock: 'top',
            }]
        },
        items: [{
            xtype: 'logIn',
            id: 'logIn',
            title: 'Tablet Choise Admin',
            dockedItems: {}
        }, {
            xtype: 'itemsList',
            id: 'itemsList',
            title: 'Tablet Choise Admin',
        }, {
            xtype: 'CategoryEdit',
            id: 'categoryEdit',
            title: 'Tablet Choise Admin',
        }]
    });

    Ext.Ajax.request({
        url: '/cgi-bin/dispatcher.py',
        params: {
            controllerClass: 'login',
            method: 'checkLoggedIn',
        },
        success: function(response){
            var r = JSON.parse(response.responseText);
            if (r.success){
                viewport.getLayout().setActiveItem('itemsList');
            }
        }
    });
});
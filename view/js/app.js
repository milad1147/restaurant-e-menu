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
        items: [{
            xtype: 'logIn',
            title: 'Tablet Choise Admin',
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
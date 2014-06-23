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
        }]
    });
});
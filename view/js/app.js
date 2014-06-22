sessionId = null; 

Ext.onReady(function(){
    viewport = Ext.create('Ext.container.Viewport', {
        itemid: 'maincontainer',
        layout: 'card',
        items: [{
            xtype: 'logIn'
        }, {
            xtype: 'itemsList',
            id: 'itemsList'
        }]
    });
});
Ext.define('LogIn', {
    extend: 'Ext.form.Panel',
    alias: 'widget.logIn',
    itemid: 'loginform',
    
    url: '/cgi-bin/dispatcher.py?controllerClass=login&method=logIn',

    defaults: {
        xtype: 'textfield',
        allowBlank: false,
    },
    items: [{
        fieldLabel: 'Username',
        name: 'username',
        padding: '100px 0 0 150px',
    },{
        inputType: 'password',
        fieldLabel: 'Password',
        name: 'password',
        padding: '10px 0 0 150px',
    }],

    buttons: [{
        text: 'Reset',
        handler: function() {
            this.up('form').getForm().reset();
        }
    }, {
        text: 'Submit',
        formBind: true,
        disabled: true,
        handler: function() {
            var me = this;
            var form = this.up('form').getForm();
            if (form.isValid()) {
                form.submit({
                    success: function(form, action) {
                       sessionId = action.result.data.sid; // needs to be global
                       viewport.getLayout().setActiveItem('itemsList');
                    },
                    failure: function(form, action) {
                        Ext.Msg.alert('Failed', action.result.message);
                    }
                });
            }
        }
    }],
});
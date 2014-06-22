Ext.define('LogIn', {
    extend: 'Ext.form.Panel',
    title: 'Tablet Choise Admin',
    alias: 'widget.logIn',
    itemid: 'loginform',
    
    // The form will submit an AJAX request to this URL when submitted
    url: '/cgi-bin/dispatcher.py?controllerClass=login&method=logIn',

    // Fields will be arranged vertically, stretched to full width
    layout: 'anchor',
    defaults: {
        anchor: '100%'
    },

    // The fields
    items: [{
        xtype: 'textfield',
        fieldLabel: 'Username',
        name: 'username',
        allowBlank: false
    },{
        xtype: 'textfield',
        inputType: 'password',
        fieldLabel: 'Password',
        name: 'password',
        allowBlank: false
    }],

    // Reset and Submit buttons
    buttons: [{
        text: 'Reset',
        handler: function() {
            this.up('form').getForm().reset();
        }
    }, {
        text: 'Submit',
        formBind: true, //only enabled once the form is valid
        disabled: true,
        handler: function() {
            var me = this;
            var form = this.up('form').getForm();
            if (form.isValid()) {
                form.submit({
                    success: function(form, action) {
                       console.log('Success', action.result.data);
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
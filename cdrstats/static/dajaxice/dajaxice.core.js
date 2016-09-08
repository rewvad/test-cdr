
var Dajaxice = {
    
    

    
    
    cdr_alert: {
    
    delete_whitelist: function(callback_function, argv, custom_settings){
        return Dajaxice.call('cdr_alert.delete_whitelist', 'POST', callback_function, argv, custom_settings);
    },

    add_whitelist_prefix: function(callback_function, argv, custom_settings){
        return Dajaxice.call('cdr_alert.add_whitelist_prefix', 'POST', callback_function, argv, custom_settings);
    },

    add_blacklist_country: function(callback_function, argv, custom_settings){
        return Dajaxice.call('cdr_alert.add_blacklist_country', 'POST', callback_function, argv, custom_settings);
    },

    delete_blacklist: function(callback_function, argv, custom_settings){
        return Dajaxice.call('cdr_alert.delete_blacklist', 'POST', callback_function, argv, custom_settings);
    },

    add_blacklist_prefix: function(callback_function, argv, custom_settings){
        return Dajaxice.call('cdr_alert.add_blacklist_prefix', 'POST', callback_function, argv, custom_settings);
    },

    add_whitelist_country: function(callback_function, argv, custom_settings){
        return Dajaxice.call('cdr_alert.add_whitelist_country', 'POST', callback_function, argv, custom_settings);
    }


    
    
    }
    
,
    


    get_cookie: function(a){var d=null;if(document.cookie&&""!=document.cookie)for(var e=document.cookie.split(";"),b=0;b<e.length;b++){var f=e[b].toString().replace(/^\s+/,"").replace(/\s+$/,"");if(f.substring(0,a.length+1)==a+"="){d=decodeURIComponent(f.substring(a.length+1));break}}return d},

    call: function(b,d,f,c,a){a=a||{};var e=Dajaxice.get_setting("default_exception_callback");"error_callback"in a&&"function"==typeof a.error_callback&&(e=a.error_callback);c="argv="+encodeURIComponent(JSON.stringify(c));a=new XMLHttpRequest;b="/dajaxice/"+b+"/";"GET"==d&&(b=b+"?"+c);a.open(d,b);a.setRequestHeader("Content-Type","application/x-www-form-urlencoded");a.setRequestHeader("X-Requested-With","XMLHttpRequest");a.setRequestHeader("X-CSRFToken",Dajaxice.get_cookie("csrftoken"));
a.onreadystatechange=function(){if(this.readyState==XMLHttpRequest.DONE)if(this.responseText!=Dajaxice.EXCEPTION&&this.status in Dajaxice.valid_http_responses()){var a;try{a=JSON.parse(this.responseText)}catch(b){a=this.responseText}f(a)}else e()};"POST"==d?a.send(c):a.send();return a},

    setup: function(settings)
    {
        this.settings = settings;
    },

    get_setting: function(key){
        if(this.settings == undefined || this.settings[key] == undefined){
            return Dajaxice.default_settings[key];
        }
        return this.settings[key];
    },

    valid_http_responses: function(){
        return {200: null, 301: null, 302: null, 304: null}
    },

    EXCEPTION: 'DAJAXICE_EXCEPTION',
    default_settings: {'default_exception_callback': function(){ }}
};

window['Dajaxice'] = Dajaxice;







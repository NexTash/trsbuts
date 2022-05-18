// Copyright (c) 2019, Framras AS-Izmir and contributors
// For license information, please see license.txt

frappe.ui.form.on('TR UTS Company Settings', {
	// refresh: function(frm) {

	// }
	check_integration: function(frm){
	    if(frm.doc.systemtoken!=""){
	        frappe.call({
	            method: "trsbuts.trsbuts.api.test_integration",
	            args:{
	                test: "real",
                    testtoken: frm.doc.systemtoken
	            },
	            callback: function(r){
                    frm.set_value("result", r.message);
	            }
	        });
	    }
	},
		check_testsystemintegration: function(frm){
	    if(frm.doc.testsystemtoken!=""){
	        frappe.call({
	            method: "trsbuts.trsbuts.api.test_integration",
	            args:{
	                test: "test",
                    testtoken: frm.doc.testsystemtoken
	            },
	            callback: function(r){
                    frm.set_value("testsystemresult", r.message);
	            }
	        });
	    }
	}
});

channels = {"{url_channel}" : {
		"name" : {"xpath" : "/html/body/div/h1//text()", "regex":u"(.*)"},
		"date" : { "xpath": "/html/body/div/div[1]/div[1]/a//text()", 
		           "regex":".*([0-9]{1,2}-[0-9]{1,2}-[0-9]{2,4})", 
		           "add_days": 1, 
		           "date_format" : "%d-%m-%Y"},
		"programmes":{
			"xpath":"/html/body/div/div[2]/div[1]/table//tr",
			"inner_xpaths":{
				"time" : "./td//text()", 
				"title" : "./td[2]/p[1]/strong/a//text()", 
				"description" : "./td[2]/p[2]//text()", 
				"category" : "./td[2]/p[3]//text()", 
			}
		}
		
	}	
}

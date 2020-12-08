function updateDate(){
	temp = new Date(start_date.value);
	timezone_offset = temp.getTimezoneOffset()/60; 
	temp.setHours(temp.getHours() + (1-timezone_offset));
	end_date.value = temp.toISOString().split(".")[0].slice(0,-3);
}
function updateDate(){
	temp = new Date(start_date.value)
	temp.setHours(temp.getHours() + 1)
	end_date.value = temp.toISOString().split(".")[0]
}
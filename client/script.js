generate_button = document.getElementById("button")
generate_button_text = document.getElementById("button_text")
text_area = document.getElementById("text")

console.log(text_area.value)

generate_button.onclick = () => {
	text_area.disabled = true
	generate_button.disabled = true
	setTimeout(() => {
		generate_button_text.innerHTML = "Working..."
	}, 500)
	fetch(`/api/request/${text_area.value}`, {
		method: 'GET',
		headers: {
			'Content-Type': 'text/plain;charset=utf-8'
		}
	}).then(res => {
		res.text().then((text) => {
			text_table = text.split(" ")
			setTimeout(() => {
				for (let i = 0; i < text_table.length; i++){
					setTimeout(() => {text_area.value += text_table[i] + " "}, i * 75)
				}
				text_area.disabled = false
				generate_button.disabled = false
				setTimeout(() => {
					generate_button_text.innerHTML = "Generate"
				}, 500)
			}, 1000)
		});
		console.log(res);
	}).catch(() => {
	})
}
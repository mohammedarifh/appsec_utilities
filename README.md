# *appsec_utilities*
### *bunch of handy scripts created for day2day assessments.*

*__[Base64JSONInjector.py](./Base64JSONInjector.py)__ - To inject multiple payloads via Intruder when the target application sends JSON data encoded in Base64. You can specify which key-value pair you want to inject the payloads from the list you have included in the script. Also, it outputs line by line of base64 data into a separate file using: `python3 Base64JSONInjector.py > output.txt`. Then, paste the output into Burp Intruder for reducing manual effort in such scenarios.*

*__[bulkJSONescaper.py](./bulkJSONescaper.py)__ - Provide bulk-escaped payloads for your list, which are useful when JSON data is used in the HTTP body. This will help when you need to use an intruder with such payloads passed in JSON.* <br>
*`python ./bulkJSONescaper.py --help`<br>*
*`python ./bulkJSONescaper.py payloads.txt --output escaped_payloads.txt`*

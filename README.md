# *appsec_utilities*
### *bunch of handy scripts created for day2day assessments.*

*__[Base64JSONInjector.py](./Base64JSONInjector.py)__ - To inject multiple payloads via Intruder when the target application sends JSON data encoded in Base64. You can specify which key-value pair you want to inject the payloads from the list you have included in the script. Also, it outputs line by line of base64 data into a separate file using: `python3 Base64JSONInjector.py > output.txt`. Then, paste the output into Burp Intruder for reducing manual effort in such scenarios.*

*__[bulkJSONescaper.py](./bulkJSONescaper.py)__ - Provide bulk-escaped payloads for your list, which are useful when JSON data is used in the HTTP body. This will help when you need to use an intruder with such payloads passed in JSON.* <br>
*`python ./bulkJSONescaper.py --help`<br>*
*`python ./bulkJSONescaper.py payloads.txt --output escaped_payloads.txt`*

*__[aes128-ECBCrypt.py](./aes128-ECBCrypt.py)__ - Decrypt-Encrypt Tool for HTTP Body Encrypted with AES-128 in ECB Mode and Base64 Encoding.
This tool is useful for penetration testers when the HTTP body is encrypted using AES-128 in ECB mode and then encoded in Base64. In such scenarios, this script provides a convenient method to decrypt the data in the HTTP body, inject payloads, encrypt it again, and send it to the application server using the relevant key. Compared to online tools, this method is risk-free.* <br> 

*[Key]: In many cases, when developers implement encryption for the HTTP body, they may hardcode the encryption key in client-side scripts, such as JavaScript within the application itself. Investing some time in inspecting the .js file is often worthwhile to retrieve the key needed to successfully encrypt or decrypt the data.* <br>
***Dependencies** - `pip3 install pycryptodome`*<br>
***Format** -`python aes128-ECBCrypt.py decrypt/encrypt <string>`* <br>
***Example -*** <br>
![image](https://github.com/user-attachments/assets/cabdac45-3eb4-4d22-bed7-f4138bb33b14) 
*Please note that if the decrypted data is in formats like JSON, you need to properly escape both single and double quotes accordingly.*

 

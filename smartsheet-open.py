#!/usr/bin/env python3
#testscript

import requests, smartsheet, json
ss_client = smartsheet.Smartsheet('4uo70rktnsyrjekbzl8lu514ft')
user_profile = ss_client.Users.get_current_user()


print(user_profile)
supSku = "JTK0701"
result = ss_client.Search.search(supSku)

print(json.dumps(result.to_json(),sort_keys=True,indent=4, separators=(',', ': ')))

import requests
import json
import meraki_info


def get_inven_org():
    baseurl = meraki_info.base_url
    key = meraki_info.key
    org_id = '681155'
    url = f'{baseurl}/organizations/{org_id}/inventory/devices'
    header = {
        'X-Cisco-Meraki-API-Key': key
    }
    response = requests.get(url, headers=header)
    r = response.json()
    # print(json.dumps(r, indent=4))
    return r


def get_null_device(res):
    num = len(res)
    ls = []
    for i in range(num):
        network = res[i]['networkId']
        if network is None:
            ls.append(res[i]['mac'])
            # print(json.dumps(r[i], indent=4))
    print(ls)


r = get_inven_org()
get_null_device(r)


import sys
from infinispan.remotecache import RemoteCache

hostname = 'datagrid-hotrod'
port = 11333
itemID = 'SalesItem13'

remote_cache = RemoteCache(host=hostname, port=port)

def addRecord(itemID):
    [miss, val] = remote_cache.put_if_absent(itemID, '1', ret_prev=True)

    if miss == False:
        remote_cache.put(itemID, str(int(val)+1))

addRecord(itemID)
salesItem = remote_cache.get(itemID)
print('Sales of item: ' + salesItem)


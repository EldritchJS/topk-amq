import sys
from infinispan.remotecache import RemoteCache

remote_cache = RemoteCache(host='datagrid-hotrod', port=11333)

remote_cache.put('SalesItem5', '500')
salesItem5 = remote_cache.get('SalesItem5')
print('Sales of item 5: ' + salesItem5)

remote_cache.put('SalesItem5', '550')
salesItem5 = remote_cache.get('SalesItem5')
print('Sales of item 5: ' + salesItem5)


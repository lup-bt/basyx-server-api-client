from __future__ import print_function
import time
import basyx_server
from basyx_server.rest import ApiException
from pprint import pprint
from basyx_server.configuration import Configuration

configuration = Configuration()
configuration.host = "http://localhost:4001/aasServer/"

# create an instance of the API class
api_instance = basyx_server.AssetAdministrationShellRepositoryApi(basyx_server.ApiClient(configuration))

aas_id = "https://lup.uni-bayreuth.de/BoxAAS"

submodel_id_short = 'ArucoSubmodel' # str | The Submodel's short id
se_id_short_path = 'x' # str | The Submodel-Element's IdShort-Path
body = 42.3 # object | The new value (optional)

try:
    # Updates the Submodel-Element's value
    api_instance.shell_repo_put_submodel_element_value_by_id_short(aas_id, submodel_id_short, se_id_short_path, body=body)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryApi->shell_repo_put_submodel_element_value_by_id_short: %s\n" % e)
import datetime
import logging

import utils.gql as gql

from utils.oc import OC_Map

CLUSTERS_QUERY = """
{
  clusters: clusters_v1 {
    name
    serverUrl
    managedGroups
    jumpHost {
      hostname
      knownHosts
      user
      port
      identity {
        path
        field
        format
      }
    }
    automationToken {
      path
      field
      format
    }
    disable {
      e2eTests
    }
  }
}
"""

E2E_NS_PFX = 'e2e-test'


def get_oc_map(test_name):
    gqlapi = gql.get_api()
    clusters = gqlapi.query(CLUSTERS_QUERY)['clusters']
    return OC_Map(clusters=clusters, e2e_test=test_name)

def get_test_namespace_name():
    return '{}-{}'.format(
        E2E_NS_PFX, datetime.datetime.utcnow().strftime('%Y%m%d%H%M')
    )

def assert_rolebinding(expected_rb, rb):
    assert expected_rb['role'] == rb['roleRef']['name']
    assert expected_rb['groups'] == rb['groupNames']
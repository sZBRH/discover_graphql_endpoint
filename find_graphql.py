import os
import sys
import requests
import json

def find_graphql():
    target_list = [line.split(",")[0] for line in open(sys.argv[1], "r").readlines() if not line.split(",")[0] == ""]
    return target_list

def query_get(target_list, endpoint_list, output_file):    
    for target in target_list:
        for endpoint in endpoint_list:
            try:
                req_get = requests.get(target + "/" + endpoint + "?query={x}", allow_redirects=False, timeout=3)
                req_get.json()
                print("GraphQL Founded [GET] -> " + target + "/" + endpoint)
                output_file.write(target + "/" + endpoint + ",GET\n")
            except (ValueError, requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as err:
                print("No GraphQL [GET] -> " + target + "/" + endpoint)

def query_post(target_list, endpoint_list, output_file):    
    for target in target_list:
        for endpoint in endpoint_list:
            try:
                req_get = requests.post(target + "/" + endpoint, allow_redirects=False, data="{x}", timeout=3)
                req_get.json()
                print("GraphQL Founded [POST] -> " + target + "/" + endpoint)
                output_file.write(target + "/" + endpoint + ",POST\n")
            except (ValueError, requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as err:
                print("No GraphQL [POST] -> " + target + "/" + endpoint)

if __name__ == "__main__":
    output_file = open(sys.argv[2], "a+")
    endpoint_list = ["graphql", "graphql/console", "graphiql.php"]
    target_list = find_graphql()
    query_get(target_list, endpoint_list, output_file)
    query_post(target_list, endpoint_list, output_file)
    f_output.close()

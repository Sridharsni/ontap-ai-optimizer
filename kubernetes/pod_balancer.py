from kubernetes import client, config

def rebalance_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name} | Node: {pod.spec.node_name}")

if __name__ == '__main__':
    rebalance_pods()
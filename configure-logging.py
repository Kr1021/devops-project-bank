import json

def configure_elk():
    config = {
        "logstash_host": "logstash.scotiabank.internal",
        "elasticsearch_index": "scotia-app-logs",
        "kibana_dashboard": True
    }
    with open("elk-config.json", "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    configure_elk()

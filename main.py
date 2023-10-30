import yaml


def merge_configs(base, override):
    for key, value in override.items():
        if isinstance(value, dict) and key in base:
            base[key] = merge_configs(base[key], value)
        else:
            base[key] = value
    return base


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load main config
    with open('configs/defaults.yaml', 'r') as base_file:
        sit_data = yaml.safe_load(base_file)

    # load dev config - more debug/dev api keys
    with open('configs/production.yaml', 'r') as override_file:
        prod_data = yaml.safe_load(override_file)

    merged_data = merge_configs(sit_data, prod_data)

    # load local config / local dabatase
    with open('configs/local.yaml', 'r') as override_file:
        uat_data = yaml.safe_load(override_file)

    merged_data = merge_configs(merged_data, uat_data)

    print(yaml.dump(merged_data, default_flow_style=False))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
